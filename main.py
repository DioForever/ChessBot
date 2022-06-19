from PIL import Image


def board():
    # Opening the board (used in background)
    board = Image.open(r"chess_board.png")
    b = Image.new("RGBA", board.size)
    b.paste(board, (0, 0))
    white_pieces = {"queen_white-1": '1:1',
                    "queen_black-1": '1:3',
                    "bishop_white-1": '4:1',
                    "rook_white-1": '6:1',
                    "pawn_black-1": '8:1',
                    "bishop_black-1": '2:1',
                    "rook_black-1": '5:1'}

    for piece in list(white_pieces.keys()):
        pieces = piece.split('-')
        piece_number = pieces[1]
        piece_name = pieces[0]
        img_piece = Image.open(f"chess_{piece_name}.png")
        x = int(white_pieces.get(piece).split(':')[0])
        y = int(white_pieces.get(piece).split(':')[1])
        b.paste(img_piece.convert('RGBA'), (x * 152 - 152, y * 152 - 152), img_piece)
    b.show()


if __name__ == '__main__':
    board()
