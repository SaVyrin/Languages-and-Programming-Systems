def sort_list_by_rows(original_list: list):
    if len(original_list) == 0:
        return original_list

    asc_list = []
    desc_list = []
    for number_list in original_list:
        if check_ascending(number_list):
            asc_list.append(number_list)
        else:
            desc_list.append(number_list)

    result_list = asc_list + desc_list
    return result_list


def check_ascending(number_list: list):
    prev_number = number_list[0]
    for number in number_list[1:]:
        if prev_number > number:
            return False
        prev_number = number

    return True


def print_pretty_matrix(list_of_lists: list):
    for number_list in list_of_lists:
        print("[ ", end="")
        for number in number_list:
            print("{} ".format(number), end="")
        print("]")


if __name__ == '__main__':
    original_list = [
        [1, 2, 3, 4, 4],
        [1, 5, 2, 4, 6, 3],
        [1, 6, 3, 2, 5, 6],
        [1, 3, 5, 7, 9],
        [1, 5, 2, 6, 2, 5, 3],
        [1, 3, 4, 5, 6, 7]
    ]
    result_list = sort_list_by_rows(original_list)
    print_pretty_matrix(result_list)
