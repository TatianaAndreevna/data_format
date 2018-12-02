import xml.etree.ElementTree as ET


def file_xml():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("files/newsafr.xml", parser)
    titles = []
    root = tree.getroot()
    xml_description = root.findall('channel/item/description')
    return xml_description


def characters_word():
    list_words = str()
    for description in file_xml():
        list_words += description.text
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