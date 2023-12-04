a = "1"
b = " "
c = "2"
d = " "
e = "3"
print("{} {} {} {} {}".format(a, b, c, d, e))

a, b = b, a
print("{} {} {} {} {}".format(a, b, c, d, e))

b, d = d, b
print("{} {} {} {} {}".format(a, b, c, d, e))

b, c = c, b
print("{} {} {} {} {}".format(a, b, c, d, e))

c, e = e, c
print("{} {} {} {} {}".format(a, b, c, d, e))

d, e = e, d
print("{} {} {} {} {}".format(a, b, c, d, e))

a, c = c, a
print("{} {} {} {} {}".format(a, b, c, d, e))

b, c = c, b
print("{} {} {} {} {}".format(a, b, c, d, e))