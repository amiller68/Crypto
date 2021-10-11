import os
import frequency

# A list of tests we can run on cipher texts.
# These test functions should take a cipher text as an argument (as read from the file)
# These tests should return a tuple of type boolean, string
# The boolean should describe whether or not we think a cipher text matches our test for type
# The string should detail our best guess for the decoded string.
# A list of tests you want to run,
# Ordering reflects precedence
# Add tests you want to run here!
testSet = [
    'frequency_analysis'
]

if __name__ == '__main__':
    ctxt_dir = 'ctxts/' #Our dir of ctxts
    analysis_dir = 'analysis/'
    file_list = os.listdir(ctxt_dir)
    file_list.sort()
    for file in file_list:
        ctxt = open(ctxt_dir + file).read()
        print("Performing analysis on " + file)

        analysis_str = ""
        for test in testSet:
            match, best_guess = test(ctxt)
            if match:
                # Construct output/UI here
                # Maybe I can add decision logic for types of analysis that would benefit from human decision making

                analysis_str += "Cipher text breakable by: " + test + "\n"
                analysis_str += "Best guess:\n"
                analysis_str += best_guess

                # For now, lets break at the first successful test
                break

        with open(analysis_dir + file, 'w') as analysis:
            analysis.write(analysis_str)


