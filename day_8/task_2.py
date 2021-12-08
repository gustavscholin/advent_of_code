import numpy as np

from utils.read_input import read_input

if __name__ == "__main__":
    digit_list = read_input("day_8/input.txt")
    digit_list = [tuple(map(str.split, digits.split("|"))) for digits in digit_list]

    output_sum = 0
    for notes, output in digit_list:
        notes = ["".join(sorted(s)) for s in notes]
        output = ["".join(sorted(s)) for s in output]

        translation = {}
        translation["1"] = next(x for x in notes if len(x) == 2)
        notes.remove(translation["1"])
        translation["4"] = next(x for x in notes if len(x) == 4)
        notes.remove(translation["4"])
        translation["7"] = next(x for x in notes if len(x) == 3)
        notes.remove(translation["7"])
        translation["8"] = next(x for x in notes if len(x) == 7)
        notes.remove(translation["8"])
        translation["3"] = next(x for x in notes if len(x) == 5 and len(set(x) & set(translation["1"])) == 2)
        notes.remove(translation["3"])
        translation["2"] = next(x for x in notes if len(x) == 5 and len(set(x) & set(translation["4"])) == 2)
        notes.remove(translation["2"])
        translation["5"] = next(x for x in notes if len(x) == 5)
        notes.remove(translation["5"])
        translation["0"] = next(x for x in notes if len(x) == 6 and len(set(x) & set(translation["5"])) == 4)
        notes.remove(translation["0"])
        translation["9"] = next(x for x in notes if len(x) == 6 and len(set(x) & set(translation["4"])) == 4)
        notes.remove(translation["9"])
        translation["6"] = notes[0]

        inv_translation = {v: k for k, v in translation.items()}
        translated_output = int("".join([inv_translation[i] for i in output]))
        output_sum += translated_output

    print(output_sum)
