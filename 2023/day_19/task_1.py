import re


def do_workflow(rating: dict[str:int], rules: list[list[str]]):
    next_workflow = ""
    for statement, workflow in rules[:-1]:
        cat = statement[0]
        val = rating[cat]
        if eval(statement.replace(cat, "val")):
            next_workflow = workflow
            break
    if not next_workflow:
        next_workflow = rules[-1][0]
    if next_workflow in ("A", "R"):
        return next_workflow
    else:
        return do_workflow(rating, workflows[next_workflow])


if __name__ == "__main__":
    with open("2023/day_19/input.txt", "r") as f:
        workflows_str, ratings_str = [
            lines.splitlines() for lines in f.read().split("\n\n")
        ]

    workflows = {}
    for w in workflows_str:
        name, rules = re.match(r"(.+)\{(.+)\}", w).groups()
        workflows[name] = [r.split(":") for r in rules.split(",")]

    accepted_ratings = []
    for r in ratings_str:
        rating_str = re.match(r"\{(.+)\}", r).group(1)
        rating = {}
        for v in rating_str.split(","):
            cat, val = v.split("=")
            rating[cat] = int(val)
        if do_workflow(rating, workflows["in"]) == "A":
            accepted_ratings.append(sum(rating.values()))
    print(sum(accepted_ratings))
