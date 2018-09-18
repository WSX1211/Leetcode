__author__ = "WSX"
def sum_0(list1,list2):  #list1和list2排序好了
    result_list = []
    for m in range(len(list1)):
        for n in range(m + 1, len(list1)):
            if -1 * (list1[m] + list1[n]) in list2:
                result_list.append([list1[m] , list1[n], -1 * (list1[m] + list1[n])])
    return result_list


def three_sum( list_num ):
    result_list = []
    pos_num = []  #正数
    neg_num = []  #负数
    for i in list_num:
        if i < 0:
            neg_num.append(i)
        elif i >0:
            pos_num.append(i)
    neg_num.sort(); pos_num.sort()
    if 0 in list_num:    #处理的含0的情况
        for i in pos_num:
            if -1*i in neg_num:
                result_list.append([-i,0,i])
                 #不含0
    result_list.extend(sum_0(pos_num, neg_num))
    result_list.extend(sum_0(neg_num, pos_num))

    return result_list

list = [-1, 0, 1, 2, -1, -4]
print(three_sum(list))


