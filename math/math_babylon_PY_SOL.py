
def babylonianRoot(k, a):
    eps = 0.01
    if k <= 0 or (a < 0 and (k%2 == 0)):
        print("Try different inputs!")
        return 0

    xn = -1 if a < 0 else 2

    while True:
        xnhkm1 = 1
        i = 0
        while i < (k - 1):
            xnhkm1 = xnhkm1 * xn
            i = i+1
        xnp1 = ((k - 1) * (xnhkm1 * xn) + a) / (k * xnhkm1)
        diff = xnp1 - xn if xn < xnp1 else xn - xnp1
        xn = xnp1
        if diff > eps:
            break
    return xn
