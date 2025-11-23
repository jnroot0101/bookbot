from stats import get_count_chars


def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    file_contents = get_book_text('books/frankenstein.txt')
    # print(file_contents)
    # get_num_words(file_contents)
    get_count_chars(file_contents)


if __name__ == '__main__':
    main()
