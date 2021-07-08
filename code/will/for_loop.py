# for loop examples

'''
in this for loop we are iterating over the index's 
(the numerical position of an index in a list)
by interating this way, we can extract the index and/or the element from a list
'''
fruits =['apples', 'bananas', 'pears', 'pineapples', 'beets', 'bears', 'battlestar', 'galactica']
for i in range(len(fruits)):
        print(fruits[i], i)
        # print(i)
# expected output
#element      index
'''
apples      0
bananas     1
pears       2
pineapples  3
beets       4
bears       5
battlestar  6
galactica   7
'''
# in the below for loop, we are simply iterating over the elements's in the list and printing
# We do not get the index by doing a for loop this, they are handy when you only care about the element,not the index
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in nums:
    print(num)

#expected output
#indice
'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
'''