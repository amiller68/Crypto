import codecs
from starter import bitwise_xor
import functools

# List of appropriate length decodes to alert us to
# Only include base strings we can expand
good_decodes = {
    # High frequency letters
    1: [
        "e",
        "t",
        "a",
        "o",
        "i"
    ],
    # High frequency digrams
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
        "ro",
        "00"
    ],
    # High frequency trigrams
    3: [
        "too",
        "the",
        "can",
        "i'm",
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
        "men",
        "000"
    ],
    4: [
        "east",
        "your",
        "hell",
        "tion",
        "that",
        "ther",
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
        "0000"
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
        "would",
        "00000"
    ]
}


def expand_decodes(good_decodes):
    for (len, guesses) in good_decodes.items():
        for guess in guesses:
            if guess[0] != ' ' and guess[len - 1] != ' ':
                good_decodes[len + 1].append(" " + guess)
                good_decodes[len + 1].append(guess + " ")
                good_decodes[len + 2].append(" " + guess + " ")
    return good_decodes


# good_decodes = expand_decodes(good_decodes)

# tests against all possible strings that exist inside
def is_good_decode(decoded_string):
    for len in good_decodes.keys():
        for guess in good_decodes[len]:
            if (guess in decoded_string) or (decoded_string in guess):
                return True
    return False


# tests against all possible strings that exist inside
def _is_good_decode(res, xor_sub):
    for guess in good_decodes[len(res)]:
        if guess in res.decode():
            return guess.encode()
    return None


_word_inputs = functools.reduce(lambda a, b: a + b, good_decodes.values())
# Filter duplicates
word_inputs = []
[word_inputs.append(word) for word in _word_inputs if word not in word_inputs]
word_inputs.reverse()


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
        print("Guessing that '" + word_str + "' is in one of the messages")
        # print("Enter 'E' to exit, else press anything")
        # choice = str(input())
        # if choice == "E":
        #     break
        word = word_str.encode()
        blank = bytearray()
        nulls = bytearray()
        ptxt_sub = bytearray()
        for i in range(len(word)):
            blank.extend([95])
            nulls.extend([0])
            ptxt_sub.extend([0])

        for i in range(len(xor) - len(word)):
            xor_sub = xor[i:i+len(word)]
            res_bytes = bitwise_xor(xor_sub, word)
            ptxt_sub[:] = ptxt_acc[i:i + len(word)]

            # Decode for all same length stuff rn
            guess_bytes = _is_good_decode(res_bytes, xor)
            if guess_bytes:
                # Means the cipher text here is 0, and therefore the messages match here!
                if guess_bytes == bytearray(word):
                    ptxt_acc[i:i + len(word)] = nulls
                    guess_acc[i:i + len(word)] = nulls
                    continue
                # If True, also true for guess_acc_sub
                elif ptxt_sub == blank:
                    ptxt_acc[i:i + len(word)] = bytearray(word)
                    guess_acc[i:i + len(word)] = guess_bytes
                else:
                    new_ptxt_acc[:] = ptxt_acc
                    new_guess_acc[:] = guess_acc
                    new_ptxt_acc[i:i + len(word)] = bytearray(word)
                    new_guess_acc[i:i + len(word)] = guess_bytes

                    # Cutting down on redundant intervention
                    if (ptxt_acc == new_guess_acc and guess_acc == new_ptxt_acc) or (ptxt_acc == new_ptxt_acc and guess_acc == new_guess_acc):
                        continue

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
                        if choice == "1":
                            break
                        elif choice == "2":
                            ptxt_acc[:] = new_ptxt_acc
                            guess_acc[:] = new_guess_acc
                            break
                        print("That wasn't a choice!")

    print("Our accumulated guesses:", guess_acc.decode())
    print("Our accumulated plaintext:", ptxt_acc.decode())
    return

    
if __name__ == '__main__':
    xor()