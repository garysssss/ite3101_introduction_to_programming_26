def anti_vowel(text: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in text if ch not in vowels)
