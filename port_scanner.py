import socket
import datetime
import sys

def scan_ports(target, start_port, end_port):
    print("=" * 50)
    print(f"Port Scanner - Cybersecurity Tool")
    print(f"Target: {target}")
    print(f"Scanning ports {start_port} to {end_port}")
    print(f"Started at: {datetime.datetime.now()}")
    print("=" * 50)

    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolved IP: {target_ip}\n")
    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
        sys.exit()

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[OPEN] Port {port} --> {service}")
            open_ports.append(port)
        sock.close()

    print("\n" + "=" * 50)
    print(f"Scan complete. {len(open_ports)} open port(s) found.")
    print(f"Finished at: {datetime.datetime.now()}")
    print("=" * 50)

# --- Main ---
if __name__ == "__main__":
    target = input("Enter target (hostname or IP): ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_ports(target, start, end)
