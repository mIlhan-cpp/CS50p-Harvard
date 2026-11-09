from validator_collection import checkers

email=input('whats your mail:')
if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")
