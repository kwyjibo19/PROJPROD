import netmiko

#MB Admin VDC .253
#KRW Admin VDC .254

nexus = {

'NUHMB-L6-N7702-WAN01' : '10.18.255.5',
'NUHKRW-L5-N7702-WAN02' : '10.18.255.6',
'NUHMB-L6-N7706-FUSION01' :	'10.18.255.11',
'NUHKRW-L5-N7706-FUSION02'	: '10.18.255.12',
'NUHMB-L6-N7706-DS01' :	'10.18.255.13',
'NUHMB-L4-N7706-DS02' :	'10.18.255.14',
'NUHMB-L6-N7702-3P01' :	'10.18.255.7',
'NUHKRW-L5-N7702-3P02' :	'10.18.255.8'

}

cisco = {

'NUHMB-L6-N7706-CS01' :	'10.18.255.1',
'NUHKRW-L5-N7706-CS02' : '10.18.255.2'

}

fortinet =  {

'FG-01' : '10.18.255.251'

}

device_type1 = 'cisco_nxos'
device_type2 = 'cisco_ios'
device_type3 = 'fortinet'

username = 'admin'
password = 'Logicalis99'
secret = 'Logicalis99'

for hostname, device in nexus.items():
        net_connect = netmiko.ConnectHandler(ip=device, device_type=device_type1,
                username=username, password=password)
        try:
            print(net_connect.find_prompt())
            net_connect.send_command('copy run start')
            print('!!!SAVE SUCCESS!!!')
            log_file = open(str(hostname)+'.txt', "a")
            log_file.write(net_connect.send_command('show run',expect_string=r'#'))
            print('!!!BACKUP SUCCESS!!!')
            print('--------------------')
            net_connect.disconnect()
        except NetMikoTimeoutException:
            print('!!!'+str(hostname)+' FAILED!!!')
            continue

for hostname, device in cisco.items():
        net_connect = netmiko.ConnectHandler(ip=device, device_type=device_type2,
                username=username, password=password)
        try:
            print(net_connect.find_prompt())
            net_connect.send_command('copy run start',expect_string=r'Destination filename')
            net_connect.send_command('\n',expect_string=r'#')
            print('!!!SAVE SUCCESS!!!')
            log_file = open(str(hostname)+'.txt', "a")
            log_file.write(net_connect.send_command('show run',expect_string=r'#'))
            print('!!!BACKUP SUCCESS!!!')
            print('--------------------')
            net_connect.disconnect()
        except NetMikoTimeoutException:
            print('!!!'+str(hostname)+' FAILED!!!')
            continue



for hostname, device in fortinet.items():
        net_connect = netmiko.ConnectHandler(ip=device, device_type=device_type3,
                username=username, password=password)

        try:
            print(net_connect.find_prompt())
            log_file = open(str(hostname)+'.txt', "a")
            log_file.write(net_connect.send_command('show full-configuration'))
            log_file.write("\n")
            print('!!!BACKUP SUCCESS!!!')
            print('--------------------')
            net_connect.disconnect()
        except NetMikoTimeoutException:
            print('!!!'+str(hostname)+' FAILED!!!')
            continue
