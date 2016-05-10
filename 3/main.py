from tqdm import tqdm
import math

def is_prime(num):
    ind = long(2)
    while ind < math.sqrt(num):
        if not num % ind:
            return False
        ind += 1
    return True

largest = 1
big = 600851475143
ind = long(1)

with tqdm(total = int(math.sqrt(big))) as bar:
    while ind < math.sqrt(big):
        if is_prime(ind):
            if not big % ind:
                largest = ind
        ind += 1
        bar.update(1)

print largest
