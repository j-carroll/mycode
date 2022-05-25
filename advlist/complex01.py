#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display list[1] which should show arista_eos
    print(list1[1])

    # create list containing single item
    list2 = ["juniper"]

    # extend list1 by list2
    list1.extend(list2)

    # display extended list1
    print(list1)

    # create list 3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use append to append list 1 by list 3
    list1.append(list3)

    # display complete list 1
    print(list1)

    # display the list of IP addresses
    print(list1[4])

    # print first IP address
    print(list1[4][0])

main()

