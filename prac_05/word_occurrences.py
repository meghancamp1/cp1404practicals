sentence = input("Text: ")
words = sentence.split(" ")
words_to_count = {}
for word in words:
    count = words_to_count.get(word, 0)
    words_to_count[word] = count + 1
words_in_text = list(words_to_count.keys())
words_in_text.sort()
max_length = max(len(word_in_text) for word_in_text in words_in_text)
for word_in_text in words_in_text:
    print("{:{}} : {}".format(word_in_text, max_length, words_to_count[word_in_text]))
