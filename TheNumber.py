
def gate1(s):
    if s >= 10:
        g1 = 1
        return g1
def gate3(s):
    if ((bn / 1000) == 1 or 7) and ((y / 100) == 1 or 7) and ((o / 10) == 1 or 7) and (b == 1 or 7):
        g3 = 0
        print(bn,y,o,b)
def gate4(s):
    if (bn/1000) + (y/100) + (o/10) + b <= 10:
        g4 = 1
        return g4
def gate5(s):
    if x > 999:
        if (bn/1000)%2 and (y/100)%2 == 1:
            g5 = 1
            return g5
    if x > 99 and x <1000:
        if (y/100) % 2 and (o/10) % 2 == 1:
            g5 = 1
            return g5
    if x > 9 and x < 100:
        if (o/10) % 2 and b % 2 == 1:
            g5 = 1
            return g5
def gate6(s):
    if (o/10) % 2 == 0:
        g6 = 1
        return g6
def gate7(s):
    if b == (bn/1000) + (y/100) + (o/10):
        g7 = 1
        return g7

for x in range(2,1000):
    global g1, g2, g3, g4, g5, g6, g7
    g1, g2, g3, g4, g5, g6, g7 = 0, 0, 0, 0, 0, 0, 0

    global bn, y, o, b
    bn, y, o, b = 0, 0, 0, 0

    b = x % 10
    o = (x % 100) - b
    y = (x % 1000) - o - b
    bn = x - y - o - b


    gate3(x)



"""
Between 1 and 1000, there is only 1 number that meets the following criteria. While 
it could be manually figured out with pen and paper, it would be much more efficient 
to write a program that would do this for you. With that being said, your goal is to find 
out which number meets these criteria. To find out if you have the correct number, click 
the link at the bottom of this main post.

1-The number has two or more digits.

2-The number is prime.

3-The number does NOT contain a 1 or 7 in it.

4-The sum of all of the digits is less than or equal to 10.

5-The first two digits add up to be odd.

6-The second to last digit is even.

7-The last digit is equal to how many digits are in the number.
"""