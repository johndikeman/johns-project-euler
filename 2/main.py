
fin = 2
fib = [1,2]
ind = 1

while 1:
    a = fib[ind] + fib[ind-1]
    # print a
    if a > 4000000: break
    fib.append(a)
    if a % 2 == 0: fin += a
    ind += 1
print fin
