from random import choice
from sys import argv
from base64 import b64encode
from base64 import b64decode
from math import sqrt

b = 22 # the "magic value" given in the script

# After finding out that the flag is the following result: (The hard part of the challenge is simplifying the code, and figurint what the encryption does)
# for each letter in the plaintext, the value of the corresponding letter in the ciphertext is:
# ciphertext = plaintext_letter + 22
# what we need to do is the following


cipher_base64 = "hnd/goJ/e4h1foWDhYOFiIZ+f3l1e4R5iI+Gin+FhA=="
decoded_base64 = b64decode(cipher_base64)
plaintext = ""

for character in decoded_base64:
	source_character = ord(character) - b
	plaintext += chr(source_character)

print plaintext # This is the flag

print "Flag: KLCTF{"+str(plaintext)+"}"