__author__ = "WSX"

phone_dict = {"2":"abc","3":"def",
            "4":"ghi","5":"jkl",
            "6":"mno","7":"pors",
            "8":"tuv","9":"wxyz",
              }

def phone_number( num_str):
    result = []
    exec_str = """""";result_str = """\tresult.append("""
    num = " ".join(num_str).split(" ") #拆分输入的字符串
    print(num)
    tab = "\t"
    for i in range(len(num)):
        exec_str = exec_str + "for s%d in range(len(phone_dict[num[%s]])):\n" % (i, i)
        for j in range(i+1):
            exec_str = exec_str + tab
    for j in range(len(num)):
        result_str = result_str + "phone_dict[num[%d]][s%d]" %(j,j)
        if len(num) - j > 1:
            result_str = result_str + "+"
        else:
            continue
    str = exec_str + result_str + ")"
    exec(str)
    return result
print(phone_number("23"))
print(phone_number("456"))
