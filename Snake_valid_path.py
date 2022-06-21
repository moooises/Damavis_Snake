import copy

def check_board(board):
    if len(board)!=2:
        raise ValueError(f"Board must have only two values.")
    if (board[1]<1 or board[1]>10 or board[0]<1 or board[0]>10):
        raise ValueError(f"Board values must be between 1 and 10. Both inclusive.")

def check_snake(snake,board):
    if (len(snake) <3 or len(snake)>7):
        raise ValueError(f"Snake must have between 3 and 7 positions. Both inclusive.")
    for s in snake:
        if len(s)!=2:
            raise ValueError(f"Position must have only to values.")
        if (s[1]<0 or s[1]>=board[1]):
            raise ValueError(f"Snake position can't be outside of the board.")

def check_depth(depth):
    if (depth<1 or depth>20):
        raise ValueError(f"Depth must be between 1 and 20. Both inclusive.")
       

def numberOfAvailableDifferentPaths(board, snake, depth):
    def move(board_matrix, snake, depth, dived, direction):

        tail=snake[-1]

        board_matrix[tail[1]][tail[0]]-=1
        snake.pop()
        head=snake[0]

        if(direction=='L'):
            snake.insert(0,[head[0]-1, head[1]])


        elif(direction=='R'):
            snake.insert(0,[head[0]+1, head[1]])


        elif(direction=='D'):
            snake.insert(0,[head[0], head[1]+1])


        elif(direction=='U'):
            snake.insert(0,[head[0], head[1]-1])

        head=snake[0]


        if(head[0]<0 or head[0]>=len(board_matrix[0]) or head[1]<0 or head[1]>=len(board_matrix)):
            return 0
        else:
            board_matrix[head[1]][head[0]]+=1
 
            if(board_matrix[head[1]][head[0]]==2):
                return 0

            elif (dived==depth):
                return 1
            else:
                
                L=move(copy.deepcopy(board_matrix) , snake.copy(), depth, dived+1,'L')
                R=move(copy.deepcopy(board_matrix) , snake.copy(), depth, dived+1,'R')
                D=move(copy.deepcopy(board_matrix) , snake.copy(), depth, dived+1,'D')
                U=move(copy.deepcopy(board_matrix) , snake.copy(), depth, dived+1,'U')

                return L+R+D+U
        

    def create_board(board):
        board_matrix_=[]
        for n in range(0,board[1]):
            board_matrix_.append([])
            board_matrix_[-1]=[0 for i in range(board[0])]
        return board_matrix_

    def place_snake(board_matrix_,snake):
        for s in snake:
            board_matrix_[s[1]][s[0]]=1
        return board_matrix_

    check_board(board)
    check_snake(snake, board)
    check_depth(depth)

    board_matrix=create_board(board)
    place_snake(board_matrix, snake)

    L=move(copy.deepcopy(board_matrix) , snake.copy(), depth, 1, 'L')
    R=move(copy.deepcopy(board_matrix) , snake.copy(), depth, 1, 'R')
    D=move(copy.deepcopy(board_matrix) , snake.copy(), depth, 1, 'D')
    U=move(copy.deepcopy(board_matrix) , snake.copy(), depth, 1, 'U')
    return L+R+D+U


#board=[4,3]
#snake=[[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]]
#depth=3

#board=[2,3]
#snake=[[0,2],[0,1],[0,0],[1,0],[1,1],[1,2]]
#depth=10

board=[10,10]
snake=[[5,5],[5,4],[4,4],[4,5]]
depth=4

result=numberOfAvailableDifferentPaths(board,snake,depth)
print(f"The number of distinct valid paths of length {depth} that the snake can make, modulo 10^9 + {result}")

