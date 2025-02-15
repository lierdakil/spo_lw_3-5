from parser import *
from lexer import *

input = ''' let a1 = 3 * 4.0;
            func f(a1:int) = a1 * a1;
            let a2 = 4 * 3;
            func f1(a2:float) = a2 + f(1);
            f1(a1) * f(a2);
            a1 + 4;
            a2 + 4 ^ f1(a2);
            f(2);
            func f2(f:(float) -> float) = f(5);
            f2(f1);
            func f3() = 5;
            f3()
            '''

parser = Parser()
trees = parser.parse(lex(input))

variables = {}

print(trees)
for tree in trees:
    if isinstance(tree, Function) or isinstance(tree, Assign):
        variables[tree.Value] = tree.type(variables)
    else:
        print("\n###################################\n")
        print(tree)
        print(tree.type(variables))