from frequency import generate_frequency

def ngram_analysis(ctxt):
    if ctxt.isdecimal():
        if len(ctxt) % 2 == 0:
            best_freq = generate_frequency(ctxt, spacing=2)
            return True, best_freq
        if len(ctxt) % 3 == 0:
            best_freq = generate_frequency(ctxt, spacing=3)
            return True, best_freq
    return False, ""

