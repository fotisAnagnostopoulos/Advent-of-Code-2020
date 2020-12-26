#loading the data
with open('data.txt') as fp:
    datas = fp.read()
#each testcase is seprated by '\n'
data = datas.split('\n')
# test cases
# data = ['FBFBBFFRLR', "BBFFBBFRLL", "FFFBBBFRRR"]
max_id = 0
for case in data:
    bot = 0
    top = 127
    for char in case[0:7]:
        dumm = (top - bot)//2 +1
        if char == 'F':
            top = top - dumm
        else:
            bot = bot + dumm
    row = min(top,bot)
    # print(row)
    bot = 0
    top = 7
    for char in case[7:]:
        dumm = (top - bot)//2 + 1
        if char == 'L':
            top = top - dumm
        else:
            bot = bot + dumm
    col = max(top,bot)
    temp_id = row * 8 + col
    if temp_id > max_id:
        max_id = temp_id
    # print(row,' ----- ', col)
print(max_id)