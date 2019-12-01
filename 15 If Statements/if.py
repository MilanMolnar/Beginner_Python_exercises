
is_male = True
is_tall = True


if is_male or is_tall:
    print("You are a Male or tall or both")
else:
    print("you are not a Male nor tall")

if is_male and is_tall:
    print("You are a Male and tall")
else:
    print("You are not a Male and not tall")

if is_male and is_tall:
    print("You are a Male and tall")
elif is_male and not(is_tall):
    print("You are a short Male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a Male and not tall")
