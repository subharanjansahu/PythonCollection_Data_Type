s = "hello subha"
print(s[-4:-1])
print(s[:])
print(s[3:])
print(s[:-1])
s1=' sahu'
print(s+s1)
print(s1*2)
# in keyword (check whether sub string is present or not)
print('ello' in s)
print('ab' in s)
print('a sa' in s+s1)
print('j' in s+s1)

s2 = "I love python for coding propuse"
for srt in s2:
  print(srt,end='')

count = 0
for ltr in s2:
  if(ltr == 'o'):
    count += 1
print()
print(count)