# edge case: 
# same as task one, we need to check if the are values to measure



# MY correction:

def average_valid_measurements(values):
    if values == []
    total = 0
    count = len(values)

    for v in values:
        if v is not None:
            total += float(v)

    return total / count
