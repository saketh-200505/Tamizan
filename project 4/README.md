
🔍 Multi-threaded Port Scanner
A Python-based TCP port scanner that uses multi-threading for speed and efficiency. Resolves domain names to IP addresses and scans user-defined port ranges to identify open ports.

🚀 Features
- 📡 Scans any domain or IP address
- ⚡ Supports concurrent scanning with customizable thread limit
- 🔐 TCP connect-based scanning (non-stealth)
- 🧵 Thread-safe console output for clean readability
- 🔧 Handles input errors and domain resolution exceptions

🧠 How It Works
- Accepts a target IP or domain name and port range from the user.
- Resolves domain to its corresponding IP address.
- Spawns threads to scan ports in parallel using socket.connect() on each.
- Prints which ports are open.
