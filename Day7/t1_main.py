with open('data.txt') as fp:
    raw_data = fp.read()
data = raw_data.replace("\n","")
# print(data)
int_0 = 0
n = len(data)
while True:
    int_1 = data.find('shiny gold',int_0, n)
    k = len('shiny gold')
    if int_1 != -1:
        # print('found it at i = ', int_1)
        #search for '.' in the right side to find where the rule ends
        end = int_1
        while data[end] != '.':
            end += 1
        #search for '.' in the left side to find where the rule starts
        st = int_1
        while data[st] != '.':
            st -= 1
        print("sentence starts at: ", st, " and ends at: ", end)
        print(data[st:end])
    if int_1 == int_0 or int_1 == -1:
        break
    int_0 = int_1 + k
