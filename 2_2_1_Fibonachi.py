def fib(n):
    fib_list = [0, 1]
    for i in range(n+1):
        if i > 1:
            fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()