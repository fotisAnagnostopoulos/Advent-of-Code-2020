##data loading
with open('data.txt') as fp:
    raw_data = fp.read()
data = raw_data.replace("\n","")
# print(data)

##defining some needed data structures
col_set = {'shiny gold'}
col_list = ['shiny gold']
n = len(data)
int_0 = 0
## j counts the interesting quantity: bags that contain directly or not shiny gold bag
j = 0
##This loop runs on the bags containing the shiny gold bag (col_list), either directly or within other bags.
## Essentially, "jumps" from bag type to bag type
work = True
while j < len(col_list):
    ## the current bag type to be searched
    color = col_list[j]
    int_1 = 0
    ## the start point (index) where the search will performed on the next iteration
    int_0 = 0
    while int_1 != -1:
        ##as long as "find" method finds the considered bag type in data, the above loop runs. 
        int_1 = data.find(color,int_0, n)
        if int_1 != -1 and not((color == 'shiny gold') and data[int_1-1] == '.'):
            # print('found it at i = ', int_1)
            ## search for '.' in both sides to find where the sentence (rule) starts/ends
            end = int_1
            st = int_1
            d_1 = d_2 = True
            while d_1 or d_2:
                if data[end] == '.':
                    d_1 = False
                else:
                    end += 1
                if data[st] == '.':
                    d_2 = False
                else:
                    st -= 1
            ##finds the length of the sentence, containing the found bag type
            k = end - st
            ##search within the considered sentence for string "bags"
            c_end_ind = data.find('bags',st,end)
            ##selects the word (bag type) before "bags"
            col = data[st+1:c_end_ind]
            ##if the found bag type is not within the list and dict, it should be added    
            # print(col)
            if not(col in col_set):
                col_list.append(col)
                col_set.add(col)
            # print(int_0, int_1)
        ## the start point (index) where the search will performed on the next iteration is calculated as
        ## the sum of last found index and the length of the sentence
        int_0 = int_0 + k
    j += 1
print("there are: {} bags containing (directly or within others) the shiny gold bag".format(j))