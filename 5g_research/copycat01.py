#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os


def main ():
    # move into the working directory
    os.chdir("/home/student/mycode/")
    
    # move into the working directory
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    # The following line will create the directory if it does not exist already
    shutil.copytree("5g_research/", "5g_research_backup/") 


if __name__ == "__main__":
    main()


