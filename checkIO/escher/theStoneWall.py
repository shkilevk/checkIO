def stone_wall(wall: str) -> int:
  lWall = []
  count = 0
  for line in wall.split('\n'):
    if line:
      lWall.append([])
      lWall[count] = [sym for sym in line]
      count += 1

  sumZero = []
  for j in range(len(lWall[0])):
    temp = 0
    for i in range(count):
      if lWall[i][j] == '0':
        temp += 1
    sumZero.append(temp)
  return sumZero.index(max(sumZero))

  
print(stone_wall('''
##########
####0##0##
00##0###00
'''))


  
