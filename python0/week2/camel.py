camelCase = input("camelCase:")
for i in camelCase:
    if i.isupper():
        print("_"+i.lower(),end="")
    else:
        print(i,end="")