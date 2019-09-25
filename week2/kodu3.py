def username(firstname, lastname):
    returnvalue = firstname + "." + lastname
    return returnvalue.lower().replace('õ', 'o').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')

in_firstname = input(str("Sisesta eesnimi:"))
in_lastname = input(str("Sisesta perenimi:"))

print(username(in_firstname, in_lastname))