import random


from string import digits
from string import punctuatuin
from string import ascii_letters



symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols))
                   for i in range(9))
  
  
print(password)
