a = "1"
b = " "
c = "2"
d = " "
e = "3"
print (a, b, c, d, e)

a, b = b, a
print (a, b, c, d, e)

b, d = d, b
print (a, b, c, d, e)

b, c = c, b
print (a, b, c, d, e)

c, e = e, c
print (a, b, c, d, e)

d, e = e, d
print (a, b, c, d, e)

a, c = c, a
print (a, b, c, d, e)

b, c = c, b
print (a, b, c, d, e)