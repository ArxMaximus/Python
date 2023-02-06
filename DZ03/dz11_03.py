l = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
     {'name': 'Nikolas', 'final': 98}]

l.sort(key=lambda a: a['name'])
print(l)
l.sort(key=lambda a: a['final'], reverse=True)
print(l)
