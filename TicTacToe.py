from textwrap import wrap
class Symbol:
    x = "X"
    o = "O"
    empty = "_"

class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.field = [[Symbol.empty for _i in range(size)] for _j in range(size)]
        self.finished = False
        self.impossible = False
        self.current_move = Symbol.x

    @staticmethod
    def len(_list, value):
        return len([x for x in _list if x == value])

    def print_state(self):
        print("-" * (self.size * 2 + 3))
        for i in self.field:
            row = f'| {str.join(" ", i)} |'
            print(row)
        print("-" * (self.size * 2 + 3))

    def input_cells(self):
        inputted_cells = input("Enter cells: ")[:self.size ** 2]
        self.field = [wrap(s, 1) for s in wrap(inputted_cells, self.size)]
        self.impossible = abs(self.len(inputted_cells, Symbol.x) - self.len(inputted_cells, Symbol.o)) > 1
        self.finished = self.is_finished()

    def is_finished(self):
        return all(str(r) != Symbol.empty for v in self.field for r in v)

    def check_state(self):
        x_win = False
        o_win = False

        
        for i in range(self.size):
            row = self.field[i]
            column = [row[i] for row in self.field]
            x_win = x_win or self.check_win(row, Symbol.x) or self.check_win(column, Symbol.x)
            o_win = o_win or self.check_win(row, Symbol.o) or self.check_win(column, Symbol.o)

           
        diag_1 = [self.field[i][i] for i in range(self.size)]
        diag_2 = [self.field[self.size - 1 - i][i] for i in range(self.size - 1, -1, -1)]
        x_win = x_win or self.check_win(diag_1, Symbol.x) or self.check_win(diag_2, Symbol.x)
        o_win = o_win or self.check_win(diag_1, Symbol.o) or self.check_win(diag_2, Symbol.o)

        return [x_win, o_win]

    def check_win(self, line, symbol):
        return self.len(line, symbol) == self.size

    def get_result(self):
        x_win, o_win = self.check_state()
        if self.impossible or (x_win and o_win):
            print("Impossible")
        elif x_win:
            print("X wins")
        elif o_win:
            print("O wins")
        elif self.finished:
            print("Draw")

    def next_move(self):
        coordinates = [x for x in input("Enter the coordinates: ").split(" ")]
        if len(coordinates) != 2 or (not coordinates[0].isdigit() or not coordinates[1].isdigit()):
            print("You should enter numbers!")
            return self.next_move()

        column = int(coordinates[0]) - 1
        row = self.size - int(coordinates[1])

        if not 0 <= row <= self.size - 1 or not 0 <= column <= self.size - 1:
            print("Coordinates should be from 1 to 3!")
            return self.next_move()

        if self.field[row][column] != Symbol.empty:
            print("This cell is occupied! Choose another one!")
            return self.next_move()

        self.field[row][column] = self.current_move
        self.print_state()

    def run(self):
        self.print_state()
        while not self.finished:
            self.next_move()
            self.check_if_finished()
            self.change_move()

    def change_move(self):
        self.current_move = Symbol.x if self.current_move == Symbol.o else Symbol.o

    def check_if_finished(self):
        if self.is_finished() or any(self.check_state()):
            self.finished = True
            self.get_result()

# Set the size of 3
game = TicTacToe(3)
game.run()
