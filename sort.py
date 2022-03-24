import json


def sort_routes(grade, sort):
    with open("problems.json") as f:
        raw_data = json.load(f)

    data = raw_data["data"]
    problem_list = []

    for i in data:
        if i["grade"] == grade.upper():
            problem_list.append(i)

    if sort == "repeats":
        problem_list = sorted(problem_list, key=lambda x: x["repeats"], reverse=True)

    if sort == "rating":
        problem_list = sorted(problem_list, key=lambda x: x["userRating"], reverse=True)

    return problem_list
