

# figure out number columns
cols = len(lhs) + len(rhs)


# figure out number rows
l = []
for c in lhs:
    l = chain(l, list(lhs[c].keys()))

for c in rhs:
    l = chain(l, list(lhs[c].keys()))

t = set(list(l))
rows = t.len()


