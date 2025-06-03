def solve(word_given):
    words = word_given.split(' ')
    final_word = [word.capitalize() for word in words]
    return ' '.join( final_word)

if __name__ == '__main__':
