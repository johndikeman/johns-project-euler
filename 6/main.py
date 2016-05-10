from tqdm import tqdm


with tqdm(total = 200) as bar:
    sum_of_squares = 0
    square_of_sums = 0
    for a in range(1,101):
        sum_of_squares += (a ** 2)
        bar.update(1)

    for a in range(1,101):
        square_of_sums += a
        bar.update(1)

    square_of_sums = square_of_sums ** 2
    print (sum_of_squares - square_of_sums)
