zi=['L', 'Ma', 'Mi', 'J', 'Vi', 'S', 'D']
print(zi)
v=[200,400,430,250,500,340,300]
print('venitul saptaminal: ', sum(v))
m=(sum(v))/7
print(m)
print('ziua cu venitul maxim: ', zi[v.index(max(v))])
print('ziua cu venitul minim: ', zi[v.index(min(v))])
  
