def parser(input_txt_file):
    '''
    Takes a .txt file and returns two arrays, the first one containing the rules, and the second
    the password
    '''
    chars = []
    lims = []
    pwords = []
    with open(input_txt_file,'r') as ff:
        for line in ff.readlines():
            bb = line.split(':')
            pword = bb[1].strip(" ").replace("\n",'')
            dd = bb[0].split(" ")
            cc = dd[0].split("-")
            lim = [int(cc[0]),int(cc[1])]
            char = dd[1]
            chars.append(char)
            lims.append(lim)
            pwords.append(pword)
    return chars,lims,pwords

chars, lims, pwords = parser("Data.txt")
count = 0
for i,p in enumerate(pwords):
    char = chars[i]
    lim = lims[i]
    let_count = 0
    for c in p:
        # print(c == char)
        if c == char:
            let_count = let_count + 1
    # print(let_count)
    if lim[0] <= let_count <= lim[1]:
        count = count + 1
print(count)
print(stop)