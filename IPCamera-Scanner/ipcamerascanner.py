import socket
import ipaddress

def read_subnet_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                ip_address = lines[0].strip()
                subnet_mask = lines[1].strip()
                subnet = ipaddress.IPv4Interface(f"{ip_address}/{subnet_mask}").network
                return subnet
    except Exception as e:
        print("Error reading subnet from file:", e)
    return None

def scan_subnet(subnet, port):
    for ip in subnet.hosts():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((str(ip), port))
                if result == 0:
                    print(f"IP Camera found at: {ip}:{port}")
        except:
            pass

if __name__ == "__main__":
    subnet_file = "subnet.txt"
    local_subnet = read_subnet_from_file(subnet_file)

    if local_subnet:
        camera_port = 554  # Change this to the appropriate port for IP cameras (e.g., 80 for HTTP)

        print(f"Scanning subnet {local_subnet.network_address}/{local_subnet.prefixlen} for IP cameras on port {camera_port}")
        scan_subnet(local_subnet, camera_port)
    else:
        print("Subnet reading failed from the file.")
