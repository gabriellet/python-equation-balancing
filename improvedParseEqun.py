from pyparsing import Word, Group, Optional, OneOrMore, ZeroOrMore, Suppress
from string import ascii_uppercase, ascii_lowercase, digits
# from pprint import pprint

# equn = sys.argv[1]
def convertIntegers(tokens):
    return int(tokens[0])

# ele = Word(uppercase, lowercase)
# inte = Word(digits).setParseAction(convertIntegers)
# element = Group(ele + Optional(inte, default=1))
# chemGroup = Group(Suppress('(') + OneOrMore(element) + Suppress(')')
# term =

element = Word(ascii_uppercase, ascii_lowercase)
integer = Word(digits).setParseAction(convertIntegers)
elementRef = Group(element + Optional(integer, default=1))
chemicalFormula = OneOrMore(elementRef)

cForm = Word(ascii_uppercase, ascii_uppercase + ascii_lowercase + digits)
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
dataDict = {}
tempList = []
rhsDict = {}

for f in LHS:
    print(f)
    lhsDict[f] = dict(chemicalFormula.parseString(f).asList())

for f in RHS:
    print(f)
    rhsDict[f] = dict(chemicalFormula.parseString(f).asList())

print(lhsDict)
print(rhsDict)
print
