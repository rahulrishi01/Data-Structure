"""
Given an IP address, remove leading zeros from the IP address.

Examples:

Input : 100.020.003.400
Output : 100.20.3.400

Input :001.200.001.004
Output : 1.200.1.4
"""


def correct_ip(ip):
    return ".".join(str(int(i)) for i in ip.split('.'))


if __name__ == '__main__':
    ip = '100.020.003.400'
    ip1 = '001.200.001.004'
    print(correct_ip(ip))
    print(correct_ip(ip1))
