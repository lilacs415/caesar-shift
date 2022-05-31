import pytest


val_to_let = lambda letter_vals: ''.join([chr(val) for val in letter_vals])


def caesar_shift(words, shift):
    """
    where words is a list of strings of text to shift
    """
    shift = shift % 26
    numbers = []
    for word in words:
        if word.isalpha():
            for letter in word:
                if letter.islower():
                    if ord(letter) + shift > 122:
                        numbers.append(96 + (ord(letter) + shift) - 122)
                    else:
                        numbers.append(ord(letter) + shift)
                else:
                    if ord(letter) + shift > 90:
                        numbers.append(64 + (ord(letter) + shift) - 90)
                    else:
                        numbers.append(ord(letter) + shift)
            numbers.append(32)
    return val_to_let(numbers).strip() if numbers else "Please input only words into the shifter."


def test_answer():
    assert caesar_shift(['hello', 'world'], 2) == 'jgnnq yqtnf'
    assert caesar_shift(['xyz'], 2) == 'zab'
    assert caesar_shift(['XYZ'], 2) == 'ZAB'
    assert caesar_shift(['ABC'], 2) == 'CDE'
    assert caesar_shift(['AbCdEf'], 2) == 'CdEfGh'
    assert caesar_shift(['123'], 2) == "Please input only words into the shifter."


if __name__ == "__main__":
    def repl():
        """
        Creates a REPL that the user can interact with.
        """
        print('To use this tool, please enter an "encode" or "decode" command, then your text, then the shift number.')
        user_input = input('input: ')
        while user_input != 'exit':
            raw_inputs = user_input.split()
            inputs = [raw_inputs[0], raw_inputs[1:-1], raw_inputs[-1]]
            if inputs[0] == 'encode':
                if inputs[-1].isnumeric() and len(inputs) == 3:
                    print('output: ', caesar_shift(inputs[1], int(inputs[2])))
                else:
                    print('Error: please provide a shift number after the text you would like to encode.')
            elif inputs[0] == 'decode':
                print("output: ", caesar_shift(inputs[1], 26 - int(inputs[2])))
            else:
                print('Error: please precede your text with an "encode" or "decode" command.')
            user_input = input('input: ')
        return
    repl()