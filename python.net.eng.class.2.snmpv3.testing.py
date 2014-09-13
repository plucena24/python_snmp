import snmp_helper
import time


IP = '192.168.1.254'
a_user = 'admin'
auth_key = 'cisco1234'
encrypt_key = 'cisco1234'

snmp_user = (a_user, auth_key, encrypt_key)

lucena1841 = (IP, 161)

snmp_oids = (
        ('sysName', '1.3.6.1.2.1.1.5.0', None),
        ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
        ('ifDescr_fa0/0', '1.3.6.1.2.1.2.2.1.2.1', None),
        ('ifInOctets_fa0/0', '1.3.6.1.2.1.2.2.1.10.1', True),
        ('ifInUcastPkts_fa0/0', '1.3.6.1.2.1.2.2.1.11.1', True),
        ('ifOutOctets_fa0/0', '1.3.6.1.2.1.2.2.1.16.1', True),
        ('ifOutUcastPkts_fa0/0', '1.3.6.1.2.1.2.2.1.17.1', True),
)

### Start of Logic -> start time value at 0

time_value = 0

### Create file on Local File System 

with open('C:/snmp_data_from_lucena.txt', mode='wb') as data:

### While loop that stops after timer gets to 1 hours

    while time_value <= 3600:

### Write the time to the file

        data.write('%s %s\n' %('time', time_value))

### Loop through the OID values and get them from the router

        for desc, oid, if_counter in snmp_oids:
            snmp_data = snmp_helper.snmp_get_oid_v3(lucena1841,snmp_user,oid)
            output = snmp_helper.snmp_extract(snmp_data)

### Write the values to the file
            data.write('%s %s\n' %(desc, output))

### Sleep for 5 Min, Increment time variable by 300 seconds, Write \n\n to make some space for the next iteration

        time.sleep(300)
        time_value += 300
        data.write('\n\n')
