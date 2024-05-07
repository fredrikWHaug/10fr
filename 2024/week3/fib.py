
def fib(n):
    a, b = 0, 1
    result = []
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result

def main():
    print(fib(10))

if __name__ == '__main__':
    main()