num = int(input())
world_list = []
save = []
count = ["st", "nd", "rd", "th"]

for x in range(num):
    world_list.append(input().split(" "))

def rank_sort(a):
    save_a = a
    save_value = 0
    save_index = []
    output_one_rank = []

    for first_index in range(int(len(a))):
        save_value = int(save_a[0][1])
        
        for second_loop in range(int(len(a))):
            if save_value <= int(a[second_loop][1]):
                save_index = save_a[save_a.index(a[second_loop])]
                save_value = int(a[second_loop][1])

        del save_a[save_a.index(save_index)]
        output_one_rank.append(save_index)
            
    return output_one_rank
    
rank_sort_value = rank_sort(world_list)

def ranking(bu):
    save_b = bu
    temp_save = []
    temp_index_value = []
    
    for frist_loop in range(len(bu)):
        temp_index_value = bu[0]
        
        for second_loop in range(len(save_b)):
            if temp_index_value[1] == save_b[second_loop][1]:
                if temp_index_value[2] == save_b[second_loop][2]:
                    if temp_index_value[3] == save_b[second_loop][3]:
                        if ord(save_b[second_loop][0]) < ord(temp_index_value[second_loop][0]):
                            temp_index_value = save_b[second_loop]

                    elif int(temp_index_value[3]) < int(save_b[second_loop][3]):
                        temp_index_value = save_b[second_loop]

                elif int(temp_index_value[2]) < int(save_b[second_loop][2]):
                    temp_index_value = save_b[second_loop]
            
        del save_b[save_b.index(temp_index_value)]
        temp_save.append(temp_index_value)

    return temp_save

final_rank = ranking(rank_sort_value)

def init(value, count):

    for frist_index in value:
        if value.index(frist_index) <= 3:
            frist_index.insert(0, str(value.index(frist_index) + 1) + count[value.index(frist_index)])

        else:
            frist_index.insert(0, str(value.index(frist_index) + 1) + count[3]) 

    return value

for lop in init(final_rank, count):
    print(" ".join(lop))
