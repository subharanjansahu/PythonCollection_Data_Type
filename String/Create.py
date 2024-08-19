s = "hello subha"
print(type(s))
print(s)

# escape sequence
s1 = '''he said, "what's there?"'''
print(s1)

def dif(name,msg="what's up?"):
  print("hey",name,msg)
print(dif('subha','gd mrg'))

def add(a,b):
  return a+b
print("sum =",add(4,6))

def mul():
  a=int(input("Ent 1st no.="))
  b=int(input("Ent 2nd no.="))
  return a*b
res = mul()
print("Product is =",res)