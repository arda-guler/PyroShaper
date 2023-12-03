from solver import *

msh = mesh(100, 100)
generate_tubular_grain(msh)
ignite_tubular_grain(msh)
simulate(msh, 1)
