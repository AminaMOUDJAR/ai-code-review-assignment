# edge case: 
# same as task one, we need to check if the are values to measure

# correctness issue and BUG: 
# the count used to calculate the average, includes the None values

# BUG:
# what if the 

# MY correction:

def average_valid_measurements(values):
    if values == []:
        return 0
    else:
        
        total = 0
        count = len(values)

        for v in values:
            if v is not None:
                total += float(v)

        return total / count
