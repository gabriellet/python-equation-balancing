import pyparsing as pp
from pyparsing import Word, Group, Optional, OneOrMore, ZeroOrMore, Suppress
from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter

def parse_equn(equation):
    c_form = pp.Word(ascii_uppercase, ascii_uppercase + ascii_lowercase + digits)
    equn_expr = pp.Group(pp.ZeroOrMore(c_form + pp.Suppress('+')) + c_form)
    lhs = equn_expr.setResultsName('lhs')
    rhs = equn_expr.setResultsName('rhs')
    chemical_equn = lhs + "->" + rhs
    parsed_equn = chemical_equn.parseString(equation)

    LHS = parsed_equn['lhs'].asList()
    RHS = parsed_Equn['rhs'].asList()

    lhs_dict = {}
    rhs_dict = {}

    element = pp.Word(ascii_uppercase, ascii_lowercase)
    integer = pp.Word(digits).setParseAction(lambda x: int(x[0]))
    element_ref = pp.Group(element + pp.Optional(integer, default=1))
    chemical_formula = pp.OneOrMore(element_ref)

    for chemical in LHS:
        lhs_dict[chemical] = Counter()
        for element, count in chemical_formula.parseString(chemical):
            lhs_dict[chemical][element] += count

    for chemical in RHS:
        rhs_dict[chemical] = Counter()
        for element, count in chemical_formula.parseString(chemical):
            rhs_dict[chemical][element] += count

    return lhs_dict, rhs_dict
