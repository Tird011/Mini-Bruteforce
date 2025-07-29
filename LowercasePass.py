import itertools
import string
import time

charset = string.ascii_lowercase
target = "skibidi"
start = time.time()
attempts = 0

for attempt in itertools.product(charset, repeat=7):
    guess = ''.join(attempt)
    attempts += 1 
    if guess == target:
     print(f"The Magic Password is: {guess} in {attempts} tries and {time.time()-start:.2f} seconds!")
    break
