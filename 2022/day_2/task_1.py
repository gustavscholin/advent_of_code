from utils.read_input import read_input

if __name__ == "__main__":
    strategy = read_input("2022/day_2/input.txt")
    scores = {
        "A X": 4,
        "B X": 1,
        "C X": 7,
        "A Y": 8,
        "B Y": 5,
        "C Y": 2,
        "A Z": 3,
        "B Z": 9,
        "C Z": 6,
    }
    score = 0
    for round in strategy:
        score += scores[round]
    print(score)
