from tqdm import tqdm

def is_prime(num):
    ind = long(2)
    while ind < num:
        if not num % ind:
            return False
        ind += 1
    return True

largest = 1
big = 600851475143
ind = long(1)

with tqdm(total = big) as bar:
    while ind < big:
        if is_prime(ind):
            if not big % ind:
                largest = ind
        ind += 1
        bar.update(1)

print largest
