from operator import itemgetter
# import matplotlib.pyplot as plt


def segments_anal(segments: list) -> list:
    i = 0
    points = []

    while i < len(segments):
        point = segments[i][1]
        points.append(point)
        # plt.plot([point, point], [0, len(segments) - 1], linestyle = 'dashed', color='k')
        i += 1
        while i < len(segments) and point >= segments[i][0]:
            i += 1
    return points


def get_input_data() -> list:
    segments = []
    n = int(input())
    assert 1 <= n <= 1000, 'n is not correct'

    for i in range(n):
        segment = list(map(int, input().split()))
        assert 0 <= segment[0] <= segment[1] <= 1e9
        segments.append(segment)
    segments = sorted(segments, key=itemgetter(1))
    return segments


# def get_test_data() -> list:
#   segments = list()
#   with open('data.txt') as text:
#       for line in text:
#           segments.append(list(map(int, line.split())))
#   # segments = sorted(segments, key=itemgetter(0))
#   segments = sorted(segments, key=itemgetter(1))

#   for i in range(len(segments)):
#       plt.plot(segments[i], [i, i], color='g')

#   return segments


def main():

    segments = get_input_data()
    result = segments_anal(segments)
    print(len(result))
    for i in result:
        print(i, end=' ')
    # plt.show()

if __name__ == "__main__":
    main()
