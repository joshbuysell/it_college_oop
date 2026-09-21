def format_text(text: str, style: str = "uppercase") -> str:
    if style == "uppercase":
        return text.upper()
    elif style == "lowercase":
        return text.lower()
    elif style == "title":
        return text.title()
    return text


def count_words(text: str) -> dict:
    words = text.split()
    return {
        "total_words": len(words),
        "total_chars": len(text),
        "unique_words": len(set(words)),
    }
