import re
import sys
equn = sys.argv[1]
equn = equn.replace(" ","")
lhs, rhs = equn.split("->",1)
lhs = lhs.split("+")
rhs = rhs.split("+")
lhs_ele = []
rhs_ele = []
for e in lhs:
    lhs_ele.extend( re.findall('[A-Z][^A-Z]*', e) )
for e in rhs:
    rhs_ele.extend( re.findall('[A-Z][^A-Z]*', e) )
lhs = []
rhs = []
for e in lhs_ele:
    temp = re.split('(\d+)',e)
    if len(temp) > 1:
        del temp[-1]
    elif len(temp) == 1:
        temp.extend("1")
    lhs.append( temp )
for e in rhs_ele: 
    temp = re.split('(\d+)',e)
    if len(temp) > 1:
        del temp[-1]
    elif len(temp) == 1:
        temp.extend("1")
    rhs.append( temp )
    # rhs.append( re.split('(\d+)',e) )
print("LHS: \n", lhs)
print("RHS: \n", rhs)
