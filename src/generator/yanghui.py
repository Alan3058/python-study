# 生成器应用--杨辉三角
def yanghui(max):
    # pre:前一行数据，current:当前行数据
    pre, current, n = [1], [1], 1
    while n < max:
        if n >= 2:
            # 第二个元素开始运算
            k = 2
            while k < n:
                current.append(pre[k - 1] + pre[k - 2])
                k = k + 1
            current.append(1)
        yield current
        pre, current, n = current, [1], n + 1


if __name__ == '__main__':
    for value in yanghui(10):
        print(value)
