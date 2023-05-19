import chess
import chess.svg
import random


def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
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
        min_eval = float('inf')
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
            return float('-inf')
        else:
            return float('inf')
    return 0


def best_move(board, depth):
    best_score = float('-inf')
    best_moves = []
    alpha = float('-inf')
    beta = float('inf')
    for move in board.legal_moves:
        board.push(move)
        eval_score = alphabeta(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval_score > best_score:
            best_score = eval_score
            best_moves = [move]
        elif eval_score == best_score:
            best_moves.append(move)
        alpha = max(alpha, eval_score)
    return random.choice(best_moves)


def random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)


def play():
    board = chess.Board()
    depth = 3

    while not board.is_game_over():
        if board.turn:
            move = best_move(board, depth)
            board.push(move)
            print("Alpha-Beta Agent's move:", move)
        else:
            move = random_move(board)
            board.push(move)
            print("computer's move:", move)

        print(board)

    if board.is_checkmate():
        if board.turn:
            print("computer wins!")
        else:
            print("Alpha-Beta Agent wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play()
