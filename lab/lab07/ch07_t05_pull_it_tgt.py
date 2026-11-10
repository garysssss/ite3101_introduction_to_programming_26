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


def rental_car_cost(days: int) -> int:
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


# 新增這個函數來把所有費用加總 (Pull it together)
def trip_cost(city: str, days: int, spending_money: int = 0) -> int:
    # 這裡的 hotel_cost 通常與天數 (days) 相同
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money