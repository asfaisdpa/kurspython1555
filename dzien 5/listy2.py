coins = [5, 2, 1, 0.5, 0.2, 0.1]
coins_amount = [0, 0, 0, 0, 0, 0,]

to_pay = 12.5
cash = 20

rest = cash - to_pay

for index, coin in enumerate(coins):
    if coin <= rest:
        quantity = rest // coin
        coins_amount[index] = quantity
        # rest = rest - quantity * coin
        rest -= quantity * coin