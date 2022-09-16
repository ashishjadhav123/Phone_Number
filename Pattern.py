rows = 6

stop = int(rows / 2 + 1)
itr = 1
for i in range(1, rows + 1):
    if i > stop:
        i = rows - stop + itr
        itr -= 1

    for j in range(1, i - 1):

        print(j, end=' ')

    for j in range(i - 1, 0, -1):

        print(j, end=' ')
    print()

