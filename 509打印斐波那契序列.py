# 打印n个斐波那契序列
# 0, 1, 1, 2, 3, 5, 8, 13...


def f(n):
    a,b = 0,1
    if n<1:
        ls = []
        ls.append(a)
        return ls
    else:
        ls=[a,b]
        for n in range(n-2):
            a,b=b,a+b
            print(a,b)
            ls.append(b)
        return ls

print(f(8))
