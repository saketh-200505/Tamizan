import socket
import threading

# Function to scan a single port
def scan_port(target, port, lock):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target, port))
        with lock:
            print(f"[+] Port {port} is open")
        s.close()
    except:
        pass  # Port is closed or unreachable

# Function to scan multiple ports with threading and limited concurrency
def port_scanner(target, start_port, end_port, max_threads=100):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    lock = threading.Lock()  # Prevent output overlap
    threads = []

    for port in range(start_port, end_port + 1):
        if len(threads) >= max_threads:  # Avoid excessive threading
            for thread in threads:
                thread.join()
            threads.clear()  

        thread = threading.Thread(target=scan_port, args=(target, port, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Command-line interface with domain resolution
if __name__ == "__main__":
    try:
        target = input("Enter target IP or domain: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        # Resolve domain to IP if necessary
        target = socket.gethostbyname(target)
        print(f"Resolved IP: {target}")

        port_scanner(target, start_port, end_port)
    except ValueError:
        print("Invalid input! Please enter numerical values for ports.")
    except socket.gaierror:
        print("Invalid domain! Could not resolve IP address.")