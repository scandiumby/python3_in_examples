class ExtendedList(list):

    def extended_append(self, item):
        self.append(item)
        return self


if __name__ == '__main__':
    _list = ExtendedList().extended_append("something")
    print(_list)
