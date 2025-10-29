

def myFunction(x, y, z=0):

    result = 0
    if x != 0 and y != 0:
        result = x * y

    print(x,y,z)            # temp tracer

    if result != 0 and z != 0:
        result = result * z

    return result




# pass 10, 4 and return 40
print(myFunction(10,4) )

# pass two number and return muplication of the 2 numbers
print(myFunction(30,2) )

# pass 3 numbers, return multiplication of three numbers
print(myFunction(30,2,5) )

print(myFunction(1,2,3) )
print(myFunction(3,4) )