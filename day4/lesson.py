# 1. RANDOM
# import random

# ran_int = random.randint(1, 10)
# ran_float = random.random()
# ran_float_between = random.random() * 5

# coin = random.randint(0, 1)
# print(coin)
# if coin == 0:
#     print('Tails')
# else:
#     print('Head')

# 2. QUEUES
# from collections import deque

# queue = deque(['Eric', 'John', 'Michael'])
# queue.append('Nike')
# queue.append('Jim')
# print(queue) #deque(['Eric', 'John', 'Michael', 'Nike', 'Jim'])
# queue.popleft()
# print(queue) #deque(['John', 'Michael', 'Nike', 'Jim'])

# 3. MAKE NEW LIST
# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
# print(squares)
# print([(x, y) for x in [1, 2, 3] for y in [3, 2, 1] if x != y])

# 4. TUPLES
# t = 12255, 34545, 'Hello'
# t2 = 255, (1,2,3,4,5)
# print(t2)

# 5. SETS
basket = {'apple', 'orange', 'apple', 'pear', 'orange'}
print(basket)

# 6. Dictionaries
tel = {'jack': 12545, 'john': 555222}
tel['anna'] = 55222255
print(tel)