from venv import create


def numberOfAvailableDifferentPaths(board, snake, depth):
    def move(board_matrix, snake, depth, dived, direction):
        tail=snake[-1]

        board_matrix[tail[1]][tail[0]]-=1
        #snake[-1]=snake[-2]
        snake.pop()
        head=snake[0]

        if(direction=='L'):
            snake.insert(0,[head[0], head[1]-1])


        elif(direction=='R'):
            snake.insert(0,[head[0], head[1]+1])


        elif(direction=='D'):
            snake.insert(0,[head[0]+1, head[1]])


        elif(direction=='U'):
            snake.insert(0,[head[0]-1, head[1]])

        


        print(len(board_matrix[0]))
        print(len(board_matrix))
        print(snake)
        if(head[0]<0 or head[0]>=len(board_matrix) or head[1]<0 or head[1]>=len(board_matrix[1])):
            return 0

        else:
            #print(head)
            board_matrix[head[1]][head[0]]+=1

            if(board_matrix[head[1]][head[0]]==2):
                return 0

            elif (dived==depth):
                for b in board_matrix:
                    print(b)
                return 1
            else:
                
                original_board=board_matrix
                original_snake=snake
                L=move(original_board , original_snake, depth, dived+1,'L')
                R=move(original_board , original_snake, depth, dived+1,'R')
                D=move(original_board , original_snake, depth, dived+1,'D')
                U=move(original_board , original_snake, depth, dived+1,'U')

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

    def dive(board_matrix, snake, depth):
        original_board=board_matrix
        original_snake=snake
        L=move(original_board , original_snake, 3, 1, 'L')
        R=move(original_board , original_snake, 3, 1, 'R')
        D=move(original_board , original_snake, 3, 1, 'D')
        U=move(original_board , original_snake, 3, 1, 'U')
        return L+R+D+U

    board_matrix=create_board(board)
    place_snake(board_matrix, snake)
    for b in board_matrix:
        print(b)
    result=dive(board_matrix, snake, depth)

    print("Resultados:")
    print(result)



board=[4,3]
snake=[[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]]
print(snake)
depth=3
result=numberOfAvailableDifferentPaths(board,snake,depth)