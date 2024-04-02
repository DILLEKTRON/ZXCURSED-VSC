import random

values = [1,2,3,4,5,6,7,8]
data = random.choices(values, weights=[2,4,5,6,8,9,10,50], k=8)
print(data)

