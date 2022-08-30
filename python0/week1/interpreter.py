x,y,z = input("Expression:").split(" ")
x = float(x)
z = float(z)
if y == "+":
    ans = x + z
    print(ans)
elif y == "-":
    ans = x - z
    print(ans)
elif y == "/":
    ans = x / z
    print(ans)
elif y == "*":
    ans = x*z 
    print(ans)
   