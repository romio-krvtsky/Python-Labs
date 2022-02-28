from string import punctuation
from statistics import mean, median


def top_n_gramms(list_of_words: list, n_gramms: int):
    top = dict()
    for word in list_of_words:
        if not len(word) < n_gramms:
            begin, end = 0, n_gramms
            for _ in range(len(word) - n_gramms + 1):
                temp_word = word[begin:end]
                if temp_word in top.keys():
                    top[temp_word] += 1
                else:
                    top[temp_word] = 1
                begin += 1
                end += 1
        else:
            pass
    return top


path1 = 'input.txt'
path2 = 'output.txt'

words_amount = dict()
lst_of_words_in_each_sentence = list()
abbreviation = ['Mr.', 'Mrs.', 'Ms.', 'etc.', 'Dr.', 'Capt.', 'Col.',
                'Gen.', 'Gov.', 'Jr.', 'Lt.', 'Prof.', 'St.', 'Sr.', 'Sgt.']
with open(path1, 'r') as file:
    text = file.read().split()
    temp = 0
    for i in range(len(text)):
        if text[i][-1] in '.!?' and not text[i] in abbreviation:
            lst_of_words_in_each_sentence.append(i+1 - temp)
            temp = i+1
    only_words = list()
    for wrd in text:
        for letter in wrd:
            if letter in punctuation and letter != '-' and letter != "'":
                wrd = wrd.replace(letter, '')
        only_words.append(wrd)
        if wrd in words_amount.keys():
            words_amount[wrd] += 1
        else:
            words_amount[wrd] = 1

print('top-K most frequently repeated letter N-grams.\n' +
      'Enter K and N. Or if you want to leave them default, enter "default"')
choice = input().split()
if choice[0] == 'default':
    k_top, n_gramms = 10, 4
elif choice[0].isdigit() and choice[1].isdigit():
     k_top, n_gramms = int(choice[0]), int(choice[1])
else:
    raise ValueError('Error input!')

our_top = top_n_gramms(only_words, n_gramms)
our_top = dict(sorted(our_top.items(), key=lambda x: x[1], reverse=True))

with open(path2, 'w') as file:
    counter = 1
    for key, value in our_top .items():
        if counter > k_top:
            break
        file.write(f'{counter}. {key} - {value} \n')
        counter += 1
    file.write('-----------------------------------------------------')
    file.write(f'\nMean amount of words: {mean(lst_of_words_in_each_sentence)}' +
               f'\nMedian amount of words: {median(lst_of_words_in_each_sentence)}\n')
    file.write('-----------------------------------------------------\n')
    for key, value in words_amount.items():
        file.write(f'{key} - {value}\n')
