import scapy.all as scapy
import optparse

#arp_request -- broadcast --response sirasiyla yapicaz

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst = ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    combined_packet = broadcast_packet / arp_request_packet
    answered_list, unanswered_list= scapy.srp(combined_packet,timeout = 1)
    answered_list.summary()

def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-s", "--sourceip", dest="ip", help="Source ip")
    user_input, arguments = parse_object.parse_args()

    if not user_input.ip:
        print("Enter IP adress")

    return user_input.ip

ip = get_input()
scan_network(ip)
