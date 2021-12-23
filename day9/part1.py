import numpy as np


def main(lines):
    heightmap = np.array([[int(digit) for digit in line.strip()] for line in lines])

    augmented_heightmap = np.zeros((heightmap.shape[0] + 2, heightmap.shape[1] + 2))
    augmented_heightmap[:] = np.infty
    augmented_heightmap[1:-1, 1:-1] = heightmap

    low_point_mask = (
            np.less(heightmap, augmented_heightmap[:-2, 1:-1]) &
            np.less(heightmap, augmented_heightmap[2:, 1:-1]) &
            np.less(heightmap, augmented_heightmap[1:-1, :-2]) &
            np.less(heightmap, augmented_heightmap[1:-1, 2:])
    )

    return (heightmap[low_point_mask] + 1).sum()


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

