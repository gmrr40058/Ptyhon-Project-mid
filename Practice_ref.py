x = 5
try:
    x = x/0
    print(x)
except ZeroDivisionError:
    print('Division not allowed')
