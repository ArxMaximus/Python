from functools import reduce


l = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
     {'name': 'Nikolas', 'final': 98}]


print(reduce(lambda s, v: v if v['final'] > s['final'] else s, l))
print(reduce(lambda s, v: v if v['final'] < s['final'] else s, l))