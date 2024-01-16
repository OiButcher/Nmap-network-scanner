# network_scanner_nmap.py

import nmap

def nmap_scan(target, options="-p 1-1000"):
    """
    Perform a network scan using Nmap.
    :param target: IP address or hostname of the target
    :param options: Additional Nmap scan options (default: -p 1-1000)
    :return: Nmap scan results
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments=options)

    return nm.all_hosts(), nm.csv()

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace with the IP address or hostname of your target
    scan_results = nmap_scan(target_ip)
    
    hosts, csv_results = scan_results
    print(f"Nmap scan results for {target_ip}:")
    
    for host in hosts:
        print(f"Host: {host}")
        print(f"Open Ports: {csv_results[host]['tcp'].keys()}")
        # Add more details as needed
        print()

