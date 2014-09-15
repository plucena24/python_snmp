import pygal

DEBUG = False

with open('C:/snmp_data_from_lucena.txt', 'r') as data:
    data_list = data.readlines()

    in_octets = []
    out_octets = []
    in_packets = []
    out_packets = []


    # Stuff all Lists into a single List
    all_packets_list = [in_octets, out_octets, in_packets, out_packets]
    
    # Stuff all match strings into a single List
    all_strings_list = ['ifInOctets_fa0/0', 'ifOutOctets_fa0/0', 'ifInUcastPkts_fa0/0', 'ifOutUcastPkts_fa0/0']



    # Function that simplifies all of the 'if' statements 
    # From previous commit
    
    def valueExtract(packets_list, match_string, data_list):

        for val in data_list:
            if match_string in val:
                packets_list.append(val.split(' ')[1][:-1])



    for i in range(len(all_packets_list)):
        all_packets_list[i] = valueExtract(all_packets_list[i],all_strings_list[i])


    # This is the "old" way - New way above uses a for loop
    # Instead of a for loop with multiple 'if' statements
    
    # for val in data_list:
    #     if 'ifInOctets_fa0/0' in val:
    #         in_octets.append(val.split(' ')[1][:-1])
    #     if 'ifOutOctets_fa0/0' in val:
    #         out_octets.append(val.split(' ')[1][:-1])
    #     if 'ifInUcastPkts_fa0/0' in val:
    #         in_packets.append(val.split(' ')[1][:-1])
    #     if 'ifOutUcastPkts_fa0/0' in val:
    #         out_packets.append(val.split(' ')[1][:-1])

    if DEBUG:
        print '%s %s\n' % ('ifInOctets_fa0/0', in_octets)
        
    
    # Now that the lists have the data, the code
    # Needs to get the Delatas between the values
    
    

    # Option 1 - Calculating deltas using a function

    def delta_calc(my_list):
        delta_list = [my_list[i + 1] - my_list[i] for i in range(len(my_list) - 1)]
        return delta_list

    # Then assigning each list to be the result of the function

    in_octets = delta_calc(in_octets)

    out_octets = delta_calc(out_octets)

    in_packets = delta_calc(in_packets)

    out_packets = delta_calc(out_packets)


    # Option 2 - Stuff the 4 Lists into a List
    # Then call the Function from a for loop
    
    all_packets_list = [in_octets,out_octets,in_packets,out_packets]
    
    for i in range(len(all_packets_list)):
       all_packets_list[i] = delta_calc(all_packets_list[i])
        
    
    # Option 3 - run an individual For loop for each List

    # for i in range(len(in_octets) - 1):
    #     in_octets[i] = int(in_octets[i + 1]) - int(in_octets[i])
    #
    # for i in range(len(out_octets) - 1):
    #     out_octets[i] = int(out_octets[i + 1]) - int(out_octets[i])
    #
    # for i in range(len(in_packets) - 1):
    #     in_packets[i] = int(in_packets[i + 1]) - int(in_packets[i])
    #
    # for i in range(len(out_packets) - 1):
    #     out_packets[i] = int(out_packets[i + 1]) - int(out_packets[i])
    
    
    
    # Use the pop Method to remove the last entry from the list
    # This is the entry at minute 60

    for x in (in_packets, in_octets, out_octets, out_packets):
        x.pop(-1)

if DEBUG:
    print '%s %s\n' % ('ifInOctets_fa0/0', in_octets)
    print '%s %s\n' % ('ifOutOctets_fa0/0', out_octets)
    print '%s %s\n' % ('ifInUcastPkts_fa0/0', in_packets)
    print '%s %s\n' % ('ifOutUcastPkts_fa0/0', out_packets)




# ## Start Pygal Code ###

line_chart = pygal.Line()

line_chart.title = 'Input/Output Packets and Bytes'
line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
line_chart.add('InPackets', in_packets)
line_chart.add('OutPackets', out_packets)
line_chart.add('InBytes', in_octets)
line_chart.add('OutBytes', out_octets)

line_chart.render_to_file('C:/test111.svg')
















