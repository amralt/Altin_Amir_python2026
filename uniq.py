def get_uniq(s) :
    m = {}
    for i in s:
        m[i] = m.get(i, 0) + 1
    return m

print( get_uniq("ssassssmm")  )