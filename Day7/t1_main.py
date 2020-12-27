with open('data.txt') as fp:
    datas = fp.read()
#each testcase is seprated by '\n. Also the last "\n" character is removed, as it will cause problems later
data = datas.strip('\n').split('\n')
count = 0
bags_set = {'shiny gold'}
test_list = []
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
for rule in data:
    for bag_color in list(bags_set):
        #search for a color that contains "shiny gold" bag, or other bags that contain the latter
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            ind2 = rule.find(" bag")
            #adds the found color to the set of colors containing directly or indirectly "shiny gold" bag
            bags_set.add(rule[0:ind2])
print(bags_set)
# print(stop)

for rule in data:
    for bag_color in list(bags_set):
        ind = rule.find(bag_color)
        # print(rule)
        if ind != -1:
            if bag_color != "shiny gold":
            # print('found ',bag_color, " bag" )
            # print(rule[ind-2])
            # num = int(rule[ind-2])
                count += 1
                break
            elif ind != 0:
                count += 1
                break
            # elif bag_color != "shiny gold":
            #     count += 1
# i = 0
# while i < N:
#     ind = rule.find('shiny gold')


# print(bags_set)
print("Count: ", count)

