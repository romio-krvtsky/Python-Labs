import constants
import utilities


def main():
    k_top, n_gramms = utilities.input_of_k_and_n()

    path1 = 'input.txt'
    path2 = 'output.txt'

    with open(path1, 'r') as file:
        text = file.read().lower().split()

        list_of_words_in_each_sentence = utilities.get_lst_of_words_in_each_sentence(text)

        list_of_all_words = utilities.get_lst_of_all_words(text)

        word_and_its_amount = utilities.get_words_and_their_amount(list_of_all_words)

    top_of_ngramms = utilities.get_top_of_ngramms(list_of_all_words, n_gramms)
    top_of_ngramms = dict(sorted(top_of_ngramms.items(), key=lambda x: x[1], reverse=True))

    with open(path2, 'w') as file:
        counter = constants.one

        for key, value in top_of_ngramms.items():

            if counter > k_top:
                break

            file.write(f'{counter}. {key} - {value} \n')
            counter += constants.one

        file.write('-----------------------------------------------------')
        file.write(f'\nMean amount of words: {utilities.mean_value(list_of_words_in_each_sentence)}' +
                   f'\nMedian amount of words: {utilities.median_value(list_of_words_in_each_sentence)}\n')
        file.write('-----------------------------------------------------\n')

        for key, value in word_and_its_amount.items():
            file.write(f'{key} - {value}\n')


if __name__ == "__main__":
    main()

