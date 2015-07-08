import re
import sys
from pyparsing import Word, Group, Optional, OneOrMore, ZeroOrMore, Suppress

equn = sys.argv[1]
def convertIntegers(tokens):
    return int(tokens[0])


ele = Word(uppercase, lowercase)
inte = Word(digits).setParseAction(convertIntegers)
element = Group(ele + Optional(inte, default=1))
chemGroup = Group(Suppress('(') + 
term = 


element = Word(uppercase, lowercase)
integer = Word(digits).setParseAction(convertIntegers)
elementRef = Group(element("symbol") + Optional(integer, default=1)("qty"))
chemicalFormula = Group(OneOrMore(elementRef))
plusSign = '+'
equnExpr = Group(ZeroOrMore(chemicalFormula+Suppress(plusSign)) +  chemicalFormula)
chemicalEqun = equnExpr.setResultsName('lhs') + "->" + equnExpr.setResultsName('rhs')
test_equn = chemicalEqun.parseString("H + O -> H2O")

from pprint import pprint

print(test_equn)
print("LHS: ")
LHS = test_equn['lhs'].asList()
print(LHS)
print("RHS: ")
RHS = test_equn['rhs'].asList()
print(RHS)

print

