def word_frequency_counter(sentence):
    word_counts = {}
    words = sentence.lower().split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sentence = input("Enter a sentence: ")
word_counts = word_frequency_counter(sentence)

for word, count in word_counts.items():
    print(f"{word}: {count}")
