#!/usr/bin/env python3

# First list of protocols
proto = ["ssh", "http", "https"]
# Second list of protocols
protoa = ["ssh", "http", "https"]

#Print first list
print(proto)
# Append DNS protocol to both lists
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list

#Print first list
print(proto)

# Create third list of ports
proto2 = [ 22, 80, 443, 53 ] # a list of common ports

# Extend first list of protocols with list of ports
proto.extend(proto2) # pass proto2 as an argument to the extend method

# Print first list
print(proto)

# Append third list to second list
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# Lab Challenge
# Use insert method
proto.insert(0, "ftp")
print(proto)

