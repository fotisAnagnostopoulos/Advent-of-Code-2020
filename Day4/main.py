
with open('data.txt') as fp:
    datas = fp.read()
data = datas.strip().split('\n\n')
# print(data)
# print(stop)
c_valids = 0
for registry in data:
    test = registry.replace('\n', ' ')
    test2 = test.split(' ')
    # print(test)
    # print(stop)
    i = 0
    valid = False
    test_dict = {'ecl':0, 'pid':0, 'eyr':0, 'hcl':0, 'byr':0, 'iyr':0, 'hgt':0, 'cid':0}
    while i <(len(test2)):
        keysVals = test2[i].split(":")
        # print(keysVals)
        try:
            test_dict[keysVals[0]] += 1
        except KeyError:
            pass
        i = i + 1
    # print(test_dict)'cid'] == 0
    dict_sum = sum(list(test_dict.values()))
    if  dict_sum == 7 and test_dict['cid'] == 0:
        c_valids += 1
    elif dict_sum == 8:
        c_valids += 1
print(c_valids)