import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt


def rotate(angle):
    sina = np.sin(np.deg2rad(angle))
    cosa = np.cos(np.deg2rad(angle))
    return np.array([[cosa, -sina, 0], [sina, cosa, 0], [0, 0, 1]])


def reflect(axis):
    if axis == "x":
        return np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    if axis == "y":
        return np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    if axis in ("xy", "yx"):
        return np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])


def scale(xfactor=1.0, yfactor=1.0):
    return np.array([[xfactor, 0, 0], [0, yfactor, 0], [0, 0, 1]])


def shear(axis, xfactor=0.0, yfactor=0.0):
    if axis == "x":
        return np.array([[1, 0, 0], [xfactor, 1, 0], [0, 0, 1]])
    if axis == "y":
        return np.array([[1, yfactor, 0], [0, 1, 0], [0, 0, 1]])
    if axis in ("xy", "yx"):
        return np.array([[1, yfactor, 0], [xfactor, 1, 0], [0, 0, 1]])


def translate(dx, dy):
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])


def bilinear_interpolate(row, col, img):
    rows, cols = img.shape
    left_col, right_col = int(col), int(col) + 1
    top_row, bottom_row = int(row), int(row) + 1
    if not (top_row >= 0 and bottom_row < rows and left_col >= 0 and right_col < cols):
        return 0

    weight_left, weight_right = col - left_col, right_col - col
    weight_top, weight_bottom = row - top_row, bottom_row - row
    in_top = weight_left * img[top_row, left_col] + weight_right * img[top_row, right_col]
    in_bottom = weight_left * img[bottom_row, left_col] + weight_right * img[bottom_row, right_col]
    return int(weight_top * in_top + weight_bottom * in_bottom)


def get_projective_extends(transform, img):
    rows, cols = img.shape
    coords = np.array([[0, 0, 1], [0, cols - 1, 1], [rows - 1, 0, 1], [rows - 1, cols - 1, 1]])
    coords_transform = transform @ coords.T
    coords_transform /= coords_transform[2, :]
    mins = coords_transform.min(axis=1)
    maxs = coords_transform.max(axis=1)
    min_row, max_row = int(np.floor(mins[0])), int(np.ceil(maxs[0]))
    min_col, max_col = int(np.floor(mins[1])), int(np.ceil(maxs[1]))
    height = max_row - min_row + 1
    width = max_col - min_col + 1
    return min_row, max_row, min_col, max_col, height, width


def apply_projective_transform(transform, img):
    transform_inv = np.linalg.inv(transform)
    min_row, max_row, min_col, max_col, height, width = get_projective_extends(transform, img)
    new_img = np.zeros((height, width), dtype=np.uint8)

    for new_i in range(min_row, max_row):
        for new_j in range(min_col, max_col):
            i, j, k = transform_inv @ np.array([new_i, new_j, 1])
            i, j = i / k, j / k
            if 0 <= i < img.shape[0] and 0 <= j < img.shape[1]:
                new_img[new_i - min_row, new_j - min_col] = bilinear_interpolate(i, j, img)

    return new_img


def display_in_actual_size(img):
    dpi = mpl.rcParams["figure.dpi"]
    height, width = img.shape
    fig = plt.figure(figsize=(width / float(dpi), height / float(dpi)))
    ax = fig.add_axes((0, 0, 1, 1))
    ax.axis("off")
    ax.imshow(img, cmap="gray")
    plt.show()
