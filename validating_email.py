import re


def parse_email(input):
    email_regex = re.compile(r"""
        ^([a-z0-9_\.-]+)    #first part of mail
        @                   # single @
        ([0-9a-z-]+)      #mail provider
        \.                  # single period
        ([a-z\.]{2,6})      #co, 
    """, re.X | re.I) # OR (re.VERBOSE | re.IGNORECASE )
    match = email_regex.search(input)
    print(f"username: {match.group(1)}")
    print(f"mail provider: {match.group(2)}")
    print(f"location: {match.group(3)}")
    return match.group()

print("================================")
print(parse_email("EmekaDanladi123@yahoo.co.uk"))
print("================================")



