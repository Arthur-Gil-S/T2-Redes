
in_file = ''
command = ''
source = ''
destiny = ''

def read_input():
    global in_file, command, source, destiny
    cmd_line = input()
    cmd_line = cmd_line.split(' ')
    in_file = cmd_line[0]
    command = cmd_line[1]
    source = cmd_line[2]
    destiny = cmd_line[3]
    
read_input()

nodes = []
routers = []
routertable = []
with open(in_file, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        if line == '#ROUTER':
            break
        nodes.append(line)
    nodes.remove('#NODE')
    for line in lines:
        if line in nodes:
            continue
        if line == '#ROUTERTABLE':
            break
        routers.append(line)
    routers.remove('#NODE')
    routers.remove('#ROUTER')
    for line in lines:
        if line in nodes or line in routers:
            continue
        routertable.append(line)
    routertable.remove('#NODE')
    routertable.remove('#ROUTER')
    routertable.remove('#ROUTERTABLE')


class Node():
    def __init__(self, node_name, mac, ip_prefix, gateway):
        self.node_name = node_name
        self.mac = mac
        self.ip_prefix = ip_prefix
        self.gateway = gateway

    def print_node(self):
        print(self.node_name, self.mac, self.ip_prefix, self.gateway)
    
nodes = [n.split(',') for n in nodes]    
nodes = [Node(n[0],n[1],n[2],n[3]) for n in nodes]
print('Nodes')
for n in nodes:
    n.print_node()


class Router():
    def __init__(self, router_name, num_ports, mac_iprefix):
        self.router_name = router_name
        self.num_ports = num_ports
        self.mac_iprefix = mac_iprefix
        
    def print_router(self):
        print(self.router_name, self.num_ports, self.mac_iprefix)

routers = [r.split(',') for r in routers]
mac_ip = []
for r in routers:
    mac_ip.append(r[2:])

mac_ip = mac_ip[0]
macs = []
ips = []

for mi in mac_ip:
    if mi.__contains__(':'):
        macs.append(mi)
    else:
        ips.append(mi)

mac_ip = [(mac,ip) for mac,ip in zip(macs, ips)]

routers = [Router(r[0],r[1], mac_ip) for r in routers]
print('Routers')
for r in routers:
    r.print_router()


class Routertable():
    def __init__(self, router_name, net_dest_prefix, nexthop, port):
        self.router_name = router_name
        self.net_dest_prefix = net_dest_prefix
        self.nexthop = nexthop	
        self.port = port

    def print_routertable(self):
        print(self.router_name, self.net_dest_prefix, self.nexthop, self.port)

routertable = [rt.split(',') for rt in routertable]
routertable = [Routertable(rt[0],rt[1],rt[2],rt[3]) for rt in routertable]
print('Routertable')
for rt in routertable:
    rt.print_routertable()

