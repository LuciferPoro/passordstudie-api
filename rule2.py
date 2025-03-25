import re
from blacklist import is_blacklisted

def validate_rule2(password):
    if is_blacklisted(password):
        return False, "Passordet er på en forbudt liste."

    if len(password) < 10:
        return False, "Passordet må være minst 10 tegn."
    if not re.search(r'[A-Z]', password):
        return False, "Passordet må inneholde minst én stor bokstav."
    if not re.search(r'[a-z]', password):
        return False, "Passordet må inneholde minst én liten bokstav."
    if not re.search(r'\d', password):
        return False, "Passordet må inneholde minst ett tall."

    return True, "Passordet er gyldig."
