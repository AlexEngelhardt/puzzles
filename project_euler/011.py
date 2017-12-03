f = open("011.txt", "r")

matrix = []

row=0
for line in f.readlines():
    matrix.append(line.rstrip("\n").split(" "))
    row +=1 

nrow = len(matrix)
ncol = len(matrix[0])

for row in xrange(nrow):  # row in 0:19
    for col in xrange(ncol):
        matrix[row][col] = int(matrix[row][col])

maxprod = 0
for row in xrange(nrow):  # row in 0:19
    for col in xrange(ncol):
        if ncol - col >= 4:  # Falls nach rechts noch Platz ist
            right = matrix[row][col] * matrix[row][col+1] * matrix[row][col+2] * matrix[row][col+3]
            if right > maxprod:
                maxprod = right
        if nrow - row >= 4:  # Falls nach unten -"-
            down = matrix[row][col] * matrix[row+1][col] * matrix[row+2][col] * matrix[row+3][col]
            if down > maxprod:
                maxprod = down

        if nrow-row>=4 and ncol-col>=4:  # Falls r.u. diagonal -"-
            dr_diag = matrix[row][col] * matrix[row+1][col+1] * matrix[row+2][col+2] * matrix[row+3][col+3]
            if dr_diag > maxprod:
                maxprod = dr_diag

        if nrow-row>=4 and col>=3:
            dl_diag = matrix[row][col] * matrix[row+1][col-1] * matrix[row+2][col-2] * matrix[row+3][col-3]
            if dl_diag > maxprod:
                maxprod = dl_diag

print maxprod

            
        
