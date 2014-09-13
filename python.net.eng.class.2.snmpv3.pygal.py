import pygal

DEBUG = False

#Open file with snmp_data

with open('C:/snmp_data_from_lucena.txt', 'r') as data:

    data_list = data.readlines()

    in_octets = []
    out_octets = []
    in_packets = []
    out_packets = []
    
    #parse data from file and remove the '\n'
    #at the end. Append value to corresponding list
    
    for val in data_list:
        if 'ifInOctets_fa0/0' in val:
            in_octets.append(val.split(' ')[1][:-1])
        if 'ifOutOctets_fa0/0' in val:
            out_octets.append(val.split(' ')[1][:-1])
        if 'ifInUcastPkts_fa0/0' in val:
            in_packets.append(val.split(' ')[1][:-1])
        if 'ifOutUcastPkts_fa0/0' in val:
            out_packets.append(val.split(' ')[1][:-1])

    if DEBUG:
        print '%s %s\n' % ('ifInOctets_fa0/0',in_octets)

    
    #Subtract value i+1 from i to get 'delta'
    
    for i in range(len(in_octets)-1):
        in_octets[i] = int(in_octets[i+1]) - int(in_octets[i])


    for i in range(len(out_octets)-1):
        out_octets[i] = int(out_octets[i+1]) - int(out_octets[i])


    for i in range(len(in_packets)-1):
        in_packets[i] = int(in_packets[i+1]) - int(in_packets[i])


    for i in range(len(out_packets)-1):
        out_packets[i] = int(out_packets[i+1]) - int(out_packets[i])
        
    
    # Pop the last value from each list
    # This value is the value taken at 60 Min

    for x in (in_packets,in_octets,out_octets,out_packets):
        x.pop(-1)


if DEBUG:
    print '%s %s\n' % ('ifInOctets_fa0/0',in_octets)
    print '%s %s\n' % ('ifOutOctets_fa0/0',out_octets)
    print '%s %s\n' % ('ifInUcastPkts_fa0/0',in_packets)
    print '%s %s\n' % ('ifOutUcastPkts_fa0/0',out_packets)




### Start Pygal Code ###

line_chart = pygal.Line()

line_chart.title = 'Input/Output Packets and Bytes'
line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
line_chart.add('InPackets', in_packets)
line_chart.add('OutPackets', out_packets)
line_chart.add('InBytes', in_octets)
line_chart.add('OutBytes', out_octets)

line_chart.render_to_file('C:/test.svg')

