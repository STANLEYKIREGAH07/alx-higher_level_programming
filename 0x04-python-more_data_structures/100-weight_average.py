#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for ttup in my_list:
        num += ttup[0] * ttup[1]
        den += ttup[1]

    return (num / den)
