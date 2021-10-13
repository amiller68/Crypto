import os
import frequency
from parser import parser
import helpers
import homophonic
import json

# A list of tests we can run on cipher texts.
# These test functions should take a cipher text as an argument (as read from the file)
# These tests should return a tuple of type boolean, string
# The boolean should describe whether or not we think a cipher text matches our test for type
# The string should detail our best guess for the decoded string.
# A list of tests you want to run,
# Ordering reflects precedence
# Add tests you want to run here!
testSet = [
    frequency.frequency_analysis,
    homophonic.ngram_analysis
]


# Generate all the general ctxt data we can for a dir of cipher texts
def gen_ctxt_data(ctxt_dir):
    file_list = os.listdir(ctxt_dir)
    file_list.sort()

    if args.g:
        all_ctxt_data = []
    else:
        with open(analysis_dir + "ctxt_data.json", 'r') as f:
            all_ctxt_data = json.load(f)

    all_ctxt_data = []
    for file in file_list:
        ctxt = open(ctxt_dir + file).read()
        ctxt_data = {
            'filename': file,
            'data': {
                'ctxt': ctxt,
                'lc': len([c for c in ctxt.lower() if c.isalnum() and c != ''])
            }
        }

        all_ctxt_data.append(ctxt_data)
    return all_ctxt_data



if __name__ == '__main__':
    args = parser.parse_args()
    #args.v bound to a boolean
    ctxt_dir = 'ctxts/' #Our dir of ctxts
    analysis_dir = 'analysis/' # Where we store our analysis

    all_ctxt_data = []
    if args.g:
        all_ctxt_data = gen_ctxt_data(ctxt_dir)
        with open(analysis_dir + "ctxt_data.json", 'w') as f:
            json.dump(all_ctxt_data, f, indent=4)
    else:
        with open(analysis_dir + "ctxt_data.json", 'r') as f:
            all_ctxt_data = json.load(f)

    comprehensive_analysis = []
    for ctxt_data in all_ctxt_data:
        # Extract anything we need from our meta data
        file = ctxt_data['filename']
        ctxt = ctxt_data['data']['ctxt']

        print("Performing analysis on " + file)
        print("Text len:" + str(len(ctxt)))

        # Frequency analysis

        for test in testSet:
            # We might want to consider returning analysis as a json
            match, best_guess = test(ctxt)

            ctxt_data['data'][test.__name__] = {
                'match': match,
                'best_guess': best_guess
            }
            if match:
                break
        comprehensive_analysis.append(ctxt_data)


        with open(analysis_dir + file.split(".")[0] + '.json', 'w') as analysis:
            json.dump(ctxt_data, analysis, indent=4)

    # save a file containging all our analysis
    with open(analysis_dir + 'comprehensive_analysis.json', 'w') as analysis:
        json.dump(comprehensive_analysis, analysis, indent=4)

