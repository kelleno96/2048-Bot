import numpy as np
import tensorflow as tf

class environment:
    def __init__(self):
        print("Making game")
        self.board = np.zeros([4,4], dtype=np.uint)
        self.add_random_tile()

    def __str__(self):
        return str(self.board) + "\n"

    def move(self, action):
        # action = 0 for left, 1 up, 2 right, 3 down
        rotated_board = np.rot90(self.board, action)
        cols = [rotated_board[i, :] for i in range(4)]
        new_board, rewards = zip(*np.array([self.move_left(col) for col in cols]))
        reward = np.sum(rewards)
        new_board = np.array(new_board)
        # print("New board: " + str(new_board))
        # print(np.rot90(new_board, -action))
        return np.rot90(new_board, -action), reward

    def is_done(self):
        return all([(self.move(a)[0]==self.board).all() for a in range(4)])

    def step(self, action):
        # Return new board state, reward for the step, isDone
        done = self.is_done()
        if not done:
            new_board, reward = self.move(action)
            if not (new_board == self.board).all():
                self.board = new_board.copy()
                self.add_random_tile()
        else:
            reward = 0
        return self.board, reward, done


    """
    Merging:
    want to combine elements in a row/col with adjacent or non-adjacent elements in the same row/col with the same value
    as long as only zeros are between them.
    
    
    """

    def move_left(self, col):
        # Slide tiles left
        new_col = np.zeros((4), dtype=np.uint)
        j = 0
        previous = None
        reward = 0
        for i in range(col.size):
            if col[i] != 0:
                if previous == None:
                    previous = col[i]
                else:
                    if previous == col[i]:
                        new_col[j] = 2*col[i]
                        reward += 2*col[i]
                        j+=1
                        previous = None
                    else:
                        new_col[j] = previous
                        j+=1
                        previous = col[i]
        if previous!=None:
            new_col[j] = previous
        return new_col, reward

    def add_random_tile(self):
        row = np.random.randint(0, 4)
        col = np.random.randint(0, 4)
        if (self.board==0).any():
            while(self.board[row, col] != 0):
                row = np.random.randint(0, 4)
                col = np.random.randint(0, 4)
            self.board[row, col] = 2 + 2*np.random.randint(0,2)

    def print_board(self):
        print(self.board)

    def testing_step(self):
        self.add_random_tile()
        self.print_board()


def main():
    env = environment()
    mode = "User"
    if mode == "User":
        key = []
        score = 0
        print(env)
        while key != 'q':
            key = input("Direction: ")
            if key == 'w':
                action = 1
            if key == 'd':
                action = 2
            if key == 's':
                action = 3
            if key == 'a':
                action = 0
            board, reward, done = env.step(action)
            if(done):
                print("You lose")
                print(score)
                break
            score+=reward
            print(board)
            print(score)
    elif mode == "Learning":
        # Implement code to learn how to play the game here
        print("Learning...")



if __name__ == "__main__":
    main()