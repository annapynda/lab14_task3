class Board:
    """
    class representing board
    """
    def __init__(self):
        """
        initializes elements
        """
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_move = None

    def check_haveplace(self):
        """

        :return: number of free places
        """
        counter = 0
        for i in self.board:
            for j in i:
                if j == 0:
                    counter += 1
        return counter

    def check_the_Board(self):
        """
        :return: the winner or True if game is continuing
        """

        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 'X' or self.board[0][0] == self.board[0][1] == self.board[0][2] == 'O':
            if self.board[0][0] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == "X" or self.board[1][0] == self.board[1][1] == self.board[1][2]== 'O':
            if self.board[1][0] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == "X" or self.board[2][0] == self.board[2][1] == self.board[2][2]=='O':
            if self.board[2][0] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        elif self.board[1][0] == self.board[2][0] == self.board[0][0] == 'X' or self.board[1][0] == self.board[2][0] == self.board[0][0]== 'O':
            if self.board[0][0] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'X' or self.board[0][1] == self.board[1][1] == self.board[2][1] == 'O':
            if self.board[0][1] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'X' or self.board[0][2] == self.board[1][2] == self.board[2][2]=='O':
            if self.board[0][2] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X' or self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':
            if self.board[0][0] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X' or self.board[0][2] == self.board[1][1] == self.board[2][0] =='O':
            if self.board[0][2] == 'X':
                return 'winner is first player'
            else:
                return 'winner is second player'

        else:
            if self.check_haveplace() == 0:
                return 'EQUITY noone won'

        return True






    def put_move(self, player, coodinates):
        """

        :param player:  X or O
        :param coodinates: the coordinates for move
        puts the move onto the board
        """
        if self.board[coodinates[0]][coodinates[1]] == 0:
            if player == 1:
                self.board[coodinates[0]][coodinates[1]] = 'X'
            else:
                self.board[coodinates[0]][coodinates[1]] = 'O'

            self.last_move = [player, coodinates]
        else:
            raise IndexError("This place is not free")





    def __str__(self):
        """
        :return: string representation of board
        """

        l = ''
        for i in self.board:
            for j in i:
                l += str(j) + ' '
            l += '\n'
        return l











