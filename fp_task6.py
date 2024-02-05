from collections import deque


def max_calories_greedy(items, budget):
    res = []
    tot_cal = 0
    for _, item in items.items():
        item["calories_cost_ratio"] = item["calories"] / item["cost"]
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories_cost_ratio"], reverse=True)
    it_q = deque(items_sorted)
    while it_q:
        item = it_q.popleft()
        if item[1]["cost"] <= budget:
            res.append(item[0])
            budget -= item[1]["cost"]
            tot_cal += item[1]["calories"]
    return tot_cal, res


def max_calories_dp(budget, items):
    n = len(items)
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[(0, []) for _ in range(budget + 1)] for i in range(n + 1)]
    costs = [item["cost"] for item in items.values()]
    calories = [item["calories"] for item in items.values()]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for curr_budg in range(budget + 1):
            if i == 0 or curr_budg == 0:
                K[i][curr_budg] = (0, [])
            elif costs[i - 1] <= curr_budg:
                if calories[i - 1] + K[i - 1][curr_budg - costs[i - 1]][0] >= K[i - 1][curr_budg][0]:
                    K[i][curr_budg] = (calories[i - 1] + K[i - 1][curr_budg - costs[i - 1]][0],
                                       K[i - 1][curr_budg - costs[i - 1]][1] + [list(items.keys())[i - 1]])
                else:
                    K[i][curr_budg] = K[i - 1][curr_budg]
            else:
                K[i][curr_budg] = K[i - 1][curr_budg]

    return K[n][budget]


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    print(max_calories_greedy(items, 100))

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    print(max_calories_dp(100, items))
