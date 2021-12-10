#x*2 = (x-1)*2 +x +(x-1)
def printSquares(n):
    square=0;
    prev_x=0;
    for x in range (0,n):
        square=(square+x+prev_x)
        print(square)
        prev_x=x
n=int(input(  ));
printSquares(n);