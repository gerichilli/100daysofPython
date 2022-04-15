from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

rerun = True

#Define function
def ceasar(input_text, shift_amount, cipher_direction): 
    global rerun  
    output_text = ""
    max_index = len(alphabet) - 1

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in input_text:
        if letter not in alphabet:
            output_text += letter
        else:
        # Shift the index
            new_pos = alphabet.index(letter) + shift_amount
            
            # Get the new index
            if new_pos > max_index:
                new_pos = new_pos - max_index - 1
            elif new_pos < 0:
                new_pos = new_pos + max_index + 1
            
            output_text += alphabet[new_pos]
            
    print(f"The {cipher_direction} text is {output_text}")

while rerun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    ceasar(input_text=text, shift_amount=shift, cipher_direction=direction)
    
    rerun_input = input("Do you want to go again?\n")
    if rerun_input == 'no':
        rerun = False
