# i think that we need to change the function, it sums the non canceled orders,
# but it divides it on the entire count of orders 
# which is wrong 
# we should only count the orders that have not  been canceled

def calculate_average_order_value(orders):
    total = 0
    count = len(orders)
    
    for order in orders:
        if order["s"]
