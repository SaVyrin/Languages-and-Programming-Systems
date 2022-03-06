def make_list_without_duplicates(original_list: list):
    if len(original_list) == 0:
        return original_list

    result_list = []
    prev_number = original_list[0]
    result_list.append(prev_number)
    for number in original_list[1:]:
        if number != prev_number:
            result_list.append(number)
            prev_number = number
    return result_list


if __name__ == '__main__':
    original_list = [2, 2, 2, 3, 2, 3, 3, 2, 2, 3, 2]
    result_list = make_list_without_duplicates(original_list)
    print(result_list)
