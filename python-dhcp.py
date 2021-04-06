from scapy.all import Ether,IP,UDP,DHCP,BOOTP,get_if_raw_hwaddr,get_if_hwaddr,conf,sniff,sendp

src_mac_address="00:90:0b:30:3a:90"
hw="caros"

ethernet = Ether(dst='ff:ff:ff:ff:ff:ff',src=src_mac_address,type=0x800)
ip = IP(src ='0.0.0.0',dst='255.255.255.255')
udp = UDP (sport=68,dport=67)
bootp = BOOTP(chaddr = hw, ciaddr = '0.0.0.0',xid =  0x01020304,flags= 1)
dhcp = DHCP(options=[("message-type","discover"),"end"])

packet = ethernet / ip / udp / bootp / dhcp

sendp(packet, iface="enp3s0.2")
