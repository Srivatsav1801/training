def main():
    expr = input("Expression:")
    ans = calc(expr)
    print(ans)


def calc(expr):
    x, y, z = expr.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        ans = x + z
        return ans
    elif y == "-":
        ans = x - z
        return ans
    elif y == "/":
        ans = x / z
        return ans
    elif y == "*":
        ans = x * z
        return ans


if __name__ == '__main__':
    main()
