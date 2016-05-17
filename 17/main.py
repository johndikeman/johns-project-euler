nums = "x one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty fourty fifty sixty seventy eighty ninety hundred".split(' ')

for a in range(1,1000):
    hundreds_place = int(a / 100)
    remainder = a - (hundereds_place * 100)
