import sys
def min_max(t):
 print "min_max",min(t),max(t)
n = int(input("enter the number of elements"))
a = [0 for i in range(n)]
for i in range (n):
 a[i] = raw_input()
min_max(a)
if __name__ == "__min_max__":
 min_max(t) 
