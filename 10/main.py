from tqdm import tqdm
import math

sum = 0

def is_prime(num):
    ind = long(2)
    while ind <= int(math.sqrt(num)):
        if not num % ind:
            return False
        ind += 1
    return True

with tqdm(total = 2000000) as bar:
    for a in range(2000000):
        if is_prime(a):
            # print "%s is prime" % a
            sum += a
        bar.update(1)

print sum - 1
