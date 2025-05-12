def get_num_words(words):
    return len(words.split())


def get_num_letters(content):
    letter_count = {}
    for letter in content:
        l = letter.lower()

        if l not in letter_count:
            letter_count[l] = 1
        else:
            letter_count[l] += 1
    return letter_count


def sort_letters_dict(content):
    def sort_key(dict):
        return dict["num"]

    sorted_list = []
    dic = get_num_letters(content)
    for k in dic:
        v = dic[k]
        sorted_list.append({"char": k, "num": v})
        sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list
