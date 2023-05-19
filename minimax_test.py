import chess
import chess.svg
import random


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval_score)
        return min_eval


def evaluate(board):
    if board.is_checkmate():
        if board.turn:
            return float('-inf')
        else:
            return float('inf')
    return 0


def best_move(board, depth):
    best_score = float('-inf')
    best_moves = []
    for move in board.legal_moves:
        board.push(move)
        eval_score = minimax(board, depth - 1, False)
        board.pop()
        if eval_score > best_score:
            best_score = eval_score
            best_moves = [move]
        elif eval_score == best_score:
            best_moves.append(move)
    return random.choice(best_moves)


def random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)


def play():
    board = chess.Board()
    depth = 3

    while not board.is_game_over():
        if board.turn:
            best = best_move(board, depth)
            board.push(best)
            print("Agent 1's move:", best)
        else:
            best1 = random_move(board)
            board.push(best1)
            print("computer's move:", best1)

        print(board)



    if board.is_checkmate():
        if board.turn:
            print("computer wins!")
        else:
            print("Agent 1 wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play()
