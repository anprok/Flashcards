import ast

expression = "(34 + 6) * (23**2 - 7 + 45**2)"

print(len(list(ast.walk(ast.parse(expression)))))