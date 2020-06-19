# bounce.py
#
# Exercise 1.5

BOUNCE_UP_FACTOR = 3/5
BOUNCE_TIMES = 10
INITIAL_HEIGHT = 100

bounce_i = 1
curr_height = INITIAL_HEIGHT
while bounce_i <= BOUNCE_TIMES:
    new_height = round(curr_height * BOUNCE_UP_FACTOR, 4)
    print(bounce_i, new_height)
    curr_height = new_height
    bounce_i += 1



