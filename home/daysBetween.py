import datetime

def day_diff(a: tuple, b: tuple) -> int:
  dt_a = datetime.date(a[0], a[1], a[2])
  dt_b = datetime.date(b[0], b[1], b[2])
  return abs((dt_a - dt_b).days)


print(day_diff((1982, 4, 19), (1982, 4, 22)))