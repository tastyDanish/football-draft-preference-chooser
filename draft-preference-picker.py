import random

preferences = {
    "Peter": 4,
    "TheDarkTower": 3,
    "Zach": 4,
    "danielbgoo": 3,
    "Havelocke": 6,
    "Ian": 1,
    "LoopCanal": 3,
    "MaiusMalum": 12,
    "MalcumButlerXLIX": 7,
    "NickWins": 5,
    "Ray": 4,
    "Venkv": 11
}


def get_coward(things, start, end):
    for j in range(start, end):
        if len(things[j]) == 0:
            continue
        coward = random.choice(things[j])
        print(f"Coward {coward} pulled from preference {j}")
        choices[i].append(coward)
        choices[j].remove(coward)
        break
    return choices


if __name__ == '__main__':
    choices = {}
    for i in range(1, 13):
        choices[i] = []
        for y, x in preferences.items():
            if x == i:
                choices[i].append(y)

    for i in range(1, 13):
        print(f"================== FOR SPOT NUMBER {i} ====================")
        if len(choices[i]) == 0:
            choices = get_coward(choices, i+1, 13)
        print(f"here are the choices {choices[i]}")
        spotWinner = random.choice(choices[i])
        print(f"The winner of spot {i} is {spotWinner}")
        losers = [x for x in choices[i] if x != spotWinner]
        if len(losers) > 0:
            print(f"losers {losers} sent to next round")
            choices[i+1] = choices[i+1] + losers
