alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



print('''  ____                                ____  _  _           
 / ___|  __ _  ___  ___  __ _ _ __   |  _ \(_)(_) ___ _ __  
| |     / _` |/ _ \/ __|/ _` | '__|  | |_) | || |/ _ \ '_ \ 
| |___ | (_| |  __/\__ \ (_| | |     |  __/| || |  __/ | | |
 \____| \__,_|\___||___/\__,_|_|     |_|   |_||_|\___|_| |_|
''')




# def encrypt(original_text,shift_amount):
#      cipher_text = ""
#      for letter in original_text:
#           shifted_position = alphabet.index(letter) + shift_amount
#           shifted_position = shifted_position % len(alphabet)
#           cipher_text += alphabet[shifted_position]
#      print(f"Here is the encoded text {cipher_text} ")  
     

# def decrypt(original_text, shift_amount):
#      output_text = ""
#      for letter in original_text:
#           shifted_position = alphabet.index(letter) - shift_amount
#           shifted_position = shifted_position % len(alphabet)
#           cipher_text += alphabet[shifted_position]
#      print(f"Here is the encoded text {output_text} ")  
     


     #mix of both encode and decoder function

def caesar(original_text,shift_amount,encoder_or_decode):
    cipher_text = ""
    for letter in original_text:

        if encoder_or_decode == "decode":
            shift_amount *= -1
        if letter not in alphabet:
            cipher_text += letter
            
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {encoder_or_decode}d text:  {cipher_text} ")  
        

program_over = False
while not program_over:
    direction = input("do you want to encode or decode ?: ")
    text = input("Enter Your Message: ")
    shift = int(input("Enter The Amount Of Shift: "))
    caesar(original_text=text,shift_amount=shift,encoder_or_decode=direction)
    user_ans = input("do you want to encode or decode again?? type 'yes' or 'no'").lower()
    if user_ans == 'no':
        program_over = True
    