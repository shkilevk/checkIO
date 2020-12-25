nodes = [['Y', 0, 0, 0,'C'],
        [ 0,  0, 0, 0,  0],
        [ 0,  0, 0, 0,  0],
        ['M', 0, 0, 0,'S']]

reachables = {}
path = []

for i in range(len(nodes)):
  if 'Y' in nodes[i]:
    reachables['Y'] = [i, nodes[i].index('Y')]
    break

for i in range(len(nodes)):
  if 'M' in nodes[i]:
    reachables['M'] = [i, nodes[i].index('M')]
    break

for i in range(len(nodes)):
  if 'C' in nodes[i]:
    reachables['C'] = [i, nodes[i].index('C')]
    break

for i in range(len(nodes)):
  if 'S' in nodes[i]:
    reachables['S'] = [i, nodes[i].index('S')]
    break

for node in reachables.keys():
  if node == 'Y':
    continue
  path.append(max(abs((reachables['Y'])[0] - (reachables[node])[0]), abs((reachables['Y'])[1] - (reachables[node])[1])))

print(sum(path))
