if __name__ == '__main__':
    d = {}
    l = list()
    for i in range(3):
        d['k'] = i
        l.append(d)
    print(l)
    print(l[0] == l[1])
    print(l[0] is l[1])
    print(l[0] in l[1])