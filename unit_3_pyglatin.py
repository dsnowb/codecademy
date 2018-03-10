original = raw_input('Enter a word:')

print original[1:] + original[0] + 'ay' if len(original) and original.isalpha() else 'empty'
