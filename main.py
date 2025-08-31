from stats import get_letter_stats, get_num_words, sort_letter_stats

PATH = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    txt = get_book_text(PATH)
    stats = get_letter_stats(txt)
    sorted_stats = sort_letter_stats(stats)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(txt)} total words")
    print("--------- Character Count -------")
    for letter_count in sorted_stats:
        if letter_count["char"].isalpha():
            print(f"{letter_count['char']}: {letter_count['num']}")
    print("============= END ===============")
    return


main()
