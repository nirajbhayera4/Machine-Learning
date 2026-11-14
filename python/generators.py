def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
result=numbers()
print(result)
for num in numbers():
    print(num)
    
    
print("-----------------using next()----------------")
    
#using next()
def nums():
    yield 1
    yield 2
    yield 3
gen=nums()
print(next(gen))
print(next(gen))
print(next(gen))

#using generator expression like list comprehensin
print("-----------------using generator expression like list comprehensin----------------")
gen=(x for x in range(1,6))
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
