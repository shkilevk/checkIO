"""
In a given string you should reverse every word, but the words should stay in
their places.
"""

def backward_string_by_word(text: str) -> str:
  result = ''
  temp = ''
  for sym in text:
    if sym != ' ':
      temp += sym
    elif temp == '':
      result += ' '
    else:
      result += temp[::-1]
      result += ' '
      temp = ''
  if temp != '':
    return result + temp[::-1]
  else:
    return result

print(backward_string_by_word('') == '')
print(backward_string_by_word('world') == 'dlrow')
print(backward_string_by_word('hello world') == 'olleh dlrow')
print(backward_string_by_word('hello   world') == 'olleh   dlrow')
print(backward_string_by_word('welcome to a game') == 'emoclew ot a emag')




