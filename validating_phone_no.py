import re


#   SEARCH (validating phone numbers and any entry before or after and returning the first/0ne)
 
def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{4}-?\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return "Error"

# FINDALL (validating phone numbers and any entry before or after and returning all)
def extract_all_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{4}-?\d{4}\b")    
    match = phone_regex.findall(input)
    return match


#   SEARCH (only validating phone numbers)
def is_valid_phone(input):
    phone_regex = re.compile(r"^\b\d{3} \d{4}-?\d{4}\b$")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return "error"


#   FULL MATCH (also validating phone numbers only)
def is_all_valid_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{4}-\d{4}\b")
    match = phone_regex.fullmatch(input)
    if match:
        return match.group()
    return "error"


print(extract_phone("080 3056-7240 566 7819-4667")) #search only call the first number
print(extract_phone("080 3056-000033"))


print(extract_all_phone("080 3056-7204, 566 7889-4667"))
print(extract_all_phone("080 3056-000"))


print(is_valid_phone("080 5678-2844"))
print(is_valid_phone("080 5678-2845"))
print(is_valid_phone("080 5678-2846"))

print(is_all_valid_phone("099 7780 0000 yusuf"))
print(is_all_valid_phone("099 7780-0000"))
print(is_all_valid_phone("dd 099 7780 0000"))
