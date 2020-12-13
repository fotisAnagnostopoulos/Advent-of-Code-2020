def parser(input_txt_file):
    '''
    Takes a .txt file and returns an array
    '''
    data = []
    with open(input_txt_file,'r') as ff:
        data = ff.read().split("\n")
            # data.append(line)
    return data

data = parser("Data.txt")
count = 0
# print(data)
nn = len(data[0])
num = 0
for i in range(len(data[0:-1])):
    num = num + 3
    if num >= nn:
        num = num%nn
    if data[i+1][num] == '#':
        count = count + 1
    # print(num)
print(count)