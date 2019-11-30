class MyException(Exception):
    def __init__(self,v=''):
        self.v=v
    def __str__(self):
        return str(self)
def Add(a,b):
    if a+b>=150:
        return a+b
    else:
        raise MyException('Custom Error Occured')
re = Add(30,40)
print('Result is',re)
