# append()
odd = [1,3,5]
odd.append(7)
print(odd)
# extend()
odd.extend([9,11,13])
print(odd)
# + and * operator
print(odd + [-1,-3,-5])
list = ['a','b']
print(list*2)
# insert()
odd.insert(2,-3)
print(odd)
# reverse()
odd.reverse()
print(odd)
# remove
odd.remove(11)
print(odd)
# del 
del odd[1]
print(odd)
del odd[2:4]
print(odd)
# del odd
# print(odd)

odd1 = odd.copy()
print(odd1)