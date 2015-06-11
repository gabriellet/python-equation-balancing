import re
import sys
from pyparsing import * 

# define some strings to use later, when describing valid lists 
# of characters for chemical symbols and numbers
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"

# equn = sys.argv[1]
equn = "H + O -> H2O"
equn = equn.replace(" ","")
lhs, rhs = equn.split("->",1)
lhs = lhs.split("+")
rhs = rhs.split("+")

# from chemicalFormulas.py

# Define grammar for a chemical formula
# - an element is a Word, beginning with one of the characters in caps,
#   followed by zero or more characters in lowers
# - an integer is a Word composed of digits
# - an elementRef is an element, optionally followed by an integer - if 
#   the integer is omitted, assume the value "1" as a default; these are 
#   enclosed in a Group to make it easier to walk the list of parsed 
#   chemical symbols, each with its associated number of atoms per 
#   molecule
# - a chemicalFormula is just one or more elementRef's
def convertIntegers(tokens):
    return int(tokens[0])
    
element = Word(caps, lowers)
integer = Word(digits).setParseAction(convertIntegers)
elementRef = Group(element("symbol") + Optional(integer, default=1)("qty"))
chemicalFormula = OneOrMore(elementRef)
plusSign = '+'
equnExpr = Group(ZeroOrMore(chemicalFormula+Suppress(plusSign)) +  chemicalFormula)
chemicalEqun = equnExpr.setResultsName('lhs') + "->" + equnExpr.setResultsName('rhs')
test_equn = chemicalEqun.parseString("H + O -> H2O")

from pprint import pprint

print(test_equn)
print(test_equn.keys())
# WHYYYYYY DOESN'T THIS WORKKKKKKKKKKKK!
print("LHS: ")
pprint(test_equn['lhs'])
print("RHS: ")
pprint(test_equn['rhs'])
LHS = test_equn['lhs'].asList()
RHS = test_equn['rhs'].asList()
print(LHS)
print('then')
print(RHS)

print("OLD PARSING RESULTS")

lhs_dict = {}
print("LHS:")
for formula in lhs:
    formulaData = chemicalFormula.parseString(formula)
    
    # print the results
    print(formula, "->", formulaData)
    print("FORMULA", formulaData)
    lhs_dict[formula] = formulaData.asList()

pprint(lhs_dict)


print()

rhs_dict = {}
print("RHS:")
for formula in rhs :
    formulaData = chemicalFormula.parseString(formula)
    
    # print the results
    print( formula, "->", formulaData )
    rhs_dict[formula] = formulaData.asList()

print(rhs_dict)
print

