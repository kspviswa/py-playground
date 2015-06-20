# py-playground
My python playground

## sendGmail.py
A simple gmail command-line client to send mail from your gmail account.

*Note*

However, due to security reasons gmail is enabled with security, that will block progmatic access to your gmail.
So you need to lessen your gmail security here https://www.google.com/settings/security/lesssecureapps where you `turn on` access for less secure apps with `your gmail account`.

Make sure you use the above `gmail account` as your `from gmail address`. Refer the help of `sendGmail.py`

*Usage*

`py-playground$ ./sendGmail.py 
Usage details
sendGmail -f <sender gmail> -p <send gmail pass> -t <receiver mail> -s <subject> -b <body inside quotes>`
***

## snmpTest.py
This program will demonstrate SNMP agent & client communication, within hosts of mininet emulation

*Pre-requisites*

* SNMPd installed [ `apt-get install snmpd`]
* mininet installed [ `apt-get install mininet`]
* python 2.7

*Note*
`mininet` usage requires the `sudo` priviledge

*Usage*

`mininet@mininet-vm:~/pyScripts/py-playground$ ./snmpTest.py`

*Demo*

```
mininet@mininet-vm:~/pyScripts/py-playground$ sudo ./snmpTest.py


*******************************************************************
             MININET - SNMP WALK - DEMO APPLICATION
*******************************************************************

        This script will host a simple network of 2 hosts connected to single switch,
        run SNMP agent in h1 and perform SNMP walk in h2

*** Adding controller
*** Add switches
*** Add host 1
*** Add host 2
*** Add links
*** Starting network
*** Configuring hosts
h1 h2
*** Starting controller
c0
*** Starting 1 switches
s1 ...
*** Starting SNMP agent in h1


 SNMPd started successfuly

*** Performing SNMP walk from h2 to h1

 SNMP walk completed succeessfully
*** Showing first 10 entries of the walked data


iso.3.6.1.2.1.1.1.0 = STRING: "Linux mininet-vm 3.13.0-24-generic #47-Ubuntu SMP Fri May 2 23:31:42 UTC 2014 i686"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (2) 0:00:00.02
iso.3.6.1.2.1.1.4.0 = STRING: "kspviswa@github.com"
iso.3.6.1.2.1.1.5.0 = STRING: "mininet-vm"
iso.3.6.1.2.1.1.6.0 = STRING: "\"mininet-vm\""
iso.3.6.1.2.1.1.8.0 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.10.3.1.1

*** Stopping 1 controllers
c0
*** Stopping 2 links
..
*** Stopping 1 switches
s1
*** Stopping 2 hosts
h1 h2
*** Done
```



