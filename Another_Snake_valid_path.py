import copy

def numberOfAvailableDifferentPaths(board, snake, depth):

    def collision(snake):
        head = snake[0]
        for n in snake[1:]:
           if n[0]==head[0] and n[1]==head[1]:
            return True

        return False 

    def move_left(snake, prev_tails):
        prev_tails.insert(0,snake.pop())
        snake.insert([snake[0][0]-1,snake[0][1]])

        if (snake[0][0]<0 or )
        move()

    def move_right(snake, prev_tails):
        prev_tails.insert(0,snake.pop())
        snake.insert([snake[0][0]+1,snake[0][1]])

    def move_up(snake, prev_tails):
        prev_tails.insert(0,snake.pop())
        snake.insert([snake[0][0],snake[0][1]-1])
    
    def move_down(snake, prev_tails):
        prev_tails.insert(0,snake.pop())
        snake.insert([snake[0][0],snake[0][1]+1])

    def move(board, snake, prev_tails ,depth, dived):

        if (dived >depth):
             return 1

        move_left(board,snake,prev_tails, depth, dived+1)


    prev_tails=[]
    valid_paths=0
    dived=0

    while(dived<=depth):

        

    

board=[4,3]
snake=[[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]]
depth=3

#board=[2,3]
#snake=[[0,2],[0,1],[0,0],[1,0],[1,1],[1,2]]
#depth=10

#board=[10,10]
#snake=[[5,5],[5,4],[4,4],[4,5]]
#depth=4


result=numberOfAvailableDifferentPaths(board,snake,depth)
print("Resultados:")
print(result)