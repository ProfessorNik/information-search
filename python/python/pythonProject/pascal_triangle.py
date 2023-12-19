from functools import reduce


def pascal_triangle(n: int):
    if n <= 0 or not isinstance(n, int):  # проверка на невалидное значение n
        print("Ошибка: введите целое положительное число.")
        return

    return reduce(
        lambda triangle, line_num: triangle + [line_in_pascal_triangle(line_num, triangle)],
        range(1, n),
        [[1]]
    )


def line_in_pascal_triangle(line_num: int, triangle: list[list[int]]) -> list[int]:
    print(triangle)
    prev_row = triangle[line_num - 1]
    return reduce(
        lambda row, elem_num: row + [prev_row[elem_num - 1] + prev_row[elem_num]],
        range(1, line_num),
        [1]
    ) + [1]


def print_pascal_triangle(triangle: list[list[int]]):
    for row in triangle:
        print(' '.join([str(num) for num in row]))


n = int(input("Введите число n: "))
print_pascal_triangle(pascal_triangle(n))
