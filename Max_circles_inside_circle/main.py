from circle import Circle


def read_from_file(file_name: str):
    result_list = []
    with open('input_files/' + file_name, 'r') as file:
        for line in file:
            circle_params = line.split(" ")
            x = float(circle_params[0])
            y = float(circle_params[1])
            r = float(circle_params[2])
            new_circle = Circle(x, y, r)

            result_list.append(new_circle)

    return result_list


def find_circle_with_max_circles_in_it(circles_list: list):
    result_circle = circles_list[0]
    for current_circle in circles_list:
        circles_count_in_current_circle = get_circles_count_in_circle(current_circle, circles_list)
        current_circle.set_circles_in(circles_count_in_current_circle)

        if result_circle.get_circles_in() < circles_count_in_current_circle:
            result_circle = current_circle
        elif result_circle.get_circles_in() == circles_count_in_current_circle:
            result_circle = choose_max_area_circle(current_circle, result_circle)

    return result_circle


def get_circles_count_in_circle(current_circle: Circle, circles_list: list):
    circles_count = 0
    for other_circle in circles_list:
        if other_circle == current_circle:
            continue
        if current_circle.circle_in(other_circle):
            circles_count += 1

    return circles_count


def choose_max_area_circle(current_circle: Circle, result_circle: Circle):
    current_circle_area = current_circle.get_area()
    result_circle_area = result_circle.get_area()

    if current_circle_area > result_circle_area:
        return current_circle

    return result_circle


if __name__ == '__main__':
    # circles_list = read_from_file("input1.txt")
    # circles_list = read_from_file("input2.txt")
    # circles_list = read_from_file("input3.txt")
    circles_list = read_from_file("input4.txt")
    # circles_list = read_from_file("input5.txt")
    result_circle = find_circle_with_max_circles_in_it(circles_list)
    result_circle.print()
