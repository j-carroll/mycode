#!/usr/bin/env python3

# parse keystone.common.wsgi for return number of failed login attempts
loginfail = 0 # counter for fails

# Open log file
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# create list from file
keystone_file_lines=keystone_file.readlines()

# loop over lines
for line in keystone_file_lines:
    # match fail pattern
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed login attempts is", loginfail)
keystone_file.close()
