try:
    a=10/0
    b='10'+12
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('all gud')
finally:
    print('this will run no matter what')