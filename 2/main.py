
fin = 0
fib = [1,2]
ind = 1
under = True

while under:
    a = fib[ind] + fib[ind-1]
    if a > 4000000: under = False
    fib.append(a)
    if not a % 2: fin += a
    ind += 1
print fin
