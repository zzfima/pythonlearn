def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == '__main__':
    print(factorial(5))  # 5! = 120
