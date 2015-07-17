from pyparsing import Word, Group, Optional, OneOrMore, ZeroOrMore, Suppress
from string import ascii_uppercase, ascii_lowercase, digits
from collections import defaultdict

def convertIntegers(tokens):
    return int(tokens[0])

def parseEqun(equation):
    element = Word(ascii_uppercase, ascii_lowercase)
    integer = Word(digits).setParseAction(convertIntegers)
    elementRef = Group(element + Optional(integer, default=1))
    chemicalFormula = OneOrMore(elementRef)

    cForm = Word(ascii_uppercase, ascii_uppercase + ascii_lowercase + digits)
    equnExpr = Group(ZeroOrMore(cForm + Suppress('+')) + cForm)
    lhs = equnExpr.setResultsName('lhs')
    rhs = equnExpr.setResultsName('rhs')
    chemicalEqun = lhs + "->" + rhs
    parsedEqun = chemicalEqun.parseString(equation)

    LHS = parsedEqun['lhs'].asList()
    RHS = parsedEqun['rhs'].asList()

    lhsDict = {}
    rhsDict = {}
    tempDict = defaultdict(int)
    tempList = []

    for f in LHS:
        tempList = chemicalFormula.parseString(f).asList()
        print(tempList)
        for k, v in tempList:
            tempDict[k] += v
            print(tempDict)
        lhsDict[f] = tempDict
        tempDict = defaultdict(int)

    for f in RHS:
        tempList = chemicalFormula.parseString(f).asList()
        print(tempList)
        for k, v in tempList:
            tempDict[k] += v
            print(tempDict)
        rhsDict[f] = tempDict
        tempDict = defaultdict(int)

    return lhsDict, rhsDict
