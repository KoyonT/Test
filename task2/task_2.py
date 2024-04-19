path_to_circle = input('Введите абсолютный путь к файлу с данными о окружности: ')
# path_to_circle = ('')
try:
    with open(path_to_circle) as file1:
        circle_info = [list(map(float, line.split(" "))) for line in file1]
except IOError:
    print('Файл не найден!')

path_to_points = input('Введите абсолютный путь к файлу с данными о точках: ')
# path_to_points = ('')
try:
    with open(path_to_points) as file2:
        points_info = [list(map(float, line.split(" "))) for line in file2]
except IOError:
    print('Файл не найден!')

circle_center = circle_info[0]
radius = circle_info[1][0]


def point_position(circle_center, radius, point):
    x0, y0 = circle_center
    x, y = point
    distance_squared = (x - x0) ** 2 + (y - y0) ** 2
    if distance_squared == radius ** 2:
        print(0)
    elif distance_squared < radius ** 2:
        print(1)
    else:
        print(2)


for i in range(0, len(points_info)):
    point = points_info[i]
    point_position(circle_center, radius, point)
