# Valid Sentence Coding Test
# Prompt: Write a function that determines if an input string is a “valid” sentence

def valid_sentence(sentence: str) -> bool:
    """
    Check if sentence is valid based on meeting criteria of set conditions:

    Condition 1: String starts with a capital letter.

    Condition 2: String has an even number of quotation marks. (Note: Only ask for even numbers of quotations marks, not necessarily have to match)

    Condition 3: String ends with one of the following sentence termination characters: ".", "?", "!"

    Condition 4: String has no period characters other than the last character.

    Condition 5: Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).

    :param sentence: Text string to be checked for validity
    :return: True if sentence is valid, False if not
    :rtype: bool
    :raises:
        TypeError: If sentence argument passes is not a string
        ValueError: If sentence argument contains unconventional spacing
    """
    # Initial Check
    if type(sentence) != str:
        raise TypeError("Argument passed must be a string")

    sentence_list = list(sentence.split(" "))
    if "" in sentence_list:
        raise ValueError("Argument string passed must not have unconventional spacing (Ex. Start or end with spacing)")

    # Variables For Condition Checks
    termination_characters = [".", "?", "!"]
    quotation_marks = ["\"", "\'", "“", "”"]
    quotations_count = 0

    # Condition 1
    if sentence_list[0][0] != sentence_list[0][0].upper():
        return False

    # Condition 3
    elif sentence_list[-1][-1] not in termination_characters:
        return False

    else:
        for word_index in range(len(sentence_list)):
            current_word = sentence_list[word_index]
            # Condition 5
            if len(current_word) > 1:
                if current_word[0].isnumeric() and current_word[1].isnumeric():
                    number_value = int(current_word[0] + current_word[1])
                    if number_value < 13:
                        return False
            else:
                if current_word[0].isnumeric():
                    number_value = int(current_word[0])
                    if number_value < 13:
                        return False
            # Condition 4
            for letters in current_word:
                if letters == "." and word_index != len(sentence_list) - 1:
                    return False
                # Condition 2
                elif letters in quotation_marks:
                    quotations_count += 1
        # Condition 2 (cont.)
        if quotations_count % 2 != 0:
            return False

    # Sentence argument passed all conditions
    return True


