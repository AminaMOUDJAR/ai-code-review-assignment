# Bug 1:
# we need to first check if there are emails

# Bug 2
# what if the @ is repeated several times? "a@@eefll"
# also there is no "." like ".com" or ".edu"  or ".dz"...?

# My correction: Method 1 - use regular expressions in this case

import re

def count_valid_emails(emails):
    if emails == []:
        return 0
    else:
        pattern = 
        count = 0

        for email in emails:
            if "@" in email:
                count += 1
    
        return count
