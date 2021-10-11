from frequency import generate_frequency

def make_buckets(text, n):
    print("n = " + str(n))
    for l in range(n):
        print("FREQUENCIES BUCKET " + str(l))
        bucket = []
        for x in range(l, len(text), n):
            bucket.append(text[x])
        joined = ''.join(bucket)
        generate_frequency(joined)

def polyalphabetic_freq(text):
    for i in range(1, len(text)):
        print("-----------------BUCKET SIZE: " + str(i) + "------------------------------")
        make_buckets(text, i)

polyalphabetic_freq("abcdefghijklmnop")
