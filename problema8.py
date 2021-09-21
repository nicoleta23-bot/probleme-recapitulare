ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[11,12,13, 12,23,24,25,26,24,23,27,30,12,27,33,17,18,11,19,20,17,12,12,13]
print('temperatura medie : ', sum(t)/24)
print(max(t))
print(min(t))
print('ora cu temperatura maxima: ', ora[t.index(max(t))])
print('ora cu temperatura min: ', ora[t.index(min(t))])