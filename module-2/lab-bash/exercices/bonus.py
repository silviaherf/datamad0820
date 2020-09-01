#!/usr/bin/env python3

import sys
from subprocess import check_output


def bash_command(cmd):
    
    """http://localhost:8890/?token=09bf26f9926818a9527717bf30e5bcc506a7a74d78943817/bonus.py#
   
"""
    return check_output(["/bin/bash","-c",cmd])

 
 
def main(name):
    print(name)
 

if __name__ == "__main__":
    name=input("Dime tu nombre\n")
    main(name)

