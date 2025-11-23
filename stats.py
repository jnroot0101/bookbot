def sort_on(items):
    return items["num"]


def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")


def get_count_chars(text: str) -> dict[str, int]:
    freq = {}

    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1

    return freq


def sort_data(data: dict[str, int]) -> list[dict]:
    items = [
        {"char": char, "num": count}
        for char, count in data.items()
        # if char.isalpha()  # skip spaces, punctuation, symbols, etc.
    ]

    items.sort(reverse=True, key=sort_on)

    return items
