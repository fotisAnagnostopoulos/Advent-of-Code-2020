#loading the data
with open('data.txt') as fp:
    datas = fp.read()
#double newline marks a different entry
data = datas.strip().split('\n\n')
#defining some useful sets to allow quick checks
eye_cols = {'amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
hcl_chars = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
c_valids = 0
for registry in data:
    #one newline its just noise
    test = registry.replace('\n', ' ')
    #space marks separation between fields
    test2 = test.split(' ')
    i = 0
    new_dict = {}
    while i <(len(test2)):
        keysVals = test2[i].split(":")
        try:
            new_dict[keysVals[0]] = keysVals[1]
        except KeyError:
            pass
        i = i + 1
    # checking that all needed fields exist at a registry
    if len(new_dict) == 7 and not('cid' in new_dict.keys()):
        valid = True
    elif len(new_dict.keys()) == 8:
        valid = True
    else:
        valid = False
    #checking further the requirements on the values
    if valid and 1920 <= int(new_dict['byr']) <= 2002 and 2010 <= int(new_dict['iyr']) <= 2020 \
    and 2020 <= int(new_dict['eyr']) <= 2030 and len(new_dict['pid']) == 9 and new_dict['ecl'] in eye_cols:
        if new_dict['hcl'][0] == '#' and len(new_dict['hcl'][1:]) == 6:
            valid = True
            for char in new_dict['hcl'][1:]:
                if not(char in hcl_chars): 
                    valid = False
        else:
            valid = False
        if valid and new_dict['hgt'][-2:] == 'cm':
            if 150 <= int(new_dict['hgt'][0:-2]) <= 193:
                valid = True
            else:
                valid = False
        elif valid and new_dict['hgt'][-2:] == 'in':
            if 58 <= int(new_dict['hgt'][0:-2]) <= 76:
                valid = True
            else:
                valid = False
        else:
            valid = False
    else:
        valid = False
    if valid:
        c_valids = c_valids +  1
print(c_valids)