def bad_function(value, seq=[]):
    seq.append(value)
    return seq

if __name__ == '__main__':
    print(bad_function(value=3))
    print(bad_function(value=2))
    print(bad_function(value=1))