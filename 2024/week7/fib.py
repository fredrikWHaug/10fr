
def fib(n):
    results = []
    a, b = 0, 1
    while a <= n:
        results.append(a)
        a, b = b, a + b
    return results

def main():
    print(fib(10))

if __name__ == '__main__':
    main()