#!/usr/bin/python
#title           :snmpTest.py
#description     :This program will demonstrate SNMP agent & client communication, within hosts of mininet emulation
#author          :kspviswa
#date            :20-June-2015
#version         :0.1
#usage           :python snmpTest.py (or) ./snmpTest.py
#license         :MIT License
#python_version  :2.7.6
#project_link    :https://github.com/kspviswa/py-playground  
#==============================================================================


from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

# Setting global data
SNMP_START_CMD = '/usr/sbin/snmpd -Lsd -Lf /dev/null -u snmp -I -smux -p /var/run/snmpd.pid -c /etc/snmp/snmpd.conf'
SNMP_WALK_CMD = 'snmpwalk -v 1 -c public -O e '
SNMP_WALK_OUT = 'dump.out'
COMMAND_BANNER = '\n\n*******************************************************************\n             MININET - SNMP WALK - DEMO APPLICATION                \n*******************************************************************\n\n'
                  


def simulateNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    net.addController(name='c0')

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')

    info( '*** Add host 1\n')
    h1 = net.addHost('h1')
    
    info( '*** Add host 2\n')
    h2 = net.addHost('h2')

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info( '*** Starting network\n')
    net.start()

    h1IP = h1.IP()
    
    info( '*** Starting SNMP agent in h1\n')
    h1.cmd(SNMP_START_CMD)

    info ('\n\n SNMPd started successfuly\n\n')

    info( '*** Performing SNMP walk from h2 to h1\n')
    h2.cmd(SNMP_WALK_CMD+h1IP+'>>'+SNMP_WALK_OUT)

    info ('\n SNMP walk completed succeessfully\n')

    info( '*** Showing first 10 entries of the walked data\n\n')
    walkOut = h2.cmd('head -10 '+SNMP_WALK_OUT)
    info('\n'+walkOut+'\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    info(COMMAND_BANNER)
    info( '\tThis script will host a simple network of 2 hosts connected to single switch, \n\trun SNMP agent in h1 and perform SNMP walk in h2\n\n')
    simulateNetwork()
