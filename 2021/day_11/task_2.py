import numpy as np

from utils.read_input import read_input_as_matrix


def get_adj(flashing):
    v_padding = np.expand_dims(np.zeros(len(flashing), int), axis=0)
    h_padding = np.transpose(v_padding)
    return (
        np.hstack((h_padding, flashing[:, :-1]))
        + np.hstack((flashing[:, 1:], h_padding))
        + np.vstack((v_padding, flashing[:-1, :]))
        + np.vstack((flashing[1:, :], v_padding))
        + np.vstack((np.hstack((h_padding, flashing[:, :-1]))[1:, :], v_padding))
        + np.vstack((v_padding, np.hstack((h_padding, flashing[:, :-1]))[:-1, :]))
        + np.vstack((np.hstack((flashing[:, 1:], h_padding))[1:, :], v_padding))
        + np.vstack((v_padding, np.hstack((flashing[:, 1:], h_padding))[:-1, :]))
    )


if __name__ == "__main__":
    octopuses = np.array(read_input_as_matrix("day_11/input.txt", "int"))

    step = 0
    while True:
        step += 1
        octopuses += np.ones_like(octopuses)
        flashed = np.zeros_like(octopuses)
        while np.sum(np.where(octopuses > 9, 1, 0)) > np.sum(flashed):
            flashing = (np.where(octopuses > 9, 1, 0) + flashed == 1).astype(int)
            octopuses += get_adj(flashing)
            flashed += flashing
        octopuses[np.where(flashed)] = 0
        if np.sum(octopuses) == 0:
            break

    print(step)
