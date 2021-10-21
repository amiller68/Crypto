import codecs
from starter import bitwise_xor
import functools

# List of appropriate length decodes to alert us to
# Only include base strings we can expand
good_decodes = {

    # High frequency letters
    # 1: [
    #     "e",
    #     "t",
    #     "a",
    #     "o",
    #     "i"
    # ],
    # # High frequency digrams
    2: [
        "it",
        "in",
        "is",
        "on",
        "to",
        "so",
        "go",
        "ed",
        "th",
        "he",
        "in",
        "en",
        "nt",
        "re",
        "er",
        "an",
        "ti",
        "es",
        "on",
        "at",
        "se",
        "nd",
        "or",
        "ar",
        "al",
        "te",
        "co",
        "de",
        "to",
        "ra",
        "et",
        "ed",
        "it",
        "sa",
        "em",
        "ro"
    ],2: [
        "it",
        "in",
        "is",
        "on",
        "to",
        "so",
        "go",
        "ed",
        "th",
        "he",
        "in",
        "en",
        "nt",
        "re",
        "er",
        "an",
        "ti",
        "es",
        "on",
        "at",
        "se",
        "nd",
        "or",
        "ar",
        "al",
        "te",
        "co",
        "de",
        "to",
        "ra",
        "et",
        "ed",
        "it",
        "sa",
        "em",
        "ro"
    ],

    # High frequency trigrams
    3: [
        "too",
        "the",
        "can",
        "sir",
        "foo",
        "red",
        "the",
        "and",
        "tha",
        "ent",
        "ing",
        "ion",
        "tio",
        "for",
        "nde",
        "has",
        "nce",
        "edt",
        "tis",
        "oft",
        "sth",
        "men"
    ],
    4: [
        "east",
        "your",
        "hell",
        "tion",
        "that",
        "ther",
        "than"
        "with",
        "tion",
        "here",
        "ould",
        "ight",
        "have",
        "hich",
        "whic",
        "this",
        "thin",
        "they",
        "atio",
        "ever",
        "from",
        "ough",
        "were",
        "hing",
        "ment",
        "then"
    ],
    5: [
        "least",
        "beast",
        "feast",
        "hello",
        "ofthe",
        "andth",
        "ction",
        "ation",
        "ndthe",
        "which",
        "inthe",
        "onthe",
        "these",
        "there",
        "edthe",
        "after",
        "ingth",
        "their",
        "eofth",
        "tothe",
        "tiona",
        "about",
        "ngthe",
        "orthe",
        "erthe",
        "other",
        "forth",
        "ional",
        "atthe",
        "ingto",
        "first",
        "tions",
        "theco",
        "would"
    ],
}


# tests against all possible strings that exist inside
def _is_good_decode(res):
    for guess in good_decodes[len(res)]:
        if guess.encode() == res:
            return True


_word_inputs = functools.reduce(lambda a, b: a + b, good_decodes.values())
# Filter duplicates
word_inputs = []
[word_inputs.append(word) for word in _word_inputs if word not in word_inputs]
word_inputs.reverse()
w = bytearray(0)

word_inputs = [
    "there",
    "than",
    "then",
    "the",
    "help",
    "it",
    "to"
]

def print_guess(bytes, i, l):
    r = bytearray()
    for x in range(len(bytes)):
        b = bytes[x]
        if i == x:
            r.extend([91])
        if (i + l) == x:
            r.extend([93])
        r.extend([b])
    print(r.decode())
    return


def xor():
    file_1 = "02.txt"  #  str(input())
    file_2 = "13.txt"  #  str(input())

    # Read our ctxts in as hex strings
    bytes_1 = open('ctxts/' + file_1).read().encode()
    bytes_2 = open('ctxts/' + file_2).read().encode()

    xor = bitwise_xor(bytes_1, bytes_2)

    print("Lets start decoding!")

    # These accumalate portions of guesses and corresponding plaintext
    ptxt_acc = bytearray()
    guess_acc = bytearray()
    new_ptxt_acc = bytearray()
    new_guess_acc = bytearray()
    for i in range(len(xor)):
        ptxt_acc.extend([95]) # These are underscores
        guess_acc.extend([95]) # These are underscores
        new_ptxt_acc.extend([95])  # These are underscores
        new_guess_acc.extend([95])  # These are underscores

    for word_str in word_inputs:
       #  print("Guessing that '" + word_str + "' is in one of the messages")
        word = word_str.encode()

        # Init some byte arrays
        blank = bytearray()
        nulls = bytearray()
        ptxt_sub = bytearray()
        for i in range(len(word)):
            blank.extend([95])
            nulls.extend([48])
            ptxt_sub.extend([0])

        print("Blank: ", blank, " | Nulls: ", nulls)

        for i in range(len(xor) - len(word)):
            xor_sub = xor[i:i+len(word)]
            guess = bitwise_xor(xor_sub, word)
            ptxt_sub[:] = ptxt_acc[i:i + len(word)]

            # Decode for all same length stuff rn
            if _is_good_decode(guess):
                # Means the cipher text here is 0, and therefore the messages match here!
                if guess == word:
                    ptxt_acc[i:i + len(word)] = nulls
                    guess_acc[i:i + len(word)] = nulls
                    continue
                # If True, also true for guess_acc_sub
                elif ptxt_sub == blank or ptxt_sub.decode().strip('_').encode() in guess:
                    ptxt_acc[i:i + len(word)] = word
                    guess_acc[i:i + len(word)] = guess
                elif (b'0' in ptxt_sub) or (ptxt_acc == new_guess_acc and guess_acc == new_ptxt_acc):
                    continue
                else:
                    new_ptxt_acc[:] = ptxt_acc
                    new_guess_acc[:] = guess_acc
                    new_ptxt_acc[i:i + len(word)] = word
                    new_guess_acc[i:i + len(word)] = guess

                    print("Which set of texts looks more correct? (1/2)")
                    print("1.")
                    print("Ptxt Acc: ")
                    print_guess(ptxt_acc, i, len(word))
                    print("Guess Acc: ")
                    print_guess(guess_acc, i, len(word))


                    print("2.")
                    print("New Ptxt Acc: ")
                    print_guess(new_ptxt_acc, i, len(word))
                    print("New Guess Acc: ")
                    print_guess(new_guess_acc, i, len(word))

                    while True:
                        choice = str(input())
                        # choice = "1"
                        if choice == "1":
                            break
                        elif choice == "2" or choice == "":
                            ptxt_acc[:] = new_ptxt_acc
                            guess_acc[:] = new_guess_acc
                            break
                        print("That wasn't a choice!")

    print("Our accumulated guesses:", guess_acc.decode())
    print("Our accumulated plaintext:", ptxt_acc.decode())
    return

def _xor():
    file_1 = "02.txt"  #  str(input())
    file_2 = "13.txt"  #  str(input())

    # Read our ctxts in as hex strings
    bytes_1 = open('ctxts/' + file_1).read().encode()
    bytes_2 = open('ctxts/' + file_2).read().encode()

    xor = bitwise_xor(bytes_1, bytes_2)

    print("Lets start decoding!")

    # These accumalate portions of guesses and corresponding plaintext
    ptxt_acc = bytearray()
    guess_acc = bytearray()
    new_ptxt_acc = bytearray()
    new_guess_acc = bytearray()
    for i in range(len(xor)):
        ptxt_acc.extend([95]) # These are underscores
        guess_acc.extend([95]) # These are underscores
        new_ptxt_acc.extend([95])  # These are underscores
        new_guess_acc.extend([95])  # These are underscores

    for word_str in word_inputs:
        print("Guessing that '" + word_str + "' is in one of the messages")
        word = word_str.encode()

        # Init some byte arrays
        blank = bytearray()
        nulls = bytearray()
        ptxt_sub = bytearray()
        for i in range(len(word)):
            blank.extend([95])
            nulls.extend([48])
            ptxt_sub.extend([0])

        print("Blank: ", blank, " | Nulls: ", nulls)

        for i in range(len(xor) - len(word)):
            xor_sub = xor[i:i+len(word)]
            guess = bitwise_xor(xor_sub, word)
            ptxt_sub[:] = ptxt_acc[i:i + len(word)]

            x = i
            for (w, g) in zip(word, guess):
                if w == g:
                    ptxt_acc[x:x+1] = bytearray(b'0')
                    continue
                x += 1
            # Decode for all same length stuff rn
            if _is_good_decode(guess):
                # Means the cipher text here is 0, and therefore the messages match here!
                if guess == word:
                    ptxt_acc[i:i + len(word)] = nulls
                    guess_acc[i:i + len(word)] = nulls
                    continue
                # If True, also true for guess_acc_sub
                elif ptxt_sub == blank or ptxt_sub.decode().strip('_').encode() in guess:
                    ptxt_acc[i:i + len(word)] = word
                    guess_acc[i:i + len(word)] = guess
                elif (b'0' in ptxt_sub) or (ptxt_acc == new_guess_acc and guess_acc == new_ptxt_acc):
                    continue
                else:
                    new_ptxt_acc[:] = ptxt_acc
                    new_guess_acc[:] = guess_acc
                    new_ptxt_acc[i:i + len(word)] = word
                    new_guess_acc[i:i + len(word)] = guess

                    # print("Which set of texts looks more correct? (1/2)")
                    # print("1.")
                    # print("Ptxt Acc: ")
                    # print_guess(ptxt_acc, i, len(word))
                    # print("Guess Acc: ")
                    # print_guess(guess_acc, i, len(word))
                    #
                    #
                    # print("2.")
                    # print("New Ptxt Acc: ")
                    # print_guess(new_ptxt_acc, i, len(word))
                    # print("New Guess Acc: ")
                    # print_guess(new_guess_acc, i, len(word))

                    while True:
                        # choice = str(input())
                        choice = "1"
                        if choice == "1":
                            break
                        elif choice == "2" or choice == "":
                            ptxt_acc[:] = new_ptxt_acc
                            guess_acc[:] = new_guess_acc
                            break
                        print("That wasn't a choice!")

    print("Our accumulated guesses:", guess_acc.decode())
    print("Our accumulated plaintext:", ptxt_acc.decode())
    return

    
if __name__ == '__main__':
    xor()