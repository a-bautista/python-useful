import pyaes

# Key length was invalid, so I changed it
key = 'Sverigearveckartmenkallt'
plaintext = 'Your text goes here'

# key must be bytes, so we convert it
key = key.encode('utf-8')

aes = pyaes.AESModeOfOperationCTR(key)
ciphertext = aes.encrypt(plaintext)

# show the encrypted data
print (ciphertext)

# Write out raw bytes to file
with open('ciphertext.txt', 'wb') as file_out:
    file_out.write(ciphertext)

ciphertext = None
print(ciphertext)

# Read in raw bytes from file
with open('ciphertext.txt', 'rb') as file_in:
    ciphertext = file_in.read()

print(ciphertext)

# DECRYPTION
aes = pyaes.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext
decrypted = aes.decrypt(ciphertext).decode('utf-8')

# True
print (decrypted == plaintext)