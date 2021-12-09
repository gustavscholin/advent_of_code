import numpy as np

from utils.read_input import read_input

if __name__ == "__main__":
    heightmap = read_input("day_9/input.txt")
    heightmap = np.array([[int(i) for i in row] for row in heightmap])

    v_padding = np.expand_dims(np.ones(len(heightmap), int) * 10, axis=0)
    h_padding = np.transpose(v_padding)

    min_adj = np.min(
        np.stack(
            (
                np.hstack((h_padding, heightmap[:, :-1])),
                np.hstack((heightmap[:, 1:], h_padding)),
                np.vstack((v_padding, heightmap[:-1, :])),
                np.vstack((heightmap[1:, :], v_padding)),
            ),
            axis=-1,
        ),
        axis=-1,
    )

    print(np.sum(heightmap[np.where(heightmap < min_adj)] + 1))
