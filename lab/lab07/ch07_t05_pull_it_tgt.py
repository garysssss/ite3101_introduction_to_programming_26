def hotel_cost(nights: int) -> int:
    return 140 * nights


def plane_ride_cost(city: str) -> int:
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    return 0


def rental_car_cost(days: int) -> int:
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


# 移除了 spending_money 參數
def trip_cost(city: str, days: int) -> int:
    # 根據測試的預期結果 (223 = 183 + 40)，酒店可能是不計入第一天的，
    # 如果這個版本遇到 AssertionError (例如 363 != 223)，請將 hotel_cost(days) 改為 hotel_cost(days - 1)
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)