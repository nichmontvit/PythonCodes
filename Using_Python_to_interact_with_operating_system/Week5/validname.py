def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        # a valueError is an error occured when the value of a parameter is incorrect
        raise ValueError("value must be minimum 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

print(validate_user("Maria", 2))

