"""
XOR two texts made of hex code
"""

def xor():
    file_1 = str(input())
    file_2 = str(input())
    
    text_1 = "0x" + open('ctxts/' + file_1).read()
    text_2 = "0x" + open('ctxts/' + file_2).read()
    
    hex_int_1 = int(text_1, 16)
    hex_int_2 = int(text_2, 16)
    
    output = hex_int_1 ^ hex_int_2
    
    print("text1 XOR text 2: ", output)
    
    word = "0x" + str(input()).encode('utf-8').hex()
    print("word in hex: ", word)
    new_word = int(word, 16)
    
    output_2 = new_word ^ output
    
    print("new_word XOR output: ", output_2)
    
    output_2_hex = hex(output_2)
    
    decrypt_word = output_2_hex[-(len(word) - 2):]
    
    word_string = bytes.fromhex(decrypt_word)
    
    ascii_string  = word_string.decode("ASCII")
    
    print("decrypted word: ", ascii_string)
    
if __name__ == '__main__':
    xor()