import codecs
from starter import bitwise_xor

# List of appropriate length decodes to alert us to
# Only include base strings we can expand
good_decodes = {
    3: [
        "the",
        "can",
        "i'm",
        "I'm",
        "sir"
    ],
    4: [
        "east",
        "your",
        "I am",
        "i am"
    ],
    5 : [
        "least",
        "beast",
        "feast"
    ],
    6 : [],
    7 : [],
    8 : []
}


def expand_decodes(good_decodes):
    for (len, guesses) in good_decodes.items():
        for guess in guesses:
            if guess[0] != ' ' and guess[len - 1] != ' ':
                good_decodes[len + 1].append(" " + guess)
                good_decodes[len + 1].append(guess + " ")
                good_decodes[len + 2].append(" " + guess + " ")
    return good_decodes

good_decodes = expand_decodes(good_decodes)

def xor():
    file_1 = "02.txt"  #  str(input())
    file_2 = "13.txt"  #  str(input())

    # Read our ctxts in as hex strings
    bytes_1 = open('ctxts/' + file_1).read().encode()
    bytes_2 = open('ctxts/' + file_2).read().encode()

    xor = bitwise_xor(bytes_1, bytes_2)

    print("text1 XOR text 2: ", xor)
    
    word = str(input()).encode()
    print("word in hex: ", word.decode())

    done = False
    for i in range(len(xor) - len(word)):
        xor_sub = xor[i:i+len(word)]
        res = bitwise_xor(xor_sub, word)
        #print(xor_sub)
        #print(word, "XOR")
        #print("= " + res.decode())
        if res.decode in good_decodes[len(word)]:
            print("Decoding at position ", i)
            print("Decoded: ", res.decode())
    return

    
if __name__ == '__main__':
    xor()