def type_out_string(s, t):
    list_s = []
    list_t = []

    for i in s:
        if i == '#' and len(list_s) > 0:
            list_s.pop()
        else:
            list_s.append(i)

    for j in t:
        if j == '#' and len(list_t) > 0:
            list_t.pop()
        else:
            list_t.append(j)

    return list_s == list_t

def type_out_string_optimized(s, t):
    for i in range(len(s), len(s[0])):
        s.replace(s[i - 1], "")

    for j in range(len(t), len(t[0])):
        t.replace(t[j - 1], "")

    return s == t


s = "ab#c"
t = "az#c"

