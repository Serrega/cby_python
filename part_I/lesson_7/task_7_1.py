import string
import random

letters = string.ascii_letters + string.digits
print(letters)

print([random.choice(letters) for _ in range(10)])
print(random.choices(letters, k=10))
print(random.sample(letters, 10))

