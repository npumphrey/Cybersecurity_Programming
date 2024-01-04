import argparse
import socket
import requests



def arg_accepter():
    parser = argparse.ArgumentParser(description='Accept domain name')

    parser.add_argument('--domain', '-d', required=True, help='domain name')
    args=parser.parse_args()

    return args

def host():
    args = arg_accepter()
    domain = args.domain
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f"Could not resolve the IP address for {domain}")
    else:
        print(f"The IP address of {domain} is {ip_address}.")
        return ip_address
    

def api(ip_address):
    try:
        response_API = requests.get(f'https://internetdb.shodan.io/{ip_address}')
        response_API.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"IP address was not found")
    else:
        data = response_API.json()
        cpes = data['cpes']
        hostnames = data['hostnames']
        print(f"There are {len(cpes)} CPEs.")
        for cpe in cpes:
            print(cpe)
        
        print(f"There are {len(hostnames)} hostnames.")
        for hostname in hostnames:
            print(hostname)

def main():
    ip_address = host()
    api(ip_address)

    

    

if __name__ == '__main__':
    main()