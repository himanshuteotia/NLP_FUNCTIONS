# -*- coding: utf-8 -*-
from nltk.corpus import wordnet
import re

old_word = 'finalllyyy'

def remove_repeated_characters_single_token(old_word):
    step = 1
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    multiple_repeat_pattern = re.compile(r'\b(\w+)(\s+\1)+\b')
    multiple_match_substitution = r'\1'
    old_word = multiple_repeat_pattern.sub(multiple_match_substitution,old_word)
    print(old_word)
    while True:
        # check for semantically correct word
        if wordnet.synsets(old_word):
            print("Final correct word:", old_word)
            return old_word
        # remove one repeated character
        new_word = repeat_pattern.sub(match_substitution,old_word)
        if new_word != old_word:
            print('Step: {} Word: {}'.format(step, new_word))
            step += 1 # update step
            # update old word to last substituted state
            old_word = new_word
            continue
        else:
            print("Final word:", new_word)
            return new_word
    
print(remove_repeated_characters_single_token("sexxuallysexxually"))


def remove_repeated_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
    correct_tokens = [replace(word) for word in tokens]
    return correct_tokens


print(remove_repeated_characters(["hellloo","finalllly","we","can","extend"]))