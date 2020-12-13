def parser(input_txt_file):
    '''
    Takes a .txt file and returns three arrays, the first one containing the rules, second: [[position_1, position_2],...]
    an the third, the passwords.
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
            chars.append(char.strip(" "))
            lims.append(lim)
            pwords.append(pword)
    return chars,lims,pwords

chars, lims, pwords = parser("Data.txt")
count = 0
for i,p in enumerate(pwords):
    char = chars[i]
    position = lims[i]
    if not(p[position[0]-1] == char and p[position[1]-1] == char) :
        if p[position[0]-1] == char or p[position[1]-1] == char:
            count = count + 1
print(count)