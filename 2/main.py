
fin = 0
fib = [1,2]
ind = 1

while under:
    a = fib[ind] + fib[ind-1]
    if a > 4000000: break
    fib.append(a)
    if not a % 2: fin += a
    ind += 1
print fin
