def computepay(h, r):
    if h <= 40 :
        return h * r
    else :
        return r * (1.5 * h - 20)

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Pay Rate:")
r = float(rate)

p = computepay(h, r)

print("Pay", p)