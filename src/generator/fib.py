# 生成器应用--斐波拉契数列
def fib(max):
    pre, current, n = 0, 1, 1
    while n <= max:
        yield current
        pre, current = current, pre + current
        n = n + 1


if __name__ == '__main__':
    for value in fib(10):
        print(value)
