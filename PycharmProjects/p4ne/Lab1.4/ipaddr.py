import ipaddress
import random


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
#        network = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) \
#                  + '.' + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
#        mask = '/' + str(random.randint(0, 32))
        net_and_mask = ((random.randint(0x20000000,0xE0000000)),(random.randint(0, 32)))
#        net_and_mask = network + mask
        ipaddress.IPv4Network.__init__(self,net_and_mask, strict=False)
#        net = '0.0.0.0/'
#        net1 = ipaddress.IPv4Network.__init__(self,net + str(random.randint(0,32)))
#        print (net1)

# network = str(random.randint(1,254)) + '.' + str(random.randint(1,254)) + '.' + str(random.randint(1,254))+ '.' + str(random.randint(1,254))
# mask = '/' + str(random.randint(1,32))
# net_and_mask = network + mask
# for i in range(1,20):
#    net1 = IPv4RandomNetwork()
#    print (net1)
def sortfunc (ipnet):
    return int(ipnet.network_address._ip) + int(ipnet.netmask._ip * 2**32)
list1 = []
for i in range(0,20):
    list1.append (IPv4RandomNetwork())
list2 = (sorted(list1, key=sortfunc))
for x in list2:
    print (x)



