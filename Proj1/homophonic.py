from frequency import generate_frequency
import string

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
suspected = {
    "083": ' ',  # I think in some trigrams
    "969": '.',
    "421": 'o',
    "495": 't',
    "917": 'a',

}


def test_break(ctxt, spacing):
    ctxt = "".join(ctxt)
    for (old, new) in suspected.items():
        ctxt = ctxt.replace(old, new)
    return {
        'best_guess': ctxt,
        'ngram_freq': ngram_freq(ctxt, spacing)
    }


spacings = [2, 3, 5]


def ngram_analysis(ctxt):
    ctxt = [c for c in ctxt if c.isalnum() and c != '']
    analysis = []
    for spacing in spacings:
        if len(ctxt) % spacing:
            continue
        if spacing == 3:
            best_guess = test_break(ctxt, spacing)
        else:
            best_guess = ngram_freq(ctxt, spacing)
        analysis.append(best_guess)
    return True, analysis
