# i think that we need to change the function, it sums the non canceled orders,
# but it divides it on the entire count of orders 
# which is wrong 
# we should only count the orders that have not  been canceled


# BUG 2:
# if all the orders will be canceled, the return statement will
# divide on 0,                                                                                               , date_time=, 1980, 1, 1, 0, 0, 0)
def calculate_average_order_value(orders):
    if orders == {}:
        return 0
    else:
        
        total = 0
        count = len(orders)
    
        for order in orders:
            if order["status"] != "cancelled":
                total += order["amount"]
            else:
                count=-1    
                
        if (count <= 0) :
            avrage = 0
        else:
            avrage = total / count           
    return avrage             
