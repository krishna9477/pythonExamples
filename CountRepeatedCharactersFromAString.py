x = input("enter a string:")
dic = {}
for chars in x:
    dic[chars] = x.count(chars)
    for keys, values in dic.items():
        print(keys + " " + str(values))




"""
#  Count Repeated Characters From A Given String.
import collections
str1 = 'theeeLLLLL23567744444'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))
      
"""