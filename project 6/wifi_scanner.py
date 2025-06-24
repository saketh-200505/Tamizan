import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    iface.scan()
    time.sleep(3)  # Wait a few seconds for the scan to complete
    
    results = iface.scan_results()
    seen = set()
    print("{:<30} {:<15} {:<10}".format("SSID", "Signal (dBm)", "Security"))
    print("-" * 60)
    
    for network in results:
        # Avoid duplicate SSIDs (optional)
        if network.ssid not in seen:
            seen.add(network.ssid)
            signal = network.signal
            auth = network.akm[0] if network.akm else "Open"
            print("{:<30} {:<15} {:<10}".format(network.ssid, signal, auth))

if __name__ == "__main__":
    scan_wifi()