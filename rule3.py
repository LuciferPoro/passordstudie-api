from blacklist import is_blacklisted

def validate_rule3(password):
    if is_blacklisted(password):
        return False, "Passordet er på en forbudt liste."

    if len(password) < 12:
        return False, "Passordet må være minst 12 tegn."
    if len(set(password)) < 6:
        return False, "Passordet må inneholde minst 6 ulike tegn."
    if password.lower() == password or password.upper() == password:
        return False, "Passordet må blande store og små bokstaver."

    return True, "Passordet er gyldig."
