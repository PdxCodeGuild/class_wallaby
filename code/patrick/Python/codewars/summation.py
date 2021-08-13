def summation(num):
    count = 1
    lst_1 = []
    sum = 0
    while count != num+1:
        lst_1.append(count)
        count += 1
    for x in lst_1:
        sum += x
    return sum
print(summation(8))

