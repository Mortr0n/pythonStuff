import random

def randInt(min=0, max=100):
    num = random.randrange(min, max+1, 1)
    return num

print(randInt(2,8))
for i in range(100):
    print(randInt())

