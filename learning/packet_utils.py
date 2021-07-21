
def mk_broadcast(packet):
    return packet[0:24] + "8888" + packet[24:]

def mk_mac_key(mac):
    return str(int(mac,16))

def get_dst_mac(packet):
    return packet[0:12]

def get_src_mac(packet):
    return packet[12:24]
