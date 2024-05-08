# data class (struct) that stores morse code info
# convert text to morse case
import sys

import morse_code_converter

input_text = input("Please enter text to turn into morse code: ")
converter = morse_code_converter.MorseCodeData(input_text)

while True:
    input_text = input("Please enter text to turn into morse code. Enter an empty string to exit: ")
    if len(input_text) == 0:
        sys.exit()
    else:
        converter.convert_string_to_morse_code(input_text)
