from pyparsing import Word, Group, Optional, OneOrMore, ZeroOrMore, Suppress
from string import ascii_uppercase, ascii_lowercase, digits
from collections import defaultdict, Counter

def parseEqun(equation):
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
    tempDict = defaultdict(int)	# should be Counter
    tempList = []

    element = Word(ascii_uppercase, ascii_lowercase)
    integer = Word(digits).setParseAction(lambda x: int(x[0]))
    elementRef = Group(element + Optional(integer, default=1))
    chemicalFormula = OneOrMore(elementRef)

    for chemical in LHS:
        lhsDict[chemical] = Counter()
        for element, count in chemicalFormula.parseString(chemical):
            lhsDict[chemical][element] += count

    for chemical in RHS:
        rhsDict[chemical] = Counter()
        for element, count in chemicalFormula.parseString(chemical):
            rhsDict[chemical][element] += count

    return lhsDict, rhsDict
