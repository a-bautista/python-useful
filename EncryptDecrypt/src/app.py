import pyaes, datetime, os

# The KEY should have 24 characters
KEY = 'Sverigearveckartmenkallt'

def main():

    start = True
    while(start):
        print("Type in the option you want to use:\n")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit\n")
        try:
            option = int(input("Type here your option: "))
            if option == 1:
                print("Encryption option selected\n")
                encrypt()
            elif option == 2:
                print("Decryption option selected\n")
                decrypt()
            elif option == 3:
                start = False
                print("Script finalized!\n")
            else:
                print("Please, try again!")
        except ValueError:
            print("That is not a number, please try again.")


def encrypt():

    # Type in your raw password when prompted
    plaintext = input('Please, type your plain password that you want to encrypt: ')

    # key must be bytes, so we convert it
    key = KEY.encode('utf-8')

    aes = pyaes.AESModeOfOperationCTR(key)
    ciphertext = aes.encrypt(plaintext)

    # show the encrypted data
    print (ciphertext)

    # Write out raw bytes to file
    print("Your password has been encrypted!")
    with open('ciphertext.txt', 'wb') as file_out:
        file_out.write(ciphertext)
    print("Your encrypted password has been written to a .txt file.")

def decrypt():

    # verify if the file exists
    if os.path.exists('ciphertext.txt'):
        # convert the string key to bytes
        key = KEY.encode('utf-8')

        # Read in raw bytes from file
        with open('ciphertext.txt', 'rb') as file_in:
            ciphertext = file_in.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        # decrypted data is always binary, need to decode to plaintext
        decrypted = str(aes.decrypt(ciphertext).decode('utf-8'))

        # read and write normally
        output_file = open('decrypted_' + str(datetime.date.today()) + '.txt', 'w')
        output_file.write(decrypted)
        output_file.close()
        print("Your password has been decrypted and stored in a .txt file. Keep it safe!")
    else:
        print("The file doesn't exist. Please, select option 1 to encrypt your password and then use this option.")

if "__main__" == __name__:
    main()