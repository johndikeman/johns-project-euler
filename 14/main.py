from tqdm import tqdm

largest = (0,0)
with tqdm(total=1000000) as bar:
    for original_ind in range(2,1000001):
        ind = original_ind
        length = 1
        while ind != 1:
            if ind % 2:
                ind = ind * 3 + 1
            else:
                ind /= 2
            length += 1
        if length > largest[0]:
            largest = (length, original_ind)
        bar.update(1)

print largest[1]
