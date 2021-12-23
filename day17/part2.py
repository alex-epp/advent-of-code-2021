
def simulate(v, mins, maxs):
    x, y = 0, 0
    vx, vy = v
    (x_min, y_min), (x_max, y_max) = mins, maxs
    peak_y = y
    while True:
        x, y = x + vx, y + vy
        peak_y = max(peak_y, y)
        vx, vy = max(vx - 1, 0), vy - 1
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return peak_y
        if vy < 0 and y < y_min:
            return None


def main(mins, maxs):
    (x_min, y_min), (x_max, y_max) = mins, maxs

    vy_min = -max(abs(y_min), abs(y_max))
    vy_max = max(abs(y_min), abs(y_max))

    vx_min = 0
    vx_max = x_max

    peaks = []

    for vx in range(vx_max, vx_min-1, -1):
        for vy in range(vy_max, vy_min-1, -1):
            y = simulate((vx, vy), mins, maxs)
            if y is not None:
                peaks.append(y)

    return len(peaks)


if __name__ == '__main__':
    print(main((20, -10), (30, -5)))
    print(main((96, -144), (125, -98)))

