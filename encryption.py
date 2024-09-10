import random 
import string

chars = "  " +  string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

text = input("Enter a message to encrypt: ")
encrypt = ""

for letter in text:
    index = chars.index(letter)
    encrypt += key[index] 

print(f'original message: {text}')
print(f"encrypted message: {encrypt}") 

encrypt = input("Enter a message to encrypt: ")
text = ""

for letter in encrypt:
    index = key.index(letter)
    text += chars[index] 

print(f"encrypted message: {encrypt}")
print(f'original message: {text}')
