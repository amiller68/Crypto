
one_letter_words = ['a', 'i']
# A dictionary describing the frequencies
# of characters in the English language
english_freq = {

}

# Construct a frequency analysis on a piece of text
def contruct_frequency(text):
    return {}

# Map an observed frequency to an expected one.
# This method both compares two frequencies by performing chi squared tests on ordered lists of their frequencies
# Returns a tuple:
#   match, map: (bool, {})
def map_frequencies(exp_freq, obs_freq):
    return False, None

# Construct a best guess decoding of a cipher text using a best guess mapping
# Returns a string of our best guess using logic we describe here
def produce_mapping(ctxt, map):
    return ""

# Perform a frequency analysis on a piece of cipher text
# Returns a boolean describing whether a cipher text appears breakable to a frequency analysis attack
# If True, returns a best guess string
def frequency_analysis(ctxt):
    obs_freq = contruct_frequency(ctxt)
    match, map = map_frequencies(english_freq, obs_freq)
    if match:
        ctxt = produce_mapping(ctxt, map)
    return match, ctxt