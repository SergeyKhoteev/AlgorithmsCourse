from operator import itemgetter


def items_anal(data: list) -> int:
    backpack_volume = data[0][1]
    del data[0]
    
    # Finding price per 1 weight point
    
    for i in range(len(data)):
        data[i].insert(0, float(data[i][0] / data[i][1]))
    data = sorted(data, key=itemgetter(0), reverse=True)
    # print(f"data {data}")

    # Calculating optimal backpack set

    total_price = float()
    remaining_volume = backpack_volume
    i = 0
    while remaining_volume > 0 and i < len(data):
        if data[i][2] <= remaining_volume:
            total_price += data[i][1]
            remaining_volume -= data[i][2]
        else:
            total_price += float(remaining_volume * data[i][0])
            break
        i += 1
        # print(f'total_price = {total_price}')
        # print(f'remaining_volume = {remaining_volume}')
    return total_price


def get_input_data() -> list:
    data_set = []
    data_set.append(list(map(int, input().split())))
    for i in range(data_set[0][0]):
        data_set.append(list(map(int, input().split())))
    return data_set


# def get_test_data(filename: str) -> list:
#   data_set = []
#   with open(filename) as data:
#       for line in data:
#           data_set.append(list(map(int, line.split())))
#   assert 1 <= data_set[0][0] <= 1e3, 'Wrong amount of items'
#   assert 0 <= data_set[0][1] <= 2e6, 'Wrong volume for backpack'
#   for i in range(1, len(data_set)):
#       for j in data_set[i]:
#           assert 0 <= j <= 2e6, f'Wrong values for {j} in {data_set[i]}'
#   return data_set


def main():
    print(f"{items_anal(get_input_data()):.3f}")
    # print(f"{items_anal(get_test_data('4_1_2_data.txt')):.3f}")
    

if __name__ == "__main__":
    main()

