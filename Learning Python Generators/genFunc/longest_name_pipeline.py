if __name__ == '__main__':
    full_names = (i.strip() for i in open("names.txt"))
    names_length = ((i, len(i)) for i in full_names)
    max_name = max(names_length, key=lambda x: x[1])
    print(max_name)
