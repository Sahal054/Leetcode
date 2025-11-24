from collections import Counter

def hashmap(n):
    map= {}
    for i in n:
        if i in map:
            map[i] +=1
        else:
            map[i] = i
    return map        




n =[1,2,3,3,4,3,5,4,3,3,5]
c = hashmap(n)
first_item =list(c.items())[0]
highest_feq_num = first_item[0]
lowest_feq_num = first_item[0]
highest_feq = first_item[1]
lowest_feq = first_item[1]



for num,freq in c.items():
    if  freq > highest_feq:
        highest_feq = freq
        highest_feq_num = num
    if freq < lowest_feq:
        lowest_feq = freq
        lowest_feq_num = num

        

print(c)
print(first_item)
print(highest_feq_num)
print(lowest_feq_num)
           
