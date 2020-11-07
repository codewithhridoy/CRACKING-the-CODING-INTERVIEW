# Determine whether or not a given string contains no duplicate characters.

def contains_no_duplicates(string):
  letters = {}
  for letter in string:
    if letter in letters:
      return 'Not Unique'
    letters[letter] = True
  return 'Unique'

if __name__ == "__main__":
  #import sys
  #print(contains_no_duplicates(sys.argv[-1]))
    print(contains_no_duplicates('amivatkhai'))
