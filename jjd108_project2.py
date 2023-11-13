def adjusted_key(text, key):
    key = key.lower()
    adjusted_key = ''

    for char in text:
        if char.isalpha():
            adjusted_key += key[len(adjusted_key) % len(key)]
    return adjusted_key

#new_text = "pittsburgh pa"
#key = "b"
#  ---- part 1

def encrypt_key():
    filename_input=input("Enter filename containing the text to be encrypted (.txt): ")
    names_File=open(filename_input, 'r')

    input_key = input("What is the encoding key to use? ")

    text=names_File.read().lower()
    key=input_key.lower()

    encryption_key = adjusted_key(text, key)
    encrypted_text = ""
    space_counter = 0 #checks for items that are not letters/two words

    for i in range(len(text)):
        character = text[i] #indexing
        if character.isalpha(): #easier for processing
            key_character = encryption_key[i - space_counter % len(encryption_key)] #finds encryption value
            shift = ord(key_character) - 97
            char_code = ord(character) - 97
            if character.islower(): #incase not lowered/makes encrypted_char variable
                encrypted_code = (char_code + shift) % 26
                encrypted_char = chr(encrypted_code + 97)
            encrypted_text += encrypted_char
        else: #checks things other than letters so output is the same character count
            encrypted_text += character
            space_counter += 1
    #print("Encrypted text:", encrypted_text)

    output_filename=input("What is the name of the output file? ")
    file_output=open(output_filename, 'w')
    file_output.write(encrypted_text)
    file_output.close()


def decrypt_key():
    filename=input("Enter file to decrypt (.txt): ")
    decrypt_file=open(filename, 'r')
    text=decrypt_file.read().lower()

    input_key=input("What is the decoding key to use? ")
    key=input_key.lower()

    decrypt_file.close()

    decryption_key=adjusted_key(text, key)
    decrypted_text=""
    space_counter=0

    for i in range(len(text)):
        character=text[i]
        if character.isalpha():
            key_character = decryption_key[i - space_counter % len(decryption_key)]
            shift = ord(key_character) - ord('a')
            char_code = ord(character) - ord('a')
            #finds decrypt value and shift amount

            decrypted_code = (char_code - shift) % 26
            if decrypted_code < 0:
                decrypted_code = 25 - abs(decrypted_code) + 1 #for negative values after subtraction

            decrypted_char = chr(decrypted_code + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += character #ensures that anything other than characters work
            space_counter += 1
    #print("Decrypted text:", decrypted_text)

    output_filename=input("Enter file to output decryption (.txt): ")
    output_file=open(output_filename, 'w')
    output_file.write(decrypted_text)
    output_file.close()

def main():
    decision=None
    while decision != 0:
        print("")
        print("Select Operation: \n 1. to encrypt text \n 2. to decrypt text \n 9. end program")
        decision = int(input("Select Operation: "))

        if decision==1:
            print("")
            print("ENCRYPYTING TEXT")
            encrypt_key()
            print("encrypting done")
        elif decision==2:
            print("")
            print("DECRYPTING TEXT")
            decrypt_key()
            print("decrypting done")
        elif decision==9:
            print("")
            print("quitting program")
            break
        else:
            print("")
            print("Invalid Option. Select 1, 2, or 9")
main()
