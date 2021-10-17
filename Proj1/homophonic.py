from frequency import generate_frequency
import string
import itertools

def ngram_freq(ctxt, spacing):
    best_freq = generate_frequency(ctxt, spacing=spacing)
    best_freq = sorted(best_freq.items(), key=lambda item: item[1], reverse=True)
    best_freq = [(i + " : " + str(j)) for (i,j) in best_freq]
    return {
        'Spacing': spacing,
        'table_size': len(best_freq),
        'freq': best_freq
    }


# Developing a function that partially encrypts some trigrams
# Our known mappings
known = {
    "083": ' ',  # I think in some trigrams
    "969": '.',
    "656": 'e'
}


# The set of hi freq codes
high_freq_codes = [
    "917",
    "981",
    "495",
    "316",
    "654"
]

high_freq_letters = [
    'a', 'i', 't', 'o',
]

guesses = [list(zip(codes,high_freq_letters)) for codes in itertools.permutations(high_freq_codes,len(high_freq_letters))]

def test_break(ctxt, spacing, v):
    ctxt = "".join(ctxt)
    freq_ctxt = ctxt

    # First, replace everything we know
    for (old, new) in known.items():
        ctxt = ctxt.replace(old, new)

    # Do a quick analysis of what's left
    for (old, new) in known.items():
        freq_ctxt = freq_ctxt.replace(old, '')

    best_guesses = []
    analysis = {
        "known": [(k,v) for k,v in known.items()],
        "best_guesses": [],
        "remaining_freq": generate_frequency(ctxt, spacing)
    }

    best_guesses.append({
        "map": [(k,v) for k,v in known.items()],
        "best_guess": ctxt
    })

    # If we want to actively decypher the string...
    if v:
        for guess in guesses:
            ctxt_test = ctxt
            for (old, new) in guess:
                ctxt_test = ctxt_test.replace(old, new)
            print("Does this look like a good guess?")
            print(ctxt_test)
            answer = input()

            # If the user inputs 'yes'
            if answer == "y":
                best_guesses.append({
                    "map": [(k,v) for k,v in known.items()] + guess,
                    "best_guess": ctxt_test
                })
            #print(analysis)
    analysis["best_guesses"] = best_guesses
    return analysis


spacings = [2, 3, 5]


def ngram_analysis(ctxt, v_opt=False):
    ctxt = [c for c in ctxt if c.isalnum() and c != '']
    analysis = []
    for spacing in spacings:
        if len(ctxt) % spacing:
            continue
        if spacing == 3:
            best_guess = test_break(ctxt, spacing, v_opt)
        else:
            best_guess = ngram_freq(ctxt, spacing)
        analysis.append(best_guess)
    return True, analysis
