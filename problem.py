#####################################################################################
#  Script that ingests data from YAML or JSON variables and renders the configuration
#  with a configuration template. Example
#
#  python configurator.py interface_vars.yaml cisco_intf_template.j2
#####################################################################################
import sys
import os

# use of range() to define a range of values
digits = [1, 2, 3, 4]

# iterate from i = 0 to i = 3
for c in digits:
    if c==2 or c==3:
        continue

    for l in digits:

#        if l==2 or l==4 or l==c:
        if l==2 or l!=4 or l==c:
            continue

        for m in digits:
            if m==c or m==l:
                continue

            for n in digits:
                if n==c or n==l or n==m :
                    continue
                elif n==1 or n==3:
                    continue
                else:
                    print("c=", c)
                    print("l=", l)
                    print("m=", m)
                    print("n=", n)
                    print("-------------------------------")


