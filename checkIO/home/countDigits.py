def count_digits(text: str) -> int:
  all_digits = ''
  num = ''

  for chr in text:
    if chr.isdigit():
      num += chr
    else:
      if num != '':
        all_digits += num
        num = ''
  if num != '':
    all_digits += num
  
  return len(all_digits)


print(count_digits('5 plus 6 is'))