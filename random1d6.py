import random

def roll_d6():
    return random.randint(1, 6)

result = roll_d6()
print("주사위를 굴려서 나온 값은:", result)