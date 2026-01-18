# handle edge cases:
# we need to first check if there are emails

# correctness issue
# what if the @ is repeated several times? "a@@eefll"
# also there is no "." like ".com" or ".edu"  or ".dz"...?

# My correction: Method 1 - use regular expressions in this case

import re

def count_valid_emails(emails):
    if emails == []:
        return 0
    else:
        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
        count = 0

        for email in emails:
            if re.match(pattern, email):
                count += 1
    
        return count

# My correction: Method 2 - use validator package

import validators

def count_valid_emails(emails):
    count = 0

    for email in emails:
        if validators.email(email):
            count += 1

    return count
