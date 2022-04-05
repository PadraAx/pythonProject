# A Python program to print all
# permutations of given length
from itertools import permutations
a= input("حرف اول: ")
b= input("حرف دوم: ")
c= input("حرف سوم: ")
d= input("حرف چهارم: ")
e= input("حرف پنجم: ")

perm = permutations([a,b,c,d,e], 3)
for i in list(perm):
	print (i)
perm = permutations([a,b,c,d,e], 4)
for i in list(perm):
	print (i)
perm = permutations([a,b,c,d,e], 5)
for i in list(perm):
	print (i)