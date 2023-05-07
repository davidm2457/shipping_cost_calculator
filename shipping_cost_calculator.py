# Basic shipping cost for box trucks.
def shipping_cost(weight, distance):
    if weight <= 5_000:
        cost = distance * 1.8
    elif weight <= 10_000:
        cost = distance * 2
    else:
        cost = None
        print("Too Heavy...weight must be below 10000!")
    return(cost)

print(shipping_cost(11111, 1000))
