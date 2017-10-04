# Created by Max Yurchenko on 01.10.2017
# email: joker0071911@gmail.com 
# feel free to ask any questions) 
# Copyright(C) 2017  


class ChessDesk:

    def __init__(self):
        """
        desk initialization
        """
        num_array = []
        for i in range(1, 9):
            num_array.append(str(i))
        let_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        string_array = []
        for let in let_array:
            string = []
            for num in num_array:
                string.append(let+num)
            string_array.append(string)
        self.desk = string_array
        self.white_king = 

    def move(self, current_coord_num, current_coord_letter, new_coord_num, new_coord_letter):
        """
        :param current_coord_num:
        :param current_coord_letter:
        :param new_coord_num:
        :param new_coord_letter:
        :return:
        """
        self.desk[new_coord_num][new_coord_letter] = self.desk[current_coord_num][current_coord_letter]



a = ChessDesk()
