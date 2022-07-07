def TripleStepTopDown(n, memo):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    if memo[n] == 0:
        memo[n]= TripleStepTopDown(n-1, memo) + TripleStepTopDown(n-2, memo) + TripleStepTopDown(n-3, memo)

    return memo[n]

def TripleStepBottomUp(n):
    if n < 0:
        return 0
    
    one=1
    two=2
    three=4
    if n==1:
        return one
    elif n==2:
        return two
    elif n==3:
        return three
    
    for i in range(4, n):
        new=one+two+three
        one=two
        two=three
        three=new

    return one+two+three
        
        
def StiarCase(n):
    return TripleStepTopDown(n, [0]*(n+1))


def boardGame(N, M, offLimits):
    if N <=0 or M <= 0:
        return 0
    
    board = [[0]*N for _ in range(M)]
    for i in range(M):
        if (0, i) not in offLimits:
            board[0][i] = 1
    for i in range(N):
        if (i, 0) not in offLimits:
            board[i][0] = 1

    for row in range(1, N):
        for col in range(1, M):
            if (row, col) in offLimits:
                continue            
            board[row][col] = board[row][col-1]+board[row-1][col]

    return board[N-1][M-1]


    
    
if __name__ == "__main__":
    print(StiarCase(40))
    print(TripleStepBottomUp(6))
