

def parser(input_txt_file):
    '''
    Takes a .txt file and returns an array with each elemnt to be that of a line
    '''
    with open(input_txt_file,'r') as ff:
        a = ff.read()
        blacklist = [',','.','?','!','(',')',';','’','"','--','-',' ','\t']
    for item in blacklist:
        a = a.replace(item,'')
    res = a.split("\n")
    return res

data = parser("data.txt")
#brute force - I can not see any possibility for optimization -
for i in range(len(data)):
    for j in range(i+1,len(data)):
        suma = int(data[i]) + int(data[j]) - 2020
        # print(suma)
        if suma == 0:
            print(int(data[i]) * int(data[j]))
            break