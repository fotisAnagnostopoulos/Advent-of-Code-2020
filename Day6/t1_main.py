with open('data.txt') as fp:
    datas = fp.read()
#each testcase is seprated by '\n\n'
data = datas.split('\n\n')
suma = 0
for elem in data:
    quests = set()
    # different lines contain no information...
    answ = elem.replace('\n','').replace(' ','')
    for char in answ:
        #if this question has not answered, it is added to the set
        quests.add(char)
    suma = len(quests) + suma
print(suma)