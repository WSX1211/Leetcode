def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    map_ = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []

    def make_combinations(i, cur):
        if i == len(digits):
            if len(cur) > 0:
                result.append(''.join(cur))
                #result.append(cur)
            return
        for ch in map_[digits[i]]:
            cur.append(ch)  #类似压栈
            print(cur)
            make_combinations(i + 1, cur)
            cur.pop()       #类似出栈

    make_combinations(0, [])

    return result

print(letterCombinations("23"))