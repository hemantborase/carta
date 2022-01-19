import re
import ipaddress
from flask import Flask

#Extract IPs from the logs and create bucket for unique Ips with number of occurences
def get_ips_from_logs(filename):
    ip_count = {}
    # Regex for IPv4
    ip_pattern = re.compile(r'(?:\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?)')

    # Loading the contents of the log file
    with  open(filename, 'r') as f:
        text_to_search = f.read()
    # Finding all the IPs
    results = ip_pattern.findall(text_to_search)

    # Loop to print all the IPv4 addresses
    for result in results:
        if result in ip_count:
            ip_count[result] += 1 
        else:
            ip_count[result] = 1

    for ip, count in ip_count.items():
        print(f'Address {ip} was encountered {count} time(s)')

    return ip_count

#Place the Ips to respective cidr blocks and count how many ips are in the particuler cidr range
def get_cidr_count(ip_count):

    cidr_list = ['108.162.0.0/16','212.129.32.128/25','173.245.56.0/23']
    cidr_ips = {}
    for cidr in cidr_list:
        for ip in ip_count.keys():
            a_network = ipaddress.ip_network(cidr)
            an_address = ipaddress.ip_address(ip)
            if an_address in a_network:
                if a_network.with_prefixlen in cidr_ips:
                    cidr_ips[a_network.with_prefixlen] += 1
                else:
                    cidr_ips[a_network.with_prefixlen] = 1
    print("------------------------------------------------")
    for cidr, counter in cidr_ips.items():
        print(f'The bucket {cidr} contains {counter} addresses')
    
    return {"buckets":cidr_ips}

app = Flask(__name__)


@app.route('/')
def cidr_buckets():
    return cidrs


if __name__ == "__main__":
    ips = get_ips_from_logs(filename='nginx.log')
    cidrs = get_cidr_count(ips)

    app.run(host="0.0.0.0", port=8080, debug=True)


