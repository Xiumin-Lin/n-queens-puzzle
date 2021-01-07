class Queen:

    value = 1   # the value that represents the queen in the chessboard

    def __init__(self, y, x, board_size, board):
        self.y = y  # queen's row index
        self.x = x  # queen's column index
        self.board_size = board_size
        self.board = board

    # A function that checks if the queen can attack another queen
    # Warning, this function only checks the right, bottom, bottom left and right diagonal boxes of the queen
    # Use this function with a loop that runs from left to right and then up and down the board.
    def can_attack(self):
        if (self.can_attack_right()
                or self.can_attack_down()
                or self.can_attack_diag_down_left()
                or self.can_attack_diag_down_right()):
            return True
        return False

    # A function that checks if the queen can attack (another queen) to her right
    def can_attack_right(self):
        for i in range(self.x + 1, self.board_size):
            if (self.board[self.y][i] == Queen.value):
                return True
        return False

    # A function that checks if the queen can attack down
    def can_attack_down(self):
        for i in range(self.y + 1, self.board_size):
            if (self.board[i][self.x] == Queen.value):
                return True
        return False

    # A function that checks if the queen can attack at her bottom left diagonal
    def can_attack_diag_down_left(self):
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.x - i) >= 0):
            newY = self.y + i
            newX = self.x - i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False

    # A function that checks if the queen can attack at her bottom right diagonal
    def can_attack_diag_down_right(self):
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.board_size - (self.x + i)) > 0):
            newY = self.y + i
            newX = self.x + i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False

    # Une fonction qui vérifie si l'emplacement de la reine n'est pas attaqué
    # Similaire à la function can_attack(self)
    # Attention, cette fonction ne vérifie que les cases en diagonal haut gauche et en diagonal bas gauche de la reine
    # Utilisez cette fonction avec une boucle qui parcourt le board de haut en bas et puis de gauche à droite
    def can_be_placed(self):
        if (self.can_attack_diag_up_left() or self.can_attack_diag_down_left()):
            return False
        return True

    # # Une fonction qui vérifie si la reine peut attaquer (une autre reine) à sa gauche
    # def can_attack_left(self):
    #     for i in range(self.x):
    #         if (self.board[self.y][i] == Queen.value):
    #             return True
    #     return False

    # Une fonction qui vérifie si la reine peut attaquer à sa diagonale haut gauche
    def can_attack_diag_up_left(self):
        i = 1
        while((self.y - i) >= 0 and (self.x - i) >= 0):
            newY = self.y - i
            newX = self.x - i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False
