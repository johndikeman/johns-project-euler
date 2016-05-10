
def find(start):
    while 1:
        start += 1
        result = 1
        for a in range(2,20):
            if start % a != 0:
                result = 0
                break
        if result:
            print start


find(2)
