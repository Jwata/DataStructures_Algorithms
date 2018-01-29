def calculate_intersection(rect_1, rect_2):
    range_x_1 = (rect_1['left_x'],
            rect_1['left_x'] + rect_1['width'])
    range_x_2 = (rect_2['left_x'],
            rect_2['left_x'] + rect_2['width'])
    range_y_1 = (rect_1['bottom_y'],
            rect_1['bottom_y'] + rect_1['height'])
    range_y_2 = (rect_2['bottom_y'],
            rect_2['bottom_y'] + rect_2['height'])

    overlap_x_start, overlap_x_end = overlap(range_x_1, range_x_2)
    overlap_y_start, overlap_y_end = overlap(range_y_1, range_y_2)

    if not overlap_x_start or not t overlap_y_start:
        return None

    overlap_rect = {
        'left_x': overlap_x_start,
        'bottom_y': overlap_y_start,
        'width': overlap_x_end - overlap_x_start,
        'height': overlap_y_end - overlap_y_start
    }

    return overlap_rect

def overlap(range_1, range_2):
    start = max(range_1[0], range_2[0])
    end = min(range_1[1], range_2[1])

    if start < end:
        return (start, end)
    else:
        return (None, None)

rectangle_1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 6,
    'height': 3
}

rectangle_2 = {
    'left_x': 4,
    'bottom_y': 2,
    'width': 4,
    'height': 10
}

intereaction = calculate_intersection(rectangle_1, rectangle_2)
print(intereaction)

rectangle_1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 1,
    'height': 1
}

rectangle_2 = {
    'left_x': 3,
    'bottom_y': 3,
    'width': 1,
    'height': 1
}

intereaction = calculate_intersection(rectangle_1, rectangle_2)
print(intereaction) # should be None
