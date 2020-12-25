import math

def line_equation(a: tuple, b: tuple) -> tuple:
  """По координатам двух точек, вычисляем коэффициенты k и m прямой"""
  if (b[0] - a[0]) == 0:
    return (0, 0)
  k = (b[1] - a[1]) / (b[0] - a[0])     # k = (y2-y1)/(x2-x1)
  m = b[1] - k * b[0]     # b = y2 - k * x2
  return (k, m)


def max_col_lines(line: list) -> tuple:
  """"""

  setLine = set(line)
  dictLine = {}

  for i in setLine:
    count = line.count(i)
    dictLine[i] = count
  maxV = max(dictLine.values())
  if maxV > 1:
    
    for k, v in dictLine.items():
      if maxV == v:
        return k
  else:

    maxK = 0
    indx = 0
    for j, i in enumerate(line):
      if i[0] > maxK:
        maxK = i[0]
        indx = j
    return line[indx]

  print(line)
  for i in line:
    print(distance_to_line(i))


def distance_to_line(k_m: tuple) -> float:
  """Вычисляем расстояние от начала координат до прямой"""

  d = abs(k_m[1]) / math.sqrt(pow(k_m[0], 2) + 1)   # d = |Ax1 + By2 + C| / sqrt(A*A + B*B)
  return d


def wild_dogs(coords: list):
  k_m = []

  # Находим коэффициенты k и m для всех возможных пар точек и помещаем в k_m
  for i in range(len(coords)):
    j = i + 1
    while(j < len(coords)):
      k_m.append(line_equation(coords[i], coords[j]))
      j +=1
  
  max_col_lines(k_m)
  d = distance_to_line(max_col_lines(k_m))

  if type(d) == int():
    return d
  else:
    return round(d, 2)


print(wild_dogs([(7, 122), (8, 139), (9, 156), (10, 173), (11, 190), (-100, 1)]))
print(wild_dogs([(6, -0.5), (3, -5), (1, -20)]))
print(wild_dogs([(10, 10), (13, 13), (21, 18)]))
print(wild_dogs([(2,20), (3,25), (10,60), (20,110), (1,-17), (540,-11)]))
print(wild_dogs([(10,23), (4,5), (7,14), (10,110)]))



# def wild_dogs(coords):
#     from itertools import combinations
#     result = []
#     for (x0, y0), (x1, y1) in combinations(coords, 2):       
#         A, B, C = y0-y1, x1-x0, y0*(x0-x1)-x0*(y0-y1)        
#         distance = abs(C)/(A**2+B**2)**0.5                   
#         result += [(distance, (1, B/A, C/A) if A else (A/B, 1, C/B))]
#     distance, *_ = max(result, key=lambda x: (result.count(x), -x[0]))
#     return round(distance, 2)

