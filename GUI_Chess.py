import chess
import chess.svg
import sys


def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        max_eval = -sys.maxsize
        for move in board.legal_moves:
            board.push(move)
            eval_score = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in board.legal_moves:
            board.push(move)
            eval_score = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
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
    alpha = -sys.maxsize
    beta = sys.maxsize
    for move in board.legal_moves:
        board.push(move)
        eval_score = alphabeta(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval_score > best_score:
            best_score = eval_score
            best_move = move
        alpha = max(alpha, eval_score)
    return best_move


def play():
    board = chess.Board()
    depth = 3

    while not board.is_game_over():
        if board.turn:
            move = input("Your move: ")
            board.push_san(move)
        else:
            best = best_move(board, depth)
            board.push(best)
            print("AI's move:", best)

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
