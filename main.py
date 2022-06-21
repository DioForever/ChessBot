from PIL import Image
from datetime import datetime
from discord.ext import tasks
from discord.ext import commands
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


pos_x = {
    "1": 75,
    "2": 225,
    "3": 375,
    "4": 525,
    "5": 675,
    "6": 825,
    "7": 975,
    "8": 1125
}
pos_y = {
    "8": 75,
    "7": 225,
    "6": 375,
    "5": 525,
    "4": 675,
    "3": 825,
    "2": 975,
    "1": 1125
}

def board_show(white_pieces, black_pieces):
    # Opening the board (used in background)
    board_ = Image.open(r"chess_board.png")
    b = Image.new("RGBA", board_.size)
    b.paste(board_, (0, 0))
    for piece in list(white_pieces.keys()):
        pieces = piece.split('-')
        piece_name = pieces[0]
        img_piece = Image.open(f"chess_{piece_name}.png")
        x = pos_x.get(white_pieces.get(piece).split(':')[0])
        y = pos_y.get(white_pieces.get(piece).split(':')[1])
        b.paste(img_piece.convert('RGBA'), (x-65, y-65), img_piece)
    for piece in list(black_pieces.keys()):
        pieces = piece.split('-')
        piece_name = pieces[0]
        img_piece = Image.open(f"chess_{piece_name}.png")
        x = pos_x.get(black_pieces.get(piece).split(':')[0])
        y = pos_y.get(black_pieces.get(piece).split(':')[1])
        b.paste(img_piece.convert('RGBA'), (x-65, y-65), img_piece)

    board = b
    board.show()
    return board


@bot.command()
async def c(ctx, *args):
    print('cmd')
    print(*args)
    if str(args[0]) == 'vs':
        try:
            id_guild = ctx.message.guild.id
        except:
            id_guild = 0
        if id_guild != 0:
            try:
                id = int(args[1].replace('<@', '').replace('>', ''))

                user = await bot.fetch_user(id)
                if user is not None:
                    await ctx.send(f'>>> The user {user} has been challenged!', delete_after=15)
            except:
                await ctx.send('>>> The user not found', delete_after=15)


def set_board():
    white_pieces = {"pawn_white-1": '1:2',
                    "pawn_white-2": '2:2',
                    "pawn_white-3": '3:2',
                    "pawn_white-4": '4:2',
                    "pawn_white-5": '5:2',
                    "pawn_white-6": '6:2',
                    "pawn_white-7": '7:2',
                    "pawn_white-8": '8:2',
                    "rook_white-1": '1:1',
                    "rook_white-2": '8:1',
                    "knight_white-1": '1:1',
                    "knight_white-2": '7:1',
                    "bishop_white-1": '3:1',
                    "bishop_white-2": '6:1',
                    "queen_white-2": '4:1',
                    "king_white-2": '5:1',
                    }


    black_pieces = {"pawn_black-1": '1:2',
                    "pawn_black-2": '2:2',
                    "pawn_black-3": '3:2',
                    "pawn_black-4": '4:2',
                    "pawn_black-5": '5:2',
                    "pawn_black-6": '6:2',
                    "pawn_black-7": '7:2',
                    "pawn_black-8": '8:2',
                    "rook_black-1": '1:1',
                    "rook_black-2": '8:1',
                    "knight_black-1": '1:1',
                    "knight_black-2": '7:1',
                    "bishop_black-1": '3:1',
                    "bishop_black-2": '6:1',
                    "queen_black-2": '4:1',
                    "king_black-2": '5:1',
                    }
    return white_pieces, black_pieces

white_pieces = {"pawn_white-1": '1:2',
                "pawn_white-2": '2:2',
                "pawn_white-3": '3:2',
                "pawn_white-4": '4:2',
                "pawn_white-5": '5:2',
                "pawn_white-6": '6:2',
                "pawn_white-7": '7:2',
                "pawn_white-8": '8:2',
                "rook_white-1": '1:1',
                "rook_white-2": '8:1',
                "knight_white-1": '2:1',
                "knight_white-2": '7:1',
                "bishop_white-1": '3:1',
                "bishop_white-2": '6:1',
                "queen_white-2": '4:1',
                "king_white-2": '5:1',
                }


black_pieces = {"pawn_black-1": '1:7',
                "pawn_black-2": '2:7',
                "pawn_black-3": '3:7',
                "pawn_black-4": '4:7',
                "pawn_black-5": '5:7',
                "pawn_black-6": '6:7',
                "pawn_black-7": '7:7',
                "pawn_black-8": '8:7',
                "rook_black-1": '1:8',
                "rook_black-2": '8:8',
                "knight_black-1": '2:8',
                "knight_black-2": '7:8',
                "bishop_black-1": '3:8',
                "bishop_black-2": '6:8',
                "queen_black-2": '4:8',
                "king_black-2": '5:8',
                }


board = board_show(white_pieces, black_pieces)

bot.run('')
