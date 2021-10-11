import string 
import math 
import collections as col

# Dictionary of frequency of letters in the English language
# Retrieved from http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
letterFrequency = {'e' : 12.02,
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
'z' : 0.07 }

def count_letters(s) :
	filtered = [c for c in s.lower() if c in ascii_letters]
	return col.Counter(filtered)


filename = str(input())



ptxtfile = open(filename)
ptxt_str = ptxtfile.read()

# Alphabet dictionary to count frequency of all letters
num_alpha = dict.fromkeys(string.ascii_lowercase, 0)
 

# Add letters to the alphabet dictionary
for i in ptxt_str:
	if i in num_alpha:
		num_alpha[i] += 1
	
print(num_alpha)
total_count = sum(num_alpha.values())


# Adding percentage frequency of each letter to the dictionary
freq_alpha = dict.fromkeys(string.ascii_lowercase, None)
for i in num_alpha:
	freq_alpha[i] = (num_alpha[i]/total_count)*100
	
sorted_freq = sorted(freq_alpha.items(), key = lambda item: item[1], reverse = True)	

print(sorted_freq)
	

	

