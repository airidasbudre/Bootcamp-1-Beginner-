import math
def paint_calc(height, wide, cover):
    x = (height * wide)/ cover
    print(math.floor(x))
coverage = 5
x = 0

h = int(input('Height'))
w = int(input('Wide'))
paint_calc(height=h, wide = w, cover=coverage)    
