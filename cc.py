
#Data Abstraction

def error_handling(file, command):

    if file[-4:] == '.txt' and file[0].islower() == True:

        if command == 'encrypt' or command == 'decrypt':

            message = 'Good File.'

            command_line = 'Good Command.'

        else:

            message = 'Good File.'

            command_line = 'Error: Bad Command.'

    if file[-4:] != '.txt' or file[0].islower() != True:

        if command == 'encrypt' or command == 'decrypt':

            message = 'Error: File did NOT open.'

            command_line = 'Good Command.'

        else:

            message = 'Error: File did NOT open.'

            command_line = 'Error: Bad Command.'

    return message, command_line





def encrypt_or_decrypt(message, command):

    character_list = []

    encoded_char_list = []

    decoded_char_list = []

    opened_file = open(message)

    text = opened_file.read()

    if text.find(' ') < 1:

        for i in text:

            character_list.append(i)

        if command == 'encrypt':

            for character in character_list:

                orig_ASCii_val = ord(character)

                new_ASCii_val = orig_ASCii_val + 3

                new_char = chr(new_ASCii_val)

                encoded_char_list.append(new_char)

            new_message = ''.join(encoded_char_list)

        elif command == 'decrypt':

            for character in character_list:

                orig_ASCii_val = ord(character)

                new_ASCii_val = orig_ASCii_val - 3

                new_char = chr(new_ASCii_val)

                decoded_char_list.append(new_char)

            new_message = ''.join(decoded_char_list)

    else: new_message = text

    return new_message



if __name__ in '__main__':

#Input

    file_name = (input('Please Enter A File Name: '))

    print(file_name)

    file_command = input(f'Please Enter A Command (encrypt or decrypt): ')

    print(file_command)

#Process

    auth_file_name, auth_file_command = (error_handling(file_name, file_command))

#Output

    print(encrypt_or_decrypt(auth_file_name, auth_file_command))

