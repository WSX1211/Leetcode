__author__ = "WSX"
#使用栈的思想

left_bracket = ["(","{","["]
right_bracket = [")","}","]"]

def Valid_brackets( str ):
    str_bracket = " ".join(str).split(" ")
    stack = []; j=1; stack.append(str_bracket[0]);  #初始化
    while j < len( str_bracket ):
        if str_bracket[j] in left_bracket or len(stack)==0:
            stack.append(str_bracket[j])    #入栈
            j += 1
        elif str_bracket[j] in right_bracket:
            if left_bracket.index(stack[-1]) == right_bracket.index(str_bracket[j]):
                stack.pop()         #出栈
                j += 1

    if len(stack) == 0:
        return True
    else:
        return False
print(Valid_brackets( "(())" ))