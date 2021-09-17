def fib_func(n):
    res = [1, 1]
    for i in range(n - 2):
        length = len(res)
        res.append(res[length - 2] + res[length - 1])
    return res


def fib_generators(n):
    nums = [1, 1]
    for i in range(n):
        if i < 2:
            yield 1
        else:
            res = nums[0] + nums[1]
            yield res
            nums[0] = nums[1]
            nums[1] = res


if __name__ == '__main__':
    print(fib_func(10))
    print(list(fib_generators(10)))
