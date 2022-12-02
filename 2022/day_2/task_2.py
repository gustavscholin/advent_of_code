from utils.read_input import read_input

if __name__ == "__main__":
    strategy = read_input("2022/day_2/input.txt")
    scores = {
        "A X": 3,
        "B X": 1,
        "C X": 2,
        "A Y": 4,
        "B Y": 5,
        "C Y": 6,
        "A Z": 8,
        "B Z": 9,
        "C Z": 7,
    }
    score = 0
    for round in strategy:
        score += scores[round]
    print(score)
