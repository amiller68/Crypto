from frequency import generate_frequency
import string
import itertools
import re

def ngram_freq(ctxt, spacing):
    best_freq = generate_frequency(ctxt, spacing=spacing)
    best_freq = sorted(best_freq.items(), key=lambda item: item[1], reverse=True)
    best_freq = [(i + " : " + str(j)) for (i,j) in best_freq]
    return {
        'Spacing': spacing,
        'table_size': len(best_freq),
        'freq': best_freq
    }


# I am developing a mapping for the ctxts 03, 04, and 12
known = {
    "083": ' ',  # There are lots of 083s
    "969": '.',  # A lot of the time 969 is followed by 083. 969 comes at the end of the ctxt
    "656": 'e',  # Educated guess, this was the most common letter
    # Guesses
    "126": 'l',  # 126126 was the most frequent digram
    "495": 't',  # 495495 had a similar frequency to 'tt' in English
    "981": 's',  # 981981 was a very common digram
    "917": 'a',  # Earlier guessing indicates this is either 917 or 981.
    # At this point I decoded a whole word: 'least'
    "480": 'h',  # I see 't480e' alot
    "654": 'i',  # Suggested guess
    "860": 'w',  # Context
    "421": 'o',  # Context and frequency
    "316": 'r',  # Context and frequency
    "855": 'y',  # Originally thought was 773
    "946": 'n',  # Suggested guess
    "119": 'c',  # Context and frequency
    "058": 'p',  # Context
    "899": 'd',  # Context
    "877": 'g',  # Context
    "038": 'u',  # Context
    "691": 'b',  # Context
    "733": 'm',  # Context
    "386": 'f',  # Context
    "465": 'v',  # Context
    "613": ',',  # Context
    "380": 'k',  # Context
    "407": 'x',  # Context
    "270": 'q',  # Context
    "006": 'j',  # Context
    "984": 'z',  # Context
    "407": 'x'   # Context
}

# Mappings we think cannot occur. Use this to element decryptions that cannot happen
negative_known = {
    "316": 'a'
}


# Include any codes you want to guess
high_freq_codes = [

]

# These are associated with decrypted letters of similar frequency
high_freq_letters = [

]

# Generate all informed guesses
guesses = [list(zip(codes,high_freq_letters)) for codes in itertools.permutations(high_freq_codes,len(high_freq_letters))]
# Filter our guesses of anything we don't think works
guesses = [guess for guess in guesses if all([pair not in guess for pair in negative_known.items()])]

# Code any deal breakers in here, to help automate our cracking
single_letter_words = ["a", "i"]
double_letter_words = ["in", "to", "no", "on", "it", "at", "an", "so", "he", "ha", "ah"]
triple_letter_words = ['the', "she", "his"]


def is_good_guess(text):
    # If there are any nonsense one letter words
    obs_single_letters = re.findall(r'\b(\w)\b', text)
    # print("Single letter words: ", obs_single_letters)
    obs_double_letters = re.findall(r'\b(\w\w)\b', text)
    # print("Single double words: ", obs_double_letters)
    obs_triple_letters = re.findall(r'\b(\w\w\w)\b', text)
    if any([(word not in single_letter_words) for word in obs_single_letters]):
        return False
    if any([(word not in double_letter_words) for word in obs_double_letters]):
        return False
    if any([(word not in    triple_letter_words) for word in obs_triple_letters]):
        return False
    return True


def substitution_break(ctxt, spacing, v):
    freq_ctxt = "".join(ctxt)

    # First, replace everything we know
    for (old, new) in known.items():
        for i in range(0, len(ctxt) - spacing, spacing):
            char_list = []
            for j in range(spacing):
                char_list.append(ctxt[i + j])
            key = "".join(list(char_list))
            if key == old:
                place_holder = new + "\x00\x00"
                ctxt[i:i+spacing] = place_holder
    # Remove any place holders we added
    ctxt = "".join([c for c in ctxt if c != '\x00'])

    best_guesses = []
    freq_dict = generate_frequency(freq_ctxt, spacing)
    remaining_freq_dict = {key: freq_dict[key] for key in freq_dict.keys() if key not in known.keys()}
    analysis = {
        "known": str([(k,v) for k,v in known.items()]),
        "best_guesses": [],
        "remaining_freq": str([(k,v) for k, v in sorted(remaining_freq_dict.items(), key=lambda item: item[1], reverse=True)])
    }

    # Our best guess given the decodings we know
    best_guesses.append({
        "map": str([(k,v) for k,v in known.items()]),
        "best_guess": ctxt
    })

    # If we want to actively decypher the string...

    for guess in guesses:
        ctxt_test = ctxt
        for (old, new) in guess:
            ctxt_test = ctxt_test.replace(old, new)
        print("Guessing that: ", guess)
        if is_good_guess(ctxt_test):
            if v:
                print("Does this look like a good guess?")
                print(ctxt_test)
                answer = input()

                # If the user inputs 'yes'
                if answer == "y":
                    best_guesses.append({
                        "map": str([(k,v) for k,v in known.items()] + guess),
                        "best_guess": ctxt_test
                    })
            else:
                best_guesses.append({
                    "map": str([(k, v) for k, v in known.items()] + guess),
                    "best_guess": ctxt_test
                })
    analysis["best_guesses"] = best_guesses
    return analysis


def ngram_analysis(ctxt, v_opt=False):
    ctxt = [c for c in ctxt if c.isalnum() and c != '']
    analysis = []
    spacings = [2, 3, 5]
    for spacing in spacings:
        if len(ctxt) % spacing:
            continue
        if spacing == 3:
            best_guess = substitution_break(ctxt, spacing, v_opt)
        else:
            best_guess = ngram_freq(ctxt, spacing)
        analysis.append(best_guess)
    return True, analysis
