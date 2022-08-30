while True:
    try:
        n,m = input("Fraction:").split("/")
        f = int(n)/int(m)
        if f<=1:
            break
        if n>m:
            print("ValueError")
    except(ValueError,ZeroDivisionError):
        pass
    
p = f * 100
if p <=1:
    print("E")
elif p>=99:
    print("F")
else:
    print("{:.2f}%".format(p))
    