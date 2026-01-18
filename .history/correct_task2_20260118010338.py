# Bug 1:
# we need to first check if there are emails

# Bug 2
# what if the @ is repeated several times? "a@@eefll"
# also there is no "." like ".com" or ".edu"  or ".dz"...?

# it's better to use regular expressions in this case

import re

def count_valid_emails(emails):
    count = 0

    for email in emails:
        if "@" in email:
            count += 1

    return count
