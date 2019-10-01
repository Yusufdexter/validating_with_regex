import re


url_regex = re.compile(r"(https?)://(www\.[A-Za-z-]{2,256}\.[A-Za-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")

match = url_regex.search("https://www.google.com/search=tunde/346851513852446244")

print(f"complete_url: {match.group(0)}")
print(f"protocol: {match.group(1)}")
print(f"domain: {match.group(2)}")
print(f"others: {match.group(3)}")
print(f"complete_url: {match.group()}")
print(match.groups())