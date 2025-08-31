def get_num_words(txt: str):
    num_words = len(txt.split())
    return num_words


def get_letter_stats(txt: str):
    letter_stats = {}
    for letter in txt:
        letter = letter.lower()
        if letter in letter_stats:
            letter_stats[letter] += 1
        else:
            letter_stats[letter] = 1
    return letter_stats


def sort_letter_stats(letter_stats):
    # Helper function for sort
    def sort_on(items):
        return items["num"]

    sorted_stats = []
    for key in letter_stats:
        sorted_stats.append({"char": key, "num": letter_stats[key]})
    sorted_stats.sort(reverse=True, key=sort_on)

    return sorted_stats
