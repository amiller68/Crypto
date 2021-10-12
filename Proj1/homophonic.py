from frequency import generate_frequency

def ngram_analysis(ctxt):
    if ctxt.isdecimal():
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
    return False, ""

