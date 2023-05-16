import chess
import chess.svg
import sys
import random



def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        max_eval = -sys.maxsize
        for move in board.legal_moves:
            board.push(move)
            eval_score = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in board.legal_moves:
            board.push(move)
            eval_score = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval_score)
        return min_eval


def evaluate(board):
    if board.is_checkmate():
        if board.turn:
            return -sys.maxsize
        else:
            return sys.maxsize
    return 0


def best_move(board, depth):
    best_score = -sys.maxsize
    best_move = None
    for move in board.legal_moves:
        board.push(move)
        eval_score = minimax(board, depth - 1, False)
        board.pop()
        if eval_score > best_score:
            best_score = eval_score
            best_move = move
    return best_move


def agent_move(board):
    move = random.choice(list(board.legal_moves))
    return move


def play():
    board = chess.Board()
    depth = 3

    while not board.is_game_over():
        if board.turn:
            while True:
                move = best_move(board,depth)
                board.push(move)
                print("Agent's move:", move)
                print(board)
                break
                # if move1.lower() == "quit":
                #     break
                # try:
                #     board.push(move)
                #     print("Agent's move:", move)
                #     print(board)
                #     break
                # except ValueError:
                #     print("Invalid move. Please try again.")

            # if move1.lower() == "quit":
            #     sys.exit("Game terminated by the player.")

        else:
            # best = best_move(board, depth)
            # board.push(best)
            print("AI's move:", agent_move(board))

        print(board)

    if board.is_checkmate():
        if board.turn:
            print("You win!")
        else:
            print("AI wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play()