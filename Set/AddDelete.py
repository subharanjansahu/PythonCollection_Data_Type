s = {1,45.9,'set',"list",'mutable'}
print(s)

# add one item to the set
s.add(58,)
print(s)

# Add more than one elements
s.update([45,('e',23)])
print(s)

# remove() remove an element if present in set otherwise give a key error
s.remove('list')
print(s)
# s.remove(23)

# discard() remove an item if item is not present then it don't give any error
s.discard(45)
print(s)
s.discard('dsfas')

# pop() it iterate a random element and return it
print(s.pop())

# clear() remove all elements from a set and give an empty set
s.clear()
print(s)