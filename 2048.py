import numpy as np


class environment:
    def __init__(self):
        print("Making game")
        self.board = np.zeros([4,4], dtype=np.uint)
        self.lock = np.zeros([4,4], dtype=np.uint)
    def __str__(self):
        return str(self.board) + "\n"

    def step(self, action):
        # Perform action
        # Return next board state (Sprime), Reward, Done
        pass

    """
    Merging:
    want to combine elements in a row/col with adjacent or non-adjacent elements in the same row/col with the same value
    as long as only zeros are between them.
    
    
    """
    def move_up(self):
        # Slide tiles up
        for col in range(0, 4):
            for row in range(1, 4):
                for i in range(4-row):
                    if self.board[row, col] == self.board[row+i, col] and np.sum(self.board[row+1:row+i-1, col]) == 0 and self.lock[row, col] == 0 and self.lock[row+i, col] == 0:
                        self.lock[row, col] = 1
                        self.lock[row+i, col] = 1
                    # if self.board[row - i, col] == self.board[row, col] and np.sum(self.board[i:row, col]) == 0:
                    #     self.board[row - 1, col] *= 2
                    #     self.board[row, col] = 0
                # if self.board[row, col]!= 0:
                #     if self.board[row-1, col] == 0:
                #         self.board[row-1, col] = self.board[row, col]


        return self.board
    def move_down(self):
        # Slide tiles down
        pass
    def move_left(self):
        # Slide tiles left
        pass
    def move_right(self):
        # Slide tiles right
        pass

    def add_random_tile(self):
        row = np.random.randint(0, 4)
        col = np.random.randint(0, 4)
        while(self.board[row, col] != 0):
            row = np.random.randint(0, 4)
            col = np.random.randint(0, 4)
        self.board[row, col] = 2

    def print_board(self):
        print(self.board)

    def testing_step(self):
        self.add_random_tile()
        self.print_board()


def main():
    env = environment()
    env.board = np.array([[2, 2, 4, 8],
                         [2, 0, 2, 4],
                         [2, 2, 0, 2],
                         [2, 2, 2, 0]], dtype=np.uint)
    print(env)
    env.move_up()
    print(env)
    print(str(env.lock))



if __name__ == "__main__":
    main()