# correctness issue and BUG: 
# i think that we need to change the function, it sums the non canceled orders,
# but it divides it on the entire count of orders 
# which is wrong 
# we should only count the orders that have not  been canceled


# BUG :
# if all the orders will be canceled, the return statement will
# divide on 0, which is mathematically incorrect  

# handle edge cases: 
# we need to check if the are orders, or else the function is useless


# MY correction 
def calculate_average_order_value(orders):
    if orders == []:
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
            average = 0
        else:
            avrage = total / count           
    return avrage             
