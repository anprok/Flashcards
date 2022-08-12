import ast

tree = ast.parse(code)

call_list = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call):
        call_list.append(node.func.id)

print(call_list)