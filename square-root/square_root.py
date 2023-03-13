def square_root_helper(number, x):
    return 0.5 * (x + number / x)

def square_root(number):
    x0 = 600_000
    xn = square_root_helper(number, x0)

    while x0 != xn:
        x0 = xn
        xn = square_root_helper(number, x0)
    return xn

print(square_root(2))
