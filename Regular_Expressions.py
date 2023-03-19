import re

# Syntax from https://docs.python.org/3/library/re.html#regular-expression-syntax%22RE%20syntax

# pattern = re.compile(r"\[(on|off)\]") # Slight optimization
# [on] is special character
# print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")) # Returns a Match object!
# print(re.search(pattern, "Nada...:-("))# Doesn't return anything.


# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]

    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

# [a-zA-Z] : could start with normal or upper character
# \w : normal word
# {2,} have to have more than 2 character 
# @ literal 
pattern = r'[a-zA-Z]\w{2,}@[a-zA-Z]{3,}.[a-zA-Z]{3,}' # Your pattern here!
test_email(pattern)

