#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split the string based on the punctuation marks: ".", "!", or "?"
        sentences = re.split(r'[.!?]', self._value)
        # Remove any empty strings from the list
        filtered_sentences = [s.strip() for s in sentences if s.strip()]
        return len(filtered_sentences)

string = MyString()
string.value = "This is a string! It has three sentences. Right?"

print(string.is_sentence())       # False
print(string.is_question())       # True
print(string.is_exclamation())    # False
print(string.count_sentences())   # 3
