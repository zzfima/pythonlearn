def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result


# Generator function which returns generator object
def even_integers_generators(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


if __name__ == '__main__':
    print(even_integers_function(11))

    print(even_integers_generators(11))
    for r in even_integers_generators(11):
        print(r)
