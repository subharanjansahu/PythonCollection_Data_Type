a = {1,3,5}
b = {5,7,9}
c = {7,3,11}
# union() or '|'
print(a.union(b))
print(a|b)

# intersection() or '&'
s = a.intersection(b)
print(s)
print(s&c)

# difference() or '-'
print(a-b)
print(b.difference(a))

# symmetric_difference() or '^'
r = a^b
print(r)
print(r.symmetric_difference(c))

s = set(['a','e','i','o','u','vawels'])
for let in s:
  print(let)

r = {'apple','ball','cat',"pet"}
for itm in r:
  print(itm)

v =set('apple')
for ltr in v:
  print(ltr)

print('l' in v)
print('ap' in v)
print('ape' in v)
print("apple" in v)
print('e' in v)