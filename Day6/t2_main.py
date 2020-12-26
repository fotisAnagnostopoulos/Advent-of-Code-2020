with open('data.txt') as fp:
    datas = fp.read()
#each testcase is seprated by '\n\n'. Also the last "\n" character is removed, as it will cause problems later
data = datas.strip('\n').split('\n\n')
suma = 0
#initialize a dict, to contain all alphabet
dict_alph = {}
for elem in 'abcdefghijklmnopqrstuvwxyz':
    dict_alph[elem] = 0
for elem in data:
    count = 0
    answers = elem.split('\n')
    # answers = answers[0:-1]
    num_p = len(answers)
    # print(num_p)
    #runs over different peoples answers
    dict_answ = dict_alph.copy()
    for qq in answers:
        #increments each question's count in the dict
        for char in qq:
            dict_answ[char] += 1
        # print(qq)
    #checks which questions are present in all peoples answers and count them
    for val in dict_answ.values():
        if val == num_p:
            count += 1
    # print("suma ", suma)
    # print('No of answers: ', num_p)
    # print("count : ", count)
    # print("The dict : ", dict_answ)
    # print('------------------------------------')
    suma += count 
print(suma)