import sys

class User:
    username:str=""
    password:str=""
    win: int = 0
    loss: int = 0
    draw: int = 0
    def __init__(self,username,password):
        self.username= username
        self.password = password


class Pawn:
    name: str = "P"
    loc: int= 0
    color: str = ""
    direction: int = 0
    start_row: int = 0
    def __init__(self, color: str, loc: int):
        self.color = color
        self.loc = loc
       

class Knight:
    name: str = "N"
    loc: int =0
    moves: list=[]
    color: str=""
    def __init__(self, color: str, loc: int):
        self.color = color
        self.loc = loc
 
       
        
class Bishop:
    name: str = "B"
    loc: int =0
    color: str =""
    def __init__(self, color: str, loc: int):
        self.color = color
        self.loc = loc

class Rook:
    name: str = "R"
    loc: int =0
    color: str =""
    def __init__(self, color: str, loc: int):
        self.color = color
        self.loc = loc

class Queen:
    name: str = "Q"
    loc: int =0
    def __init__(self, color: str, loc: int):
        self.color = color
        self.loc = loc
class King:
    name: str = "K"
    loc: int=0
    max_move: int = 1
    def __init__(self, color: str, loc: int):
        self.color = color
        self.loc = loc

class Chess:
    chess: list = []
    users:list[User]=[]
    turn: str =""
    limit: int = 0
    move_count: int = 0
    selected: None
    history: list = []
    game_over: bool = False
    result:None

    def __init__(self):
        self.chess = [[None for _ in range(8)] for _ in range(8)]
        self.users = []
        self.turn = "w"
        self.limit = 0
        self.move_count = 0
        self.selected = None
        self.history = []
        self.game_over = False
        self.result = None
        self.chess[0][0] = Rook("b", 0)
        self.chess[0][1] = Knight("b", 1)
        self.chess[0][2] = Bishop("b", 2)
        self.chess[0][3] = Queen("b", 3)
        self.chess[0][4] = King("b", 4)
        self.chess[0][5] = Bishop("b", 5)
        self.chess[0][6] = Knight("b", 6)
        self.chess[0][7] = Rook("b", 7)

        for c in range(8):
            self.chess[1][c] = Pawn("b", 8 + c)

        for c in range(8):
            self.chess[6][c] = Pawn("w", 48 + c)

        self.chess[7][0] = Rook("w", 56)
        self.chess[7][1] = Knight("w", 57)
        self.chess[7][2] = Bishop("w", 58)
        self.chess[7][3] = Queen("w", 59)
        self.chess[7][4] = King("w", 60)
        self.chess[7][5] = Bishop("w", 61)
        self.chess[7][6] = Knight("w", 62)
        self.chess[7][7] = Rook("w", 63)
    def print_chess(self):
        for row in range(8):
            cells = []
            for column in range(8):
                piece = self.chess[row][column]
                if piece is None:
                    cells.append("  ")
                else:
                    cells.append(f"{piece.name}{piece.color}")

            
            print(  "|".join(cells) + "|")
    f1=open("input0.txt","rt")
    sys.stdin= f1
    f2=open("output0.txt" , "wt")
    sys.stdout = f2


c1=Chess()
c1.print_chess()
level = "register"
while True:
    if level=="register":
        print("1.register")
        print("2.login")
        print("3.remove")
        print("4.help")
        print("0.exit")
        cmd=int(input())
        if cmd==1:
            level="register"
        elif cmd==2:
            level="login"
        elif cmd==3:
            level="remove"
        elif cmd==4:
            level="help"
        elif cmd==0:
            level="register"
            print("exit")



