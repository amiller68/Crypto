import string 
import math 
from scipy.stats import chisquare, fisher_exact
from helpers import *

# Dictionary of frequency of letters in the English language
# Retrieved from http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
letterFrequency = {
	'e' : 12.02,
	't' : 9.10,
	'a' : 8.12,
	'o' : 7.68,
	'i' : 7.31,
	'n' : 6.95,
	's' : 6.28,
	'r' : 6.02,
	'h' : 5.92,
	'd' : 4.32,
	'l' : 3.98,
	'u' : 2.88,
	'c' : 2.71,
	'm' : 2.61,
	'f' : 2.30,
	'y' : 2.11,
	'w' : 2.09,
	'g' : 2.03,
	'p' : 1.82,
	'b' : 1.49,
	'v' : 1.11,
	'k' : 0.69,
	'x' : 0.17,
	'q' : 0.11,
	'j' : 0.10,
	'z' : 0.07
}


def generate_frequency(text, spacing=1):
	# Alphabet dictionary to count frequency of all letters in our text set
	if spacing == 1:
		num_alpha = dict.fromkeys(string.ascii_lowercase, 0.0)
		freq_alpha = dict.fromkeys(string.ascii_lowercase, None)
		text = [c for c in text if c in string.ascii_lowercase and c != '']
	else:
		num_alpha = {}
		freq_alpha = {}
		text = [c for c in text if c.isalnum() and c != '']


	# Add letters to the alphabet dictionary
	for i in range(0, len(text) - spacing, spacing):
		char_list = []
		for j in range(spacing):
			char_list.append(text[i+j])
		key = "".join(list(char_list))
		if key in num_alpha:
			num_alpha[key] += 1.0
		else:
			num_alpha[key] = 1.0

	# print(num_alpha)
	total_count = sum(num_alpha.values())
	if total_count == 0:
		return None

	# Adding percentage frequency of each letter to the dictionary
	for i in num_alpha:
		freq_alpha[i] = (num_alpha[i] / total_count) * 100
	# print(freq_alpha)
	return freq_alpha

# Compare two alphanumeric frequencies and return a tuple:
# 	map
# where match is a boolean describing whether two frequencies are similar enough
# and map is a potential frequency mapping
# Assumes inputted frequencies normalized to add up to 100.0
def _map_frequencies(obs_freq, exp_freq=None):
	if exp_freq is None:
		exp_freq = letterFrequency

	# Sorted tuple lists of expected frequencies, normalized to 100.0
	sorted_exp_freq = sorted(exp_freq.items(), key=lambda item: item[1], reverse=True)
	sorted_obs_freq = sorted(obs_freq.items(), key=lambda item: item[1], reverse=True)

	# Returns chisq, p
	return chisquare(
		[math.log(v + 1.0) for (k, v) in sorted_obs_freq],
		f_exp=[math.log(v + 1.0) for (k, v) in sorted_exp_freq]
	)


# Assumes inputted frequencies normalized to add up to 100.0
def map_frequencies(obs_freq, exp_freq=None):
	if exp_freq is None:
		exp_freq = letterFrequency

	# Sorted tuple lists of expected frequencies, normalized to 100.0
	sorted_exp_freq = sorted(exp_freq.items(), key=lambda item: item[1], reverse=True)
	sorted_obs_freq = sorted(obs_freq.items(), key=lambda item: item[1], reverse=True)

	chisq, p = chisquare(
		[math.log(v + 1.0) for (k, v) in sorted_obs_freq],
		f_exp=[math.log(v + 1.0) for (k, v) in sorted_exp_freq]
	)

	if p > 0.95:
		print("Prime for frequency attack")
		return dict(
			zip([k for (k, v) in sorted_obs_freq], [k for (k, v) in sorted_exp_freq])
		)

	return None



# Make a best guess at the cipher text.
# Add any extra logic we want here!
def replace_letters(text, freq):
	return "".join([freq[i] if i in freq else i for i in text])


# Perform a detailed frequency analysis on a piece of text
# Returns a best guess at the cipher

def frequency_analysis(text, v_opt=False):
	obs_freq = generate_frequency(text)
	if obs_freq is None:
		return None, ""
	map = map_frequencies(obs_freq)  #exp_freq = letterFrequency by default
	if map:
		text = replace_letters(text, map)
	return (map is not None), text


# Run a detailed frequency analysis on a single file
# DON"T type out the dir when using
if __name__ == "__main__":
	filename = 'ctxts/' + '01.txt'# str(input())

	ptxtfile = open(filename)
	ptxt_str = ptxtfile.read()

	if is_hex(ptxt_str):
		print("This seems to have been encoded in hex!")
		ptxt_str = read_hex(ptxt_str)

	print(ptxt_str)
	best_guess = frequency_analysis(ptxt_str)
	print(best_guess)
