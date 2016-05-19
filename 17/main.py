
vals = {
    0:0,
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:len('thirty'),
    40:len('fourty'),
    50:len('fifty'),
    60:len('sixty'),
    70:len('seventy'),
    80:len('eighty'),
    90:len('ninety'),
    100:len('hundred')
}

count = 0
for a in range(1,1000):
    if len(str(a)) == 1:
        count += vals[int(str(a)[0])]
    elif len(str(a)) == 2:
        # if the number is less that twenty
        if int(str(a)[0]) * 10 < 20:
            count += vals[int(str(a))]
        else:
            count += vals[int(str(a)[0]) * 10] + vals[int(str(a)[1])]
    elif len(str(a)) == 3:
        count += vals[int(str(a)[0])] + vals[100]
        if str(a)[1] != 0 and str(a)[2] != 0:
            # we need to add an and
            count += 3
            if str(a)[1] != 0:
                if int(str(a)[1]) * 10 < 20:
                    count += vals[int(str(a)[1:])]
                else:
                    count += vals[int(str(a)[1]) * 10] + vals[int(str(a)[2])]
            else:
                count += vals[int(str(a)[2])]

count += 11
print count
