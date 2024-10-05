#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: rsharma346(117061226)

import subprocess

# Function to return the available free disk space
def free_space():
    # Running the command: df -h | grep '/$' | awk '{print $4}'
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = p.communicate()[0]
    
    # Convert output to string, decode it, and strip newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

