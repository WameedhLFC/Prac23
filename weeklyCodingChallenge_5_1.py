# x = [1, 2, 3, 4, 5, 6]
# x = [-1, -2, -3, -4, -5, -6]
x = [0,0]
y = []
even = 0
odd = 0
for i in x:
    if i%2 == 0:
        even += i
    else:
        odd += i
y = [even,odd]
print (y)