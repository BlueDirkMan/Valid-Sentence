from valid_sentence import valid_sentence

given_valid_cases = [
    "The quick brown fox said “hello Mr lazy dog”.",
    "The quick brown fox said hello Mr lazy dog.",
    "One lazy dog is too few, 13 is too many.",
    "One lazy dog is too few, thirteen is too many.",
    "How many \"lazy dogs\" are there?"
]

given_invalid_cases = [
    "The quick brown fox said \"hello Mr. lazy dog\".",
    "the quick brown fox said “hello Mr lazy dog\".",
    "\"The quick brown fox said “hello Mr lazy dog.\"",
    "One lazy dog is too few, 12 is too many.",
    "Are there 11, 12, or 13 lazy dogs?",
    "There is no punctuation in this sentence"
]

personal_valid_cases = [
    "Hello my friend.",
    "I like number one and two, but not 13.",
    "What time is it???",
    "Faker once said, 'I have started enjoying Yasuo, so I am playing him more'.",
    "I main Yasuo and Yone."
]

personal_invalid_cases = [
    "hello my friend.",  # Does not start with capital
    "I like number 1 and 2, but not thirteen.",  # Number 1 and 2 (below 13), not written as word
    "What time is it",  # No termination character
    "Faker once said, 'I have started enjoying Yasuo, so I'm playing him more'.",  # Not even quotation
    "Yes, I main Yasuo and Yone. How can you tell?" # Period character exist, but not at the end
]

type_error_cases = [
    True,
    False,
    12.345,
    12345,
]

value_error_cases = [
    " ",
    " Hello my friend. ",
    " Hello my friend.",
    "Hello my friend. ",
    "\"\"\" "
]

print("-----Given Valid Cases-----")
for cases in given_valid_cases:
    try:
        print("Output: ", valid_sentence(cases), "|", "Expected: True")
    except Exception as inst:
        print(type(inst))
        print("Error Occurred: ", inst.args)

print("-----Given Invalid Cases-----")
for cases in given_invalid_cases:
    try:
        print("Output: ", valid_sentence(cases), "|", "Expected: False")
    except Exception as inst:
        print(type(inst))
        print("Error Occurred: ", inst.args)

print("\n---------Additional Testing---------\n")
print("-----Personal Valid Cases-----")
for cases in personal_valid_cases:
    try:
        print("Output: ", valid_sentence(cases), "|", "Expected: True")
    except Exception as inst:
        print(type(inst))
        print("Error Occurred: ", inst.args)

print("-----Personal Invalid Cases-----")
for cases in personal_invalid_cases:
    try:
        print("Output: ", valid_sentence(cases), "|", "Expected: False")
    except Exception as inst:
        print(type(inst))
        print("Error Occurred: ", inst.args)

print("-----Type Error Cases-----")
for cases in type_error_cases:
    try:
        print("Output: ", valid_sentence(cases), "|", "Expected: None")
    except Exception as inst:
        print("Error Occurred: ", type(inst), "|", "Error Expected: Type Error")
        print("Error Description: ", inst.args[0])

print("-----Value Error Cases-----")
for cases in value_error_cases:
    try:
        print("Output: ", valid_sentence(cases), "|", "Expected: None")
    except Exception as inst:
        print("Error Occurred: ", type(inst), "|", "Error Expected: Value Error")
        print("Error Description: ", inst.args[0])
