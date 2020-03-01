class Rook:
    def move(self):
        return "I move any number of spaces but only horizontally or vertically."


class Knight:
    def move(self):
        return "I move 2 and half spaces."


class Bishop:
    def move(self):
        return "I move any number of spaces diagonally."


def make_chess_piece(piece):
    '''
    Factory method that takes a string and returns an object based on it.
    '''
    pieces = {"knight": Knight(), "bishop": Bishop(), "rook": Rook()}
    return pieces[piece]


class ChessPieceFactory:
    def create_chess_piece(self, input_string):
        created_piece = make_chess_piece(input_string)
        return created_piece


chessPieceFactory = ChessPieceFactory()

piece_one = chessPieceFactory.create_chess_piece('knight')
print("Knight:", piece_one.move())

piece_two = chessPieceFactory.create_chess_piece('bishop')
print("Bishop:", piece_two.move())

piece_three = chessPieceFactory.create_chess_piece('rook')
print("Rook:", piece_three.move())



 #   without    factory    pattern


class ChessPieceFactory:

    def create_chess_piece(self, input_string):
        if input_string == "knight":
            return Knight()
        elif input_string == "rook":
            return Rook()
        elif input_string == "bishop":
            return Bishop()


chess_piece_factory = ChessPieceFactory
pieceOne = chessPieceFactory.create_chess_piece('knight')


 #  Problem is to add new piece because we have to perform action in the same function