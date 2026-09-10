from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = False
    for item in allowed:
        if item.lower() in ingredients.lower():
            is_valid = True
            break
    status = "VALID" if is_valid else "INVALID"
    return ingredients + " - " + status
