lista = input().split()
c = 0
lista2 = []
for i in lista:
    if i == "{":
        lista2.append("{")
    elif i == "[":
        lista2.append("[")
    elif i == "(":
        lista2.append("(")
    elif i == "}":
        if lista2[-1] == "{":
            lista2.pop()
        else:
            c += 1
            break
    elif i == "]":
        if lista2[-1] == "[":
            lista2.pop()
        else:
            c += 1
            break
    elif i == ")":
        if lista2[-1] == "(":
            lista2.pop()
        else:
            c += 1
            break
if c == 0 and len(lista2) == 0:
    print("YES")
else:
    print("NO")
    