"""
from collections import deque

queue = deque(["asd","qwe"])
queue.append("zxc")
queue.append("hjk")
queue.popleft()


words = ['cat', 'window', 'defenestrate']
for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print(words)

# Asal Sayı

for x in range(2, 50):
    for i in range(2, x):
        if x % i == 0:
            #print(x, 'equals', i, '*', x//i)
            break
    else:
        print(x, 'is a prime number')
"""