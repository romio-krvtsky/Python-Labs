import constants
from string import punctuation


def input_of_k_and_n():
    choice = input(constants.welcome_massage).split()

    if choice[0] == constants.default_value:
        k_top, ngramms = constants.k_value, constants.n_value
    elif choice[0].isdigit() and choice[1].isdigit():
        k_top, ngramms = int(choice[0]), int(choice[1])
    else:
        raise ValueError(constants.error_massage)

    return k_top, ngramms


def get_top_of_ngramms(list_of_words: list, n_gramms: int):
    top = dict()
    for word in list_of_words:

        if not len(word) < n_gramms:
            begin, end = 0, n_gramms

            for _ in range(len(word) - n_gramms + constants.one):
                temp_word = word[begin: end]

                if temp_word in top.keys():
                    top[temp_word] += constants.one
                else:
                    top[temp_word] = constants.one

                begin += constants.one
                end += constants.one

    return top


def get_lst_of_words_in_each_sentence(text: list):
    lst_of_words_in_each_sentence = list()
    temp = 0
    for i in range(len(text)):

        if text[i][-1] in constants.sentence_end and not text[i] in constants.abbreviations:
            lst_of_words_in_each_sentence.append(i + constants.one - temp)
            temp = i + constants.one

    return lst_of_words_in_each_sentence


def get_lst_of_all_words(text: list):
    lst_of_all_words = list()
    for wrd in text:

        for letter in wrd:
            if letter in punctuation and letter != constants.hyphen \
                    and letter != constants.apostrophe:
                wrd = wrd.replace(letter, '')

        lst_of_all_words.append(wrd)

    return lst_of_all_words


def get_words_and_their_amount(text: list):
    words_and_their_amount = dict()
    for wrd in text:

        if wrd in words_and_their_amount.keys():
            words_and_their_amount[wrd] += constants.one
        else:
            words_and_their_amount[wrd] = constants.one

    return words_and_their_amount


def mean_value(lst: list):
    return sum(lst) / len(lst)


def median_value(lst: list):
    n = len(lst)
    index = n // 2
    if n % 2:
        return sorted(lst)[index]
    return sum(sorted(lst)[index - 1: index + 1]) / 2


