# errors with string values
hrs = input("Enter Hours:")
rate = input("Enter Pay Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
    
print(h, r)
if h <= 40 :
    pay = h * r
else :
    pay = r * (1.5 * h - 20)
print("Pay:",pay)