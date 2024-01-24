import random
import string
from typing import List

l= int(input("Enter length For password: "))
combination = string.ascii_letters + string.digits+string.punctuation
password= " ".join(random.choice(combination)for i in range(l))
print("Generated Password :", password)