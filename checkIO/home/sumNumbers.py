def sum_numbers(text: str) -> int:
  return sum([int(i) for i in text.split() if i.isdigit()])


print(sum_numbers('12 dsf 3s'))
