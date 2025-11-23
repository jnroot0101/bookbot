import sys

from stats import sort_data, get_count_chars, get_num_words


def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])

    get_num_words(file_contents)
    data = get_count_chars(file_contents)
    result = sort_data(data)

    for item in result:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")


if __name__ == '__main__':
    main()
