def calculate_result(num: int) -> list:
    rest = num
    count = 1
    result = []
    while rest > 0:
        if count <= rest:
            result.append(count)
            rest -= count
            count += 1
        else:
            result[-1] += rest
            break
    return list(map(str, result))


def main():
    num = int(input())
    assert 1 <= num <= 1e9
    result = calculate_result(num)
    print(len(result))
    print(' '.join(result))


if __name__ == '__main__':
    main()
