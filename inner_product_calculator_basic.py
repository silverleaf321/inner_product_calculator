def p(x):
    res = 12 * x ** 2 # adjust this
    return res

def t(x):
    res = 2 * x - 1 # adjust this
    return res

t_matrix = [0, 1/2, 1] # adjust this

sol = 0 

for i in t_matrix:
    sol += p(i) * t(i)  # maybe adjust this

print(sol)