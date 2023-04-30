import random
import string

characters_list = list(" " + string.punctuation + string.digits + string.ascii_letters)
substitution_key = characters_list.copy()
random.shuffle(substitution_key)

# Encryption
plain_text = input("Enter the message you would like to encrypt:")
cipher_text = "".join(substitution_key)

for letter in plain_text:
    index = characters_list.index(letter)
    cipher_text += substitution_key[index]

print(f"Your encrypted message is: {cipher_text}")

# Decryption 
decrypt_text = input("Enter the message you would like to decrypt:")
find_substitution_key = decrypt_text[0:len(substitution_key)]

plain_text = ""

for letter in decrypt_text[len(substitution_key):len(decrypt_text)]:
    index = find_substitution_key.index(letter)
    plain_text += characters_list[index]

print(f"Your decrypted message is: {plain_text}")