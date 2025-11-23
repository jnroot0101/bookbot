def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")
    # print(text)


def get_count_chars(text: str) -> dict[str, int]:
    freq = {}
    # texts = text.split()
    # print(text)

    for char in text.lower():
        # print(char)
        # char = char.lower()
        freq[char] = freq.get(char, 0) + 1
        # # freq.get(char, 0)
        # if char in freq:
        #     freq[char] += 1
        # else:
        #     freq[char] = 1

    print(freq)
    return freq
