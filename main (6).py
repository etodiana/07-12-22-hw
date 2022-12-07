n = int(input())
mas = [[0]*n for i in range (n)]
i = 1 
x = 0 #строки
y = -1 #колонки
d_row = 0 #движение по строке (может принимать -1 движение вверх 0 на той же строке и 1 движение вниз по строке)
d_column = 1 #движение по колонкам (может принимать -1 движение влево 0 в той же колонке и 1 движение вправо)
lenght = len(str(n**2))
while i<= n**2:
    if 0<=x+d_row<n and 0<=y+d_column<n and mas[x+d_row][y+d_column]== 0:
        x+=d_row
        y+=d_column
        mas[x] [y] = i
        i+=1 
    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
                d_row = 0
                d_column = -1 
        elif d_column == -1:
                d_column = 0
                d_row = -1
        elif d_row == -1:
                d_row = 0
                d_column = -1
for row in mas:
    for elem in row:
        print(str(elem).rjust(lenght),end=' ')
print()
            
    
    