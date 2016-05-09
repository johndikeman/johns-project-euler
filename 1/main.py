# john dikeman, 5/5/16

fin = 0
for a in range(1000):
    if not a % 5 or not a % 3:
        fin += a

print fin
