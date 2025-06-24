
🔐 Secure Chat Application
A lightweight, end-to-end encrypted chat application in Python using RSA encryption, sockets for network communication, and a Tkinter GUI for real-time messaging. It supports peer-to-peer encrypted chat over localhost—ideal for testing and educational use.

💡 Features
- 🔑 RSA public/private key generation and exchange
- 🔐 Message encryption using PKCS1_OAEP with 2048-bit RSA
- 🌐 Peer discovery with automatic server/client role selection
- 💬 Clean, scrollable chat interface powered by Tkinter
- 🔁 Simultaneous message sending and receiving using threads

🧱 How It Works
- Generates RSA key pairs and saves them to private.pem and public.pem.
- One user starts the script first (auto-acts as server), the second becomes the client.
- They exchange public keys over a secure socket connection.
- All messages sent are encrypted using the peer’s public key, and decrypted using the user’s private key.
- Messages appear in a chat log within the Tkinter GUI.
