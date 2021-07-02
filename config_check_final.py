import os
import smtplib
from datetime import datetime
import smtplib
import string
import netmiko
from getpass import getpass

user_name = raw_input("Enter Username: ")
pass_word = getpass()


WR01_ip = raw_input("Enter WR01 ip: ")
WR02_ip = raw_input("Enter WR02 ip: ")
CS01_ip = raw_input("Enter CS01 ip: ")
FS01_ip = raw_input("Enter FS01 ip: ")
#WLC_ip = raw_input("Enter WLC ip: ")

WR01 = {'device_type': 'cisco_ios','ip': WR01_ip ,'username': user_name ,'password': pass_word , 'verbose': True }
WR02 = {'device_type': 'cisco_ios','ip': WR02_ip ,'username': user_name ,'password': pass_word , 'verbose': True }
CS01 = {'device_type': 'cisco_ios','ip': CS01_ip ,'username': user_name ,'password': pass_word , 'verbose': True }
FS01 = {'device_type': 'cisco_ios','ip': FS01_ip ,'username': user_name ,'password': pass_word , 'verbose': True }
#WLC = {'device_type': 'cisco_ios','ip': WLC_ip ,'username': user_name ,'password': pass_word , 'verbose': True }


Routers =[WR01,WR02]

Core_Switch =[CS01]

Floor_Switch =[FS01]

#WLCs =[WLC]


##################################### ROUTERS ############################################################3


for a_device in Routers:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show ip int br | ex unassigned",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Router: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show ip int br | ex unassigned <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Routers:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show ip bgp summary",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Router: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show ip bgp summary <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Routers:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show ip eigrp neighbors",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Router: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show ip eigrp neighbors <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Routers:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("sh int g0/0/2 | i Duplex",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Router: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> sh int g0/0/2 | i Duplex <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


######################################## CORE SWITCH ##################################################


for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show switch",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show switch <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show switch stack-ports",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show switch stack-ports <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show ip eigrp neighbors",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show ip eigrp neighbors <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show inven",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show inventory  <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"




for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show ip int br | ex unassigned",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show ip int br | ex unassigned <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"



for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show etherchannel summary",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show etherchannel summary <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("sh ip route | i 10.140",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> Route to DC01 <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("sh ip route | i 10.141",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> Route to PX DC02 <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("sh ip route | i 10.200",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> Route to SG DC <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("sh ip route | i 10.220",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> DC02 <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Core_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("sh ip cef 4.4.4.4",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> Route to Internet <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
   SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
   net_connect = SSHClass(**a_device)
   output = net_connect.send_command_expect("sh ip route | i 10.181.196",delay_factor=5)
   net_connect.disconnect()
   with open("check.txt", "a") as data: # Create txt file output.txt and send output
       print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
       print>>data, ">>>>>>>>> office VC <<<<<<<<<\n\n"
       print>>data, output
       print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Core_Switch:
   SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
   net_connect = SSHClass(**a_device)
   output = net_connect.send_command_expect("sh ip route | i 10.210.0.0",delay_factor=5)
   net_connect.disconnect()
   with open("check.txt", "a") as data: # Create txt file output.txt and send output
       print>>data, "\n\n>>>>>>>>> Core Switch: {0} <<<<<<<<<".format(a_device['ip'])
       print>>data, ">>>>>>>>> Route to office VC <<<<<<<<<\n\n"
       print>>data, output
       print>>data, ">>>>>>>>> End <<<<<<<<<"



####################################### FLOOR SWITCHES ###################################################


for a_device in Floor_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show switch",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Floor Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show switch <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"

for a_device in Floor_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show switch stack-ports",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Floor Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show switch stack-ports <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


for a_device in Floor_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show stack-power neighbors",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Floor Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show stack-power neighbors <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"



for a_device in Floor_Switch:
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
    net_connect = SSHClass(**a_device)
    output = net_connect.send_command_expect("show etherchannel summary",delay_factor=5)
    net_connect.disconnect()
    with open("check.txt", "a") as data: # Create txt file output.txt and send output
        print>>data, "\n\n>>>>>>>>> Floor Switch: {0} <<<<<<<<<".format(a_device['ip'])
        print>>data, ">>>>>>>>> show etherchannel summary <<<<<<<<<\n\n"
        print>>data, output
        print>>data, ">>>>>>>>> End <<<<<<<<<"


######################################  WLC  ###############################################################

#for a_device in WLCs:
#   SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])
#   net_connect = SSHClass(**a_device)
#   output = net_connect.send_command_expect("show ap summary",delay_factor=5)
#   net_connect.disconnect()
#   with open("check.txt", "a") as data: # Create txt file output.txt and send output
#              print>>data, "\n\n>>>>>>>>> WLC: {0} <<<<<<<<<".format(a_device['ip'])
#              print>>data, output
#              print>>data, ">>>>>>>>> End <<<<<<<<<"






from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate

filePath = r'/home/administrator/pscripts/archive/General/config_check/check.txt'


def sendEmail(TO = "first.lastname@org.com",
              FROM="Notify@PYTHNA.com"):
    HOST = "smtp.org.com"

    msg = MIMEMultipart()
    msg["From"] = FROM
    msg["To"] = TO
    msg["Subject"] = "pscripts/archive/General/config_check/config_check_final.py"
    msg['Date']    = formatdate(localtime=True)

    # attach a file
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(filePath,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
    msg.attach(part)

    server = smtplib.SMTP(HOST)
    # server.login(username, password)  # optional

    try:
        failed = server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception, e:
        errorMsg = "Unable to send email. Error: %s" % str(e)

if __name__ == "__main__":
    sendEmail()


print "Job Done, Email notification sent"

os.remove("check.txt")
print("Generated check.txt Purged!")
