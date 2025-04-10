from scapy.all import *

# Switch port mapping
intf_dict = {"veth0": 0, "veth2": 1,
             "veth4": 2, "veth6": 3,
             "veth8": 4, "veth10": 5,
             "veth12": 6, "veth14": 7}

# Print revceived packets and received interface info
def process_packet(pkt):
    """
    Handles inbound packet
    """
    print("----------")
    print(f"Received packet on interface: {pkt.sniffed_on} (port {intf_dict[pkt.sniffed_on]})")
    print(pkt.summary())

# Sniff asyn on all switch ports
sniffer = AsyncSniffer(iface = ["veth0", "veth2","veth4", "veth6", "veth8", "veth10", "veth12", "veth14"],
                       prn = process_packet, store = False)
sniffer.start()

port2_pwd = Ether(dst = "02:02:02:ef:ef:ef")
port3_pwd = Ether(dst = "03:03:03:ef:ef:ef")
