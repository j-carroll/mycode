#!/usr/bin/env python3

import shutil
import os



def main():
    # define path
    os.chdir('/home/student/mycode/')

    # move file
    shutil.move('raynor.obj', 'ceph_storage/')

    # new file name for kerrigan.obj
    xname = input('What is the new name for kerrigan.obj? ')
    
    # rename file to input file name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()


