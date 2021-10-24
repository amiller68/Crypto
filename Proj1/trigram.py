"""
Find and replace all the trigrams we can
"""

def search_replace(list_ctxts, known_tri):
    big_str = ""
    for i in list_ctxts:
        file = i
        
        ctxt = open('ctxts/' + file).read()
        
        big_str += '\n' + i + '\n\n' + ctxt
    
    for i in range(0, len(big_str)-1, 3):
        if big_str[i:i+3] in known_tri.values():
            big_str.replace(big_str[i:i+3], )
    
    for i in known_tri:
        for j in known_tri[i]:
            big_str = big_str.replace(str(j), i)
            
    f = open("testfile.txt", "w")
    f.write(big_str)
    f.close()        
    
    while True:
        tri = str(input())
        letter = str(input())
        
        if letter in known_tri:
            known_tri[letter].append(tri)
        else:
            known_tri[letter] = [tri]
        
        if letter == "\\n":
            big_str = big_str.replace(tri, '\n')
        else:
            big_str = big_str.replace(tri, letter)
        
        print(known_tri)
        
        f = open("testfile.txt", "w")
        f.write(big_str)
        f.close()
        
if __name__ == '__main__':
    search_replace(['07.txt', '08.txt', '19.txt', '20.txt'],  
                   {'\n': ['546'], 'e': ['402', '487', '773', '174', '659', '147'], 'm': ['262'], ':': ['949'], 'w': ['990', '810'], 'l': ['041'], 'i': ['782', '397', '036', '853', '569', '215'], 'd': ['835', '013', '370'], 'n': ['043', '730'], 't': ['304', '192', '715', '045', '060'], 'g': ['563'], 'h': ['211', '700', '640'], 'a': ['061', '513', '954', '298', '234'], 'j': ['523'], 'o': ['182'], 'b': ['750'], 'r': ['208', '756', '683'], 's': ['596', '396'], 'v': ['917'], 'p': ['722', 
'555'], 'f': ['882'], '.': ['627'], ' ': ['243', '011', '559', '668', '148', '280', '021', '598', '237', '797', '308', '639', '425']}

)