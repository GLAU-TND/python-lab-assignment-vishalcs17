arr = (1,2,3,4,66,5,7,)
try:
    arr.remove(5)
except AttributeError as e:
    print(e)

ar = [1,2,3,5,4,6,6,]
try:
    print(len(5))
except TypeError as e:
    print(e)


try:
    x = int(input('Enter a integer number:'))
except ValueError as e:
    print(e)    
