def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result


if __name__ == '__main__':
    print(even_integers_function(11))
