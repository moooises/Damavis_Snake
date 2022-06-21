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

    def collision(snake):
        head = snake[0]
        for n in snake[1:]:
           if n[0]==head[0] and n[1]==head[1]:
            return True

        return False 

    def step_back(snake, prev_tails):
        snake.pop(0)
        snake.insert(len(snake),prev_tails[0])
        prev_tails.pop(0)

    def move(snake, prev_tails, board, depth, dived, direction):

        prev_tails.insert(0,snake.pop())

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

        if(head[0]<0 or head[1]<0 or head[0]==board[0] or head[1]==board[1] or collision(snake)):
            return 0
        else:

            if (dived==depth):
                return 1

            else:
                L=move(snake, prev_tails, board, depth, dived+1,'L')
                step_back(snake,prev_tails)
                R=move(snake, prev_tails, board, depth, dived+1,'R')
                step_back(snake,prev_tails)
                D=move(snake, prev_tails, board, depth, dived+1,'D')
                step_back(snake,prev_tails)
                U=move(snake, prev_tails, board, depth, dived+1,'U')
                step_back(snake,prev_tails)

                return L+R+D+U
        
    

    check_board(board)
    check_snake(snake, board)
    check_depth(depth)

    prev_tails=[]

    L=move(snake, prev_tails, board, depth, 1, 'L')
    step_back(snake,prev_tails)
    R=move(snake, prev_tails, board, depth, 1, 'R')
    step_back(snake,prev_tails)
    D=move(snake, prev_tails, board, depth, 1, 'D')
    step_back(snake,prev_tails)
    U=move(snake, prev_tails, board, depth, 1, 'U')
    step_back(snake,prev_tails)
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
