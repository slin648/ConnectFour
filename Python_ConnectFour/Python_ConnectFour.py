
#work of 林诗雨.
#serial number 222017321102082.

def creat_space(height, width):
        global slots
        slots = [[' '] * width for row in range(height)]

def creat_board(height, width):
        s = ''
        for row in range(height):
            s += '|'  
            for col in range(width):
                s += slots[row][col] + '|'
            s += '\n'  
       
        for col in range(2 * width + 1):
            s += '-'
        s += '\n'
        print(s)

def default():
        global player_choose,row_0,row_1,row_2,row_3,row_4,row_5,row_6
        player_choose=1
        row_0=5
        row_1=5
        row_2=5
        row_3=5
        row_4=5
        row_5=5
        row_6=5

def move_chess(player_choose,row_0,row_1,row_2,row_3,row_4,row_5,row_6):
        global cols,row
        if player_choose % 2==1:
                cols=int(input("Drop a red disk at column(0-6):"))
                if cols==0:
                        row=row_0
                if cols==1:
                        row=row_1
                if cols==2:
                        row=row_2
                if cols==3:
                        row=row_3
                if cols==4:
                        row=row_4
                if cols==5:
                        row=row_5
                if cols==6:
                        row=row_6
                slots[row][cols]="R"
        else:
                cols=int(input("Drop a yellow disk at column(0-6):"))
                if cols==0:
                        row=row_0
                if cols==1:
                        row=row_1
                if cols==2:
                        row=row_2
                if cols==3:
                        row=row_3
                if cols==4:
                        row=row_4
                if cols==5:
                        row=row_5
                if cols==6:
                        row=row_6
                slots[row][cols]="Y"

def value_change():
        global player_choose,row_0,row_1,row_2,row_3,row_4,row_5,row_6
        player_choose+=1
        if cols==0:
                row_0-=1
        if cols==1:
                row_1-=1
        if cols==2:
                row_2-=1
        if cols==3:
                row_3-=1
        if cols==4:
                row_4-=1
        if cols==5:
                row_5-=1
        if cols==6:
                row_6-=1
                
def is_horizontal_win(height, width):
        global win_type
        win_type=0
        for row in range(height):
            for col in range(width - 3):
                if slots[row][col] == "R" and \
                   slots[row][col+1] == "R" and \
                   slots[row][col+2] == "R" and \
                   slots[row][col+3] == "R":
                        win_type=1.1
                if slots[row][col] == "Y" and \
                   slots[row][col+1] == "Y" and \
                   slots[row][col+2] == "Y" and \
                   slots[row][col+3] == "Y":
                        win_type=1.2
                        
def is_vertical_win(height, width):
        global win_type
        win_type=0
        for row in range(height - 3):
                for col in range(width):
                        if slots[row][col] == "R" and \
                           slots[row + 1][col] == "R" and \
                           slots[row + 2][col] == "R" and \
                           slots[row + 3][col] == "R":
                                win_type=2.1
                        if slots[row][col] == "Y" and \
                           slots[row + 1][col] == "Y" and \
                           slots[row + 2][col] == "Y" and \
                           slots[row + 3][col] == "Y":
                                win_type=2.2

def is_down_diagonal_win(height, width):
        global win_type
        win_type=0
        for row in range(height - 3):
                for col in range(width - 3):
                        if slots[row][col] == "R" and \
                           slots[row + 1][col + 1] == "R" and \
                           slots[row + 2][col + 2] == "R" and \
                           slots[row + 3][col + 3] == "R":
                                win_type=3.1
                        if slots[row][col] == "Y" and \
                           slots[row + 1][col + 1] == "Y" and \
                           slots[row + 2][col + 2] == "Y" and \
                           slots[row + 3][col + 3] == "Y":
                                win_type=3.2

def is_up_diagonal_win(height, width):
        global win_type
        win_type=0
        for row in range(3, height):
                for col in range(width - 3):
                        if slots[row][col] == "R" and \
                           slots[row - 1][col + 1] == "R" and \
                           slots[row - 2][col + 2] == "R" and \
                           slots[row - 3][col + 3] == "R":
                                win_type=4.1
                        if slots[row][col] == "Y" and \
                           slots[row - 1][col + 1] == "Y" and \
                           slots[row - 2][col + 2] == "Y" and \
                           slots[row - 3][col + 3] == "Y":
                                win_type=4.2
                        


def main():
        global player_choose,row,row_0,row_1,row_2,row_3,row_4,row_5,row_6,win_type
        
        creat_space(6, 7)
        creat_board(6, 7)
        
        default()
        while True:
                move_chess(player_choose,row_0,row_1,row_2,row_3,row_4,row_5,row_6)
                if row > (-1):
                        value_change()
                        creat_board(6, 7)
                        is_horizontal_win(6,7)
                        if win_type==1.1:
                                print("--------------------The Red_player won (horizontal)--------------------")
                                break
                        if win_type==1.2:
                                print("--------------------The Yellow_player won (horizontal)--------------------")
                                break
                        is_vertical_win(6,7)
                        if win_type==2.1:
                                print("--------------------The Red_player won (vertical)--------------------")
                                break
                        if win_type==2.2:
                                print("--------------------The Yellow_player won (vertical)--------------------")
                                break
                        is_down_diagonal_win(6,7)
                        if win_type==3.1:
                                print("--------------------The Red_player won (down_diagonal)--------------------")
                                break
                        if win_type==3.2:
                                print("--------------------The Yellow_player won (down_diagonal)--------------------")
                                break
                        is_up_diagonal_win(6,7)
                        if win_type==4.1:
                                print("--------------------The Red_player won (up_diagonal)--------------------")
                                break
                        if win_type==4.2:
                                print("--------------------The Yellow_player won (up_diagonal)--------------------")
                                break
                else:
                        print("This column is full, change to another column and continue.")


try:
        main()
except ValueError:
        print("Make sure your input is an Interger and restart the programme.")
except SyntaxError:
        print("Make sure your input is an Interger and restart the programme.")
except UnboundLocalError:
        print("The Interger must be one between 0 and 5. restart the programme.")
except NameError:
        print("The Interger must be one between 0 and 5. restart the programme.")


