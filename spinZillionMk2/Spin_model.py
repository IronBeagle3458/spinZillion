class Spin_Model:
    def __init__(self) -> None:
        #Black - 0, Blue - 1, Red - 2, Orange - 3, Yellow - 4, Green - 5
        self.row_0 = [0, 1, 1, 1, 1]
        self.row_1 = [5, 5, 5, 5]
        self.row_2 = [0, 4, 4, 4, 4]
        self.row_3 = [0, 3, 3, 3, 3]
        self.row_4 = [2, 2, 2, 2]
        #1 = up, 0 = down
        self.up = 1
        self.win = False
        self.moves = 1

    def set_row(self, row_num, new_array):
        if row_num == 0:
            self.row_0 = new_array
        elif row_num == 1:
            self.row_1 = new_array
        elif row_num == 2:
            self.row_2 = new_array
        elif row_num == 3:
            self.row_3 = new_array
        elif row_num == 4:
            self.row_4 = new_array

    def get_row(self, row_num):
        if row_num == 0:
            return self.row_0
        elif row_num == 1:
            return self.row_1
        elif row_num == 2:
            return self.row_2
        elif row_num == 3:
            return self.row_3
        elif row_num == 4:
            return self.row_4

    #level - 0 = top - 2 = bottom
    #direction - 0 = clockwise - 1 = counterclockwise
    def move(self, level, direction):
        row_buffer = self.row_0.copy()
        if direction == 0:
            self.row_0.pop(0 + self.up + level)
            self.row_0.pop(0 + self.up + level)
            self.row_0.insert(0 + self.up + level, self.row_1[0 + level])
            self.row_0.insert(1 + self.up + level, self.row_1[1 + level])
            self.row_1.pop(0 + level)
            self.row_1.pop(0 + level)
            self.row_1.insert(0 + level, self.row_2[0 + self.up + level])
            self.row_1.insert(1 + level, self.row_2[1 + self.up + level])
            self.row_2.pop(0 + self.up + level)
            self.row_2.pop(0 + self.up + level)
            self.row_2.insert(0 + self.up + level, self.row_3[0 + self.up + level])
            self.row_2.insert(1 + self.up + level, self.row_3[1 + self.up + level])
            self.row_3.pop(0 + self.up + level)
            self.row_3.pop(0 + self.up + level)
            self.row_3.insert(0 + self.up + level, self.row_4[0 + level])
            self.row_3.insert(1 + self.up + level, self.row_4[1 + level])
            self.row_4.pop(0 + level)
            self.row_4.pop(0 + level)
            self.row_4.insert(0 + level, row_buffer[0 + self.up + level])
            self.row_4.insert(1 + level, row_buffer[1 + self.up + level])
        else:
            self.row_0.pop(0 + self.up + level)
            self.row_0.pop(0 + self.up + level)
            self.row_0.insert(0 + self.up + level, self.row_4[0 + level])
            self.row_0.insert(1 + self.up + level, self.row_4[1 + level])
            self.row_4.pop(0 + level)
            self.row_4.pop(0 + level)
            self.row_4.insert(0 + level, self.row_3[0 + self.up + level])
            self.row_4.insert(1 + level, self.row_3[1 + self.up + level])
            self.row_3.pop(0 + self.up + level)
            self.row_3.pop(0 + self.up + level)
            self.row_3.insert(0 + self.up + level, self.row_2[0 + self.up + level])
            self.row_3.insert(1 + self.up + level, self.row_2[1 + self.up + level])
            self.row_2.pop(0 + self.up + level)
            self.row_2.pop(0 + self.up + level)
            self.row_2.insert(0 + self.up + level, self.row_1[0 + level])
            self.row_2.insert(1 + self.up + level, self.row_1[1 + level])
            self.row_1.pop(0 + level)
            self.row_1.pop(0 + level)
            self.row_1.insert(0 + level, row_buffer[0 + self.up + level])
            self.row_1.insert(1 + level, row_buffer[1 + self.up + level])

    def shift(self):
        if self.up == 1:
            self.up = 0
        else:
            self.up = 1

    def display_text(self):
        print(self.row_0)
        print(self.row_1)
        print(self.row_2)
        print(self.row_3)
        print(self.row_4)

    def win_check(self, move_cnt):
        if self.row_0[1] == self.row_0[2] and self.row_0[3] == self.row_0[4] and self.row_0[1] == self.row_0[4]:
            if self.row_2[1] == self.row_2[2] and self.row_2[3] == self.row_2[4] and self.row_2[1] == self.row_2[4]:
                if self.row_3[1] == self.row_3[2] and self.row_3[3] == self.row_3[4] and self.row_3[1] == self.row_3[4]:
                    if self.row_1[0] == self.row_1[1] and self.row_1[2] == self.row_1[3] and self.row_1[0] == self.row_1[3]:
                        if self.row_4[0] == self.row_4[1] and self.row_4[2] == self.row_4[3] and self.row_4[0] == self.row_4[3]:
                            self.win = True
                            self.moves = move_cnt
                            return True
        return False

    def score_game(self):
        score = 0
        if self.row_0[0] == 0:
            score += 1
        if self.row_0[1] == self.row_0[2]:
            score += 1
        if self.row_0[2] == self.row_0[3]:
            score += 1
        if self.row_0[3] == self.row_0[4]:
            score += 1
        if self.row_0[4] == self.row_0[1]:
            score += 1
        
        if self.row_1[0] == self.row_1[1]:
            score += 1
        if self.row_1[1] == self.row_1[2]:
            score += 1
        if self.row_1[2] == self.row_1[3]:
            score += 1
        if self.row_1[3] == self.row_1[0]:
            score += 1

        if self.row_2[0] == 0:
            score += 1
        if self.row_2[1] == self.row_2[2]:
            score += 1
        if self.row_2[2] == self.row_2[3]:
            score += 1
        if self.row_2[3] == self.row_2[4]:
            score += 1
        if self.row_2[4] == self.row_2[1]:
            score += 1

        if self.row_3[0] == 0:
            score += 1
        if self.row_3[1] == self.row_3[2]:
            score += 1
        if self.row_3[2] == self.row_3[3]:
            score += 1
        if self.row_3[3] == self.row_3[4]:
            score += 1
        if self.row_3[4] == self.row_3[1]:
            score += 1

        if self.row_4[0] == self.row_4[1]:
            score += 1
        if self.row_4[1] == self.row_4[2]:
            score += 1
        if self.row_4[2] == self.row_4[3]:
            score += 1
        if self.row_4[3] == self.row_4[0]:
            score += 1

        if self.win:
            score == 10000 * (1/self.moves)

        return score