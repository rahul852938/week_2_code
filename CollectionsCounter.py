from collections import Counter

shoes = int(input())
sizes = list(map(int, input().split()))
customers = int(input())

stock = Counter(sizes)
money = 0

for _ in range(customers):
    need, pay = map(int, input().split())
    if stock[need] > 0:
        money += pay
        stock[need] -= 1

print(money)
