import random
import re
from find_gender import find_gender
from generate_sentences import generate_sentences


def find_srs_pattern(num_items, target_repetitions):
    srs_list = []
    item_counts = {i: 0 for i in range(1, num_items + 1)}

    # Initial sequence
    for i in range(1, num_items + 1):
        srs_list.extend([i, i])
        item_counts[i] += 2
        for j in range(1, i + 1):
            if item_counts[j] < target_repetitions:
                srs_list.append(j)
                item_counts[j] += 1

    # Fill in the rest to ensure each item reaches the target repetition
    while any(count < target_repetitions for count in item_counts.values()):
        for i in range(1, num_items + 1):
            if item_counts[i] < target_repetitions:
                srs_list.append(i)
                item_counts[i] += 1

    return srs_list


def create_sentence_tuple_list(language, word_or_exp_list, n, verbs):
    sentence_tuple_list = []
    for num, word in enumerate(word_or_exp_list):
        text = generate_sentences(language=language, word_or_exp=word, n=n,
                                  verbs=verbs)
        sentences = [x for x in text.split('\n') if x != '']
        for s in sentences:
            # Matching the original sentence
            original_match = re.search(r'\d+[.)]\s*["\s]*(.*?)["\s]*\s*\(', s)
            sentence = original_match.group(1)
            gender = find_gender(language, sentence)
            # Matching the translation
            translation_match = re.search(r"\(\s*['\"]?(.*?)['\"]?\s*\)", s)

            # Only add to the list if both matches are successful
            if original_match and translation_match:
                sentence_tuple_list.append(
                    (num + 1, sentence, translation_match.group(1), gender))

    return sentence_tuple_list


def create_ordered_sentences(language, word_or_exp_list, shuffle=True, n=10,
                             SRS=False, verbs=False):
    if shuffle:
        random.shuffle(word_or_exp_list)
    sentence_tuple_list = create_sentence_tuple_list(language,
                                                     word_or_exp_list, n,
                                                     verbs)

    if SRS:
        srs_order = find_srs_pattern(len(word_or_exp_list), n)

        # Creating a dictionary for quick access to sentences based on number
        sentence_dict = {i: [] for i in range(1, len(word_or_exp_list) + 1)}
        for sentence in sentence_tuple_list:
            sentence_dict[sentence[0]].append(sentence)

        # Ordering the sentences based on the SRS pattern
        ordered_sentences = []
        for order in srs_order:
            # Check if the list for the current order is not empty
            if sentence_dict[order]:
                # Pop the first sentence from the list corresponding to the
                # current order
                ordered_sentences.append(sentence_dict[order].pop(0))
    else:
        ordered_sentences = sentence_tuple_list
    print("Here are the ordered sentences:\n")
    for sentence in ordered_sentences:
        print(f"{sentence[0]}: {sentence[1]}")
    return ordered_sentences
