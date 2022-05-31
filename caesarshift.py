import pytest
# num_to_val = lambda string: [ord(char) - 96 for char in string]
def num_to_val(string):
    if string.isalpha():
        return [ord(char) - 96 for char in string]
# val_to_num = lambda letter_vals: ''.join([chr(val + 96) for val in letter_vals if val != 32])

def val_to_num(letter_vals):
    return ''.join([chr(val + 96) for val in letter_vals if val != 32])
    
def caesar_shift(words, shift):
    """
    where words is a list of strings of text to shift
    """
    shifted = []
    for word in words:
        nums = num_to_val(word)
        intermediate = [num + shift for num in nums]
        shifted.append(val_to_num(intermediate))
    return shifted


def test_answer():
    assert caesar_shift(['hello', 'world'], 2) == ['jgnnq', 'yqtnf']
    # assert caesar_shift(['xyz'], 2) == ['zab']
    assert caesar_shift(['ABC'], 2) == ['CDE']
    assert caesar_shift(['AbCdEf'], 2) == ['CdEfGh']

if __name__ == "__main__":
    def repl():
        """
        Creates a REPL that the user can interact with.
        """
        print('To use this tool, please enter an "encode" or "decode" command, then your text, then if applicable the shift number.')
        user_input = input('input: ')
        while user_input != 'exit.':
            raw_inputs = user_input.split()
            inputs = [raw_inputs[0], raw_inputs[1:-1], raw_inputs[-1]]
            if inputs[0] == 'encode':
                if inputs[-1].isnumeric():
                    print('output: ', ' '.join(caesar_shift(inputs[1], int(inputs[2]))))
                else:
                    print('Error: please provide a shift number after the text you would like to encode.')
            elif inputs[0] == 'decode':
                # TODO: make this decode
                print("output: ", caesar_shift(inputs[0], int(inputs[1])))
            else:
                print('Error: please precede your text with an "encode" or "decode" command.')
            user_input = input('input: ')
        return
    repl()