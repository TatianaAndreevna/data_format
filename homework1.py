import json


def file_json():
    with open("files/newsafr.json", encoding='utf-8') as datafile:
        json_data = json.load(datafile)
    return json_data


def characters_word():
    list_words = str()
    for items in file_json()['rss']['channel']['items']:
        list_words += items['description']
    description = list_words.split()
    long_words = []
    for word in description:
        if len(word) > 6:
            long_words.append(word)
    return long_words


def number_words():
    words = {}
    for word in characters_word():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def top_10_words():
    l = lambda number_words: number_words[1]
    sort_list = sorted(number_words().items(), key=l, reverse=True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 11:
            break
    print(top_10)


if __name__ == "__main__":
    top_10_words()