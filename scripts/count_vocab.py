import json
from os import listdir
from os.path import isfile, join


def main():
    entities_dir = '../entities/'
    file_list = [f for f in listdir(entities_dir) if isfile(join(entities_dir, f))]

    vocab = {}
    for file_name in file_list:
        if 'entries' in file_name:
            with open("{}{}".format(entities_dir, file_name)) as file:
                entities = json.load(file)
                for entity in entities:
                    for word in entity['value'].replace(',', '').split():
                        if '@' not in word:
                            if word not in vocab:
                                vocab[word] = 0
                            vocab[word] += 1

                    for syn in entity['synonyms']:
                        for word in syn.replace(',', '').split():
                            if '@' not in word:
                                if word not in vocab:
                                    vocab[word] = 0
                                vocab[word] += 1

    intents_dir = '../intents/'
    file_list = [f for f in listdir(intents_dir) if isfile(join(intents_dir, f))]

    for file_name in file_list:
        if 'usersays' in file_name:
            with open("{}{}".format(intents_dir, file_name)) as file:
                intents = json.load(file)
                for intent in intents:
                    for data in intent['data']:
                        for word in data['text'].replace(',', '').replace('.', '').replace('?', '').split():
                            if '@' not in word:
                                if word not in vocab:
                                    vocab[word] = 0
                                vocab[word] += 1

    print(len(vocab.keys()))
    print(sum(vocab.values()))


if __name__ == "__main__":
    main()
