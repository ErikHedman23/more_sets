def count_vowels(text):
    uppers = 0
    lowers = 0
    total = 0
    upper_lst = ['A', 'E', 'I', 'O', 'U']
    lower_lst = ['a', 'e', 'i', 'o', 'u']
    uniques = set()
    for c in text:
        if c in upper_lst:
            uppers += 1
            uniques.add(c)
        elif c in lower_lst:
            lowers += 1
            uniques.add(c)
    total = uppers + lowers
    return total, uniques