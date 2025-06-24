import socket
import threading
import os
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

HOST = 'localhost'
PORT = 65432

# ------------- Crypto Utils -------------
def generate_keys():
    key = RSA.generate(2048)
    with open("private.pem", "wb") as priv:
        priv.write(key.export_key())
    with open("public.pem", "wb") as pub:
        pub.write(key.publickey().export_key())

def load_keys():
    if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
        generate_keys()
    private_key = RSA.import_key(open("private.pem").read())
    public_key = RSA.import_key(open("public.pem").read())
    return private_key, public_key

def encrypt_message(msg, pubkey):
    cipher = PKCS1_OAEP.new(pubkey)
    return cipher.encrypt(msg.encode())

def decrypt_message(ciphertext, privkey):
    cipher = PKCS1_OAEP.new(privkey)
    return cipher.decrypt(ciphertext).decode()

# ------------- GUI App Class -------------
class SecureChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🔐 Secure Chat")
        self.chat_log = Text(master, state=DISABLED, bg="#f0faff", wrap=WORD)
        self.chat_log.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.entry = Entry(master)
        self.entry.pack(fill=X, padx=10, pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        self.private_key, self.public_key = load_keys()
        self.sock = None
        self.peer_key = None
        self.start_connection()

    def start_connection(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            self.sock.sendall(self.public_key.export_key())  # Send as bytes
            self.peer_key = RSA.import_key(self.sock.recv(4096))
            self.log("Connected as client.")
        except:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((HOST, PORT))
            server.listen(1)
            self.log("Waiting for client to connect...")
            self.sock, _ = server.accept()
            self.peer_key = RSA.import_key(self.sock.recv(4096))
            self.sock.sendall(self.public_key.export_key())
            self.log("Client connected.")

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def log(self, message):
        self.chat_log.config(state=NORMAL)
        self.chat_log.insert(END, f"{message}\n")
        self.chat_log.config(state=DISABLED)
        self.chat_log.yview(END)

    def send_message(self, event=None):
        msg = self.entry.get()
        if msg and self.peer_key:
            try:
                encrypted = encrypt_message(msg, self.peer_key)
                self.sock.sendall(encrypted)
                self.log(f"You: {msg}")
            except Exception as e:
                self.log(f"[Error sending]: {e}")
            self.entry.delete(0, END)

    def receive_messages(self):
        while True:
            try:
                data = self.sock.recv(4096)
                if not data:
                    self.log("Disconnected.")
                    break
                msg = decrypt_message(data, self.private_key)
                self.log(f"Peer: {msg}")
            except Exception as e:
                self.log(f"[Error receiving]: {e}")
                break

# ------------- Start GUI -------------
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x500")
    app = SecureChatApp(root)
    root.mainloop()