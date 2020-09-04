import math


def s(x):
    ilt = 6
    now1 = 0

    def guess(a):

        digits = int(math.log10(a)) + 1
        if digits % 2 == 1:
            var1 = 10**((digits-1)/2)
        else:
            var1 = 10**(digits/2)

        return var1

    def go(a, b):
        nonlocal now1, div1, ilt

        if a/b != b:
            div1 = (b+(a/b))/2
            now1 += 1
        else:
            print(now1)
            now1 = ilt

    div1 = guess(x)

    while now1 < ilt:
        go(x, div1)

    print("Bulunan değer: ", div1)
    print("Gerçek cevap: ", math.sqrt(x))
    print("Benzerlik: ", div1/math.sqrt(x)*100)


s(8)
