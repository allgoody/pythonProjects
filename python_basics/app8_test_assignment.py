# calculating pay
# 40 * r + (h - 40) * 1.5 *r == 40 * r + 1.5 * r * h - 1.5 * r * 40 ==
# r * (40 + 1.5 * h - 1.5 * 40) == r * (1.5 * h - 20)
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Pay Rate:")
r = float(rate)
if h <= 40 :
    pay = h * r
else :
    # pay = 40 * r + (h - 40) * 1.5 * r
    pay = r * (1.5 * h - 20)
print("Pay:",pay)