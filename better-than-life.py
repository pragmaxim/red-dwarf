import requests

file = requests.get('https://gist.githubusercontent.com/pragmaxim/fbf0a4c4d9012358f7e4494798e30de0/raw/41a428e0e484bf216c58ecb0ab51cbb95d47d372/red-dwarf.txt')

# načteme obsah souboru do proměnné 'text'
text = file.text

print("Počet znaků v kapitole Lepší než život: ", len(text))

print("prvních 100 písmenek/znaků: ", text[:100])

print("dalších 100 písmenek/znaků", text[100:200])

# Vypíšeme všechny unikátní znaky v textu a jejich celkový počet
unique_chars = sorted(list(set(text)))
vocab_size = len(unique_chars)
print("všechny unikátní znaky v textu", ''.join(unique_chars))
print("počet unikátních znaků v textu", vocab_size)

# Vypíšeme počet unikátních znaků individuálně pomocí for-loop
unique_chars = sorted(list(set(text)))
print("počet unikátních znaků individuálně pomocí for-loop")
for char in unique_chars:
    count = text.count(char)
    print(f"'{char}': {count}")

# Vypíšeme prvních 10 vět s přítomností slova David
def get_sentences_with_word(word):
    sentences = text.split('.')
    sentences_with_word = []
    for sentence in sentences:
        if word in sentence:
            sentences_with_word.append(sentence.replace('\n', ''))
    return sentences_with_word


print("věty s obsahem slova David:\n", '\n'.join(get_sentences_with_word("David")))
