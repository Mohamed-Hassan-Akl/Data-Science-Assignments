# this module called my Math that has 1 function "get_average " to get average of list values,

def get_averg(y):
    sum=0
    for n in y:
        sum += n

    count_num=len(y)
    aver=sum /count_num
    print (f"the average of list: {y} is equal = {aver} ")
    return
