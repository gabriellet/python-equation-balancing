from pyparsing import Word, Group, Optional, OneOrMore, ZeroOrMore, Suppress
from string import ascii_uppercase, ascii_lowercase, digits
from pprint import pprint

# equn = sys.argv[1]
def convertIntegers(tokens):
    return int(tokens[0])

# ele = Word(uppercase, lowercase)
# inte = Word(digits).setParseAction(convertIntegers)
# element = Group(ele + Optional(inte, default=1))
# chemGroup = Group(Suppress('(') +
# term =

element = Word(ascii_uppercase, ascii_lowercase)
integer = Word(digits).setParseAction(convertIntegers)
elementRef = Group(element + Optional(integer, default=1))
# chemicalFormula = Group(OneOrMore(elementRef))

cForm = Word(ascii_uppercase, ascii_uppercase+ascii_lowercase+digits)
equnExpr = Group(ZeroOrMore(cForm + Suppress('+')) + cForm)
lhs = equnExpr.setResultsName('lhs')
rhs = equnExpr.setResultsName('rhs')
chemicalEqun = lhs + "->" + rhs
testEqun = chemicalEqun.parseString("H2 + O2 -> H2O")

print(testEqun)
print("LHS: ")
LHS = testEqun['lhs'].asList()
print(LHS)
print("RHS: ")
RHS = testEqun['rhs'].asList()
print(RHS)

print

lhsDict = {}
temp = ()
tempList = []
rhsDict = {}

for f in LHS:
    print(f)
    data = elementRef.parseString(f).asList()
    print(data)
    for d in data:
        temp = tuple(data)
        print(temp)
        tempList.append(temp)
    lhsDict[f] = tempList
    temp = ()
    tempList = []
    
for f in RHS:
    print(f)
    data = elementRef.parseString(f).asList()
    for d in data:
        temp = tuple(data)
        print(temp)
        tempList.append(temp)
    rhsDict[f] = tempList
    temp = ()
    tempList = []

print(lhsDict)
print(rhsDict)
print
