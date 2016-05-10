from tqdm import tqdm

li1 = list(range(999))[::-1]
li2 = list(range(999))[::-1]
pals = []

with tqdm(total = 999) as bar:
    for number_1 in li1:
        for number_2 in li2:
            s = "%d" % (number_1 * number_2)
            if s == s[::-1]:
                pals.append(int(s))
        bar.update(1)

pals.sort()
print pals.pop()
