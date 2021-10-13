from frequency import generate_frequency
import string


def ngram_analysis(ctxt):
    ctxt = [c for c in ctxt if c.isalnum() and c != '']
    if len(ctxt) % 2 == 0:
        best_freq = generate_frequency(ctxt, spacing=2)
        best_guess = {
            'table_size': len(best_freq),
            'freq': best_freq
        }
        return True, best_guess
    if len(ctxt) % 3 == 0:
        best_freq = generate_frequency(ctxt, spacing=3)
        best_guess = {
            'table_size': len(best_freq),
            'freq': best_freq
        }
        return True, best_guess
    best_freq = generate_frequency(ctxt, spacing=2)
    return False, {
               'table_size': len(best_freq),
               'freq': best_freq
           }

