import string

import pyparsing as pp
import toolz

element = pp.Word(string.ascii_uppercase, string.ascii_lowercase)
number = pp.Optional(pp.Word(string.digits), "1") \
           .setParseAction(lambda x: int(x[0]))

element = (element + number).setParseAction(lambda x: {x[0]: x[1]})

def combine(name, start, tokens):
    end = pp.getTokensEndLoc()
    return {name[start:end]: toolz.merge_with(sum, *tokens)}

chemical = pp.OneOrMore(element).setParseAction(combine)

def combine(tokens):
    def merge(xs):
        ts = tuple(toolz.take(2, xs))
        if len(ts) != 1:
            raise ValueError("Repeated chemical")
        return ts[0]
    return toolz.merge_with(merge, *tokens)

side = pp.delimitedList(chemical, pp.Literal("+")).setParseAction(combine)

equation = side + pp.Suppress("->") + side
equation = pp.LineStart() + equation + pp.LineEnd()

if __name__ == "__main__":
    x = equation.parseString("C6H12O6 + O2 -> CO2 + H2O")
    lhs, rhs = x.asList()
    print(lhs, rhs, sep="\n\n")
