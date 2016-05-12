from tqdm import tqdm

def find_nth_triangle_number(num):
    sum = 0
    for a in range(1,num + 1):
        sum += a
    return sum

def get_number_of_factors(num):
    sum = 0
    for a in range(1,num+1):
        if not num % a:
            sum += 1
    return sum


progress = 0
ind = 1
largest = 0
num = 0

with tqdm(total = 500) as bar:
    while 1:
        progress += ind
        num = get_number_of_factors(progress)
        if num > largest:
            diff = num - largest
            largest = num
            bar.update(diff)
        if num > 500:
            print progress
            break
        ind += 1
