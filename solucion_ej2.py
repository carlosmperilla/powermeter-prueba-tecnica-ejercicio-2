import json
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

print()
# 1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.
print("1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.")
print("\tSolución primer inciso:")
print("\t"*2, list(set(repetidos)))
print()

# 2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
print("2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’")
print("\tSolución segundo inciso:")
print("\t"*2, list(set(repetidos).intersection(r)))
print()

# 3. Transforme ‘d_str’ en un diccionario.
third_solution_a = eval(d_str)
third_solution_b = json.loads(d_str, encoding="utf-8")
print("3. Transforme ‘d_str’ en un diccionario.")
print("\tCon eval (se debe tener cuidado en la practica, debido a que evalua expresiones, y por tanto las ejecuta.):")
print("\t"*2, third_solution_a, type(third_solution_a))
print("\tCon json.loads (la opción preferible en la practica):")
print("\t"*2, third_solution_b, type(third_solution_b))
