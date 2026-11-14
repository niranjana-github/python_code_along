class ValueTooHighError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value
def value(x):
    if x>100:
        raise ValueTooHighError('value is too high:',x)
    if x<0:
        raise ValueTooSmallError('value is too small:',x)
    else:
        print('Valid Value')

try:
    value(100)
except ValueTooHighError as e:
     print(e.message,e.value)
except ValueTooSmallError as e:
    print(e.message,e.value)
    