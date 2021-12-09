def clean_list(list_to_clean):
    def del_list(list, x):
        dellist = []
        ter = (len(list)-1-x)
        y = x+1
        for i in range(ter):
            if list[x]==list[y] and type(list[x])== type(list[y]):
                dellist.append(y)
            y=y+1
        return dellist
    lent = len(list_to_clean)
    b = []
    x = 0
    for i in range(lent-1):
        b.extend(del_list(list_to_clean, x))
        x = x+1
       
    b = list(set(b))[::-1]
    for i in b:
        del list_to_clean[i]
 
    return list_to_clean;