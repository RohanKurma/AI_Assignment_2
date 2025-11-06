# ===============================================================
# minimax.py
# ---------------------------------------------------------------
# Implements MINIMAX, ALPHA-BETA, and DEPTH-LIMITED ALPHA-BETA
# search algorithms exactly following the pseudocode mentioned in Russell & Norvig (2021).
#
# Each function includes docstrings describing:
#   • Purpose (as in the textbook definition)
#   • Parameters (game, state, player, depth, etc.)
#   • Return values (utility, move)
# ===============================================================

import math


# ---------------------------------------------------------------
# 1️  MINIMAX-SEARCH (basic version)
# ---------------------------------------------------------------
def minimax_search(game, state):
    """
    Perform a complete MINIMAX search for the given game state.

    Implements the textbook MINIMAX-SEARCH(game, state) algorithm
    from Russell & Norvig (AIMA).

    Args:
        game: An instance of a game class implementing
              TO-MOVE(s), ACTIONS(s), RESULT(s, a),
              IS-TERMINAL(s), and UTILITY(s, p).
        state: The current game state tuple (red, blue, to_move).

    Returns:
        move: The optimal action for the current player to take
              according to the Minimax decision rule.
    """
    player = game.to_move(state)
    value, move = max_value(game, state, player)
    return move


def max_value(game, state, player):
    """
    Compute the maximum expected utility for the maximizing player.

    This corresponds to the MAX-VALUE function in AIMA pseudocode.

    Args:
        game: The game environment object.
        state: Current game state (tuple).
        player: The player whose perspective the utility is evaluated from.

    Returns:
        (utility, move): A tuple containing the best achievable utility
                         value and the corresponding move for MAX.
    """
    if game.is_terminal(state):
        return game.utility(state, player), None

    v = -math.inf
    best_move = None
    for a in game.actions(state):
        v2, _ = min_value(game, game.result(state, a), player)
        if v2 > v:
            v, best_move = v2, a
    return v, best_move


def min_value(game, state, player):
    """
    Compute the minimum expected utility for the minimizing player.

    This corresponds to the MIN-VALUE function in AIMA pseudocode.

    Args:
        game: The game environment object.
        state: Current game state (tuple).
        player: The player whose perspective the utility is evaluated from.

    Returns:
        (utility, move): A tuple containing the best achievable utility
                         value and the corresponding move for MIN.
    """
    if game.is_terminal(state):
        return game.utility(state, player), None

    v = math.inf
    best_move = None
    for a in game.actions(state):
        v2, _ = max_value(game, game.result(state, a), player)
        if v2 < v:
            v, best_move = v2, a
    return v, best_move


# ---------------------------------------------------------------
# 2️  ALPHA-BETA-SEARCH (with pruning)
# ---------------------------------------------------------------
def alpha_beta_search(game, state):
    """
    Perform MINIMAX search using Alpha–Beta pruning.

    Implements ALPHA-BETA-SEARCH(game, state) from AIMA,
    which reduces the number of nodes explored without
    affecting the final result.

    Args:
        game: The game environment object.
        state: Current game state (tuple).

    Returns:
        move: The optimal move for the player to move next.
    """
    player = game.to_move(state)
    value, move = max_value_ab(game, state, player, -math.inf, math.inf)
    return move


def max_value_ab(game, state, player, alpha, beta):
    """
    Compute the MAX-VALUE for Alpha–Beta search.

    Prunes branches where beta ≤ alpha to improve efficiency.

    Args:
        game: The game environment object.
        state: Current game state (tuple).
        player: The reference player whose utility is evaluated.
        alpha (float): The best value found so far for MAX.
        beta (float): The best value found so far for MIN.

    Returns:
        (utility, move): The best utility and move for MAX from this node.
    """
    if game.is_terminal(state):
        return game.utility(state, player), None

    v = -math.inf
    best_move = None
    for a in game.actions(state):
        v2, _ = min_value_ab(game, game.result(state, a), player, alpha, beta)
        if v2 > v:
            v, best_move = v2, a
        alpha = max(alpha, v)
        if v >= beta:  # β cutoff
            break
    return v, best_move


def min_value_ab(game, state, player, alpha, beta):
    """
    Compute the MIN-VALUE for Alpha–Beta search.

    Prunes branches where beta ≤ alpha to improve efficiency.

    Args:
        game: The game environment object.
        state: Current game state (tuple).
        player: The reference player whose utility is evaluated.
        alpha (float): The current best value for MAX.
        beta (float): The current best value for MIN.

    Returns:
        (utility, move): The best utility and move for MIN from this node.
    """
    if game.is_terminal(state):
        return game.utility(state, player), None

    v = math.inf
    best_move = None
    for a in game.actions(state):
        v2, _ = max_value_ab(game, game.result(state, a), player, alpha, beta)
        if v2 < v:
            v, best_move = v2, a
        beta = min(beta, v)
        if v <= alpha:  # α cutoff
            break
    return v, best_move


# ---------------------------------------------------------------
# 3️  DEPTH-LIMITED ALPHA-BETA (Extra Credit)
# ---------------------------------------------------------------
def alpha_beta_limited(game, state, depth_limit, eval_fn):
    """
    Perform a depth-limited Alpha–Beta search.

    Used when full search to terminal states is infeasible.
    At depth == 0 or terminal nodes, uses a heuristic evaluation
    function to estimate the utility value.

    Args:
        game: Game environment implementing the AIMA methods.
        state: Current game state (tuple).
        depth_limit (int): Maximum search depth (number of plies).
        eval_fn (callable): Heuristic evaluation function taking
                            (state, player) → numeric value.

    Returns:
        move: The best move determined by the depth-limited search.
    """
    player = game.to_move(state)
    value, move = max_value_dl(game, state, player, -math.inf, math.inf, depth_limit, eval_fn)
    return move


def max_value_dl(game, state, player, alpha, beta, depth, eval_fn):
    """
    Compute MAX-VALUE for the depth-limited Alpha–Beta algorithm.

    Stops searching further when depth == 0, returning
    eval_fn(state, player) as an approximate utility.

    Args:
        game: The game environment.
        state: Current state (tuple).
        player: The reference player for evaluation.
        alpha (float): Alpha bound.
        beta (float): Beta bound.
        depth (int): Remaining depth limit.
        eval_fn (callable): Evaluation function.

    Returns:
        (utility, move): Estimated utility and best move.
    """
    if game.is_terminal(state) or depth == 0:
        return eval_fn(state, player), None

    v = -math.inf
    best_move = None
    for a in game.actions(state):
        v2, _ = min_value_dl(game, game.result(state, a), player, alpha, beta, depth - 1, eval_fn)
        if v2 > v:
            v, best_move = v2, a
        alpha = max(alpha, v)
        if v >= beta:  # β cutoff
            break
    return v, best_move


def min_value_dl(game, state, player, alpha, beta, depth, eval_fn):
    """
    Compute MIN-VALUE for the depth-limited Alpha–Beta algorithm.

    Stops searching further when depth == 0, returning
    eval_fn(state, player) as an approximate utility.

    Args:
        game: The game environment.
        state: Current state (tuple).
        player: The reference player for evaluation.
        alpha (float): Alpha bound.
        beta (float): Beta bound.
        depth (int): Remaining depth limit.
        eval_fn (callable): Evaluation function.

    Returns:
        (utility, move): Estimated utility and best move.
    """
    if game.is_terminal(state) or depth == 0:
        return eval_fn(state, player), None

    v = math.inf
    best_move = None
    for a in game.actions(state):
        v2, _ = max_value_dl(game, game.result(state, a), player, alpha, beta, depth - 1, eval_fn)
        if v2 < v:
            v, best_move = v2, a
        beta = min(beta, v)
        if v <= alpha:  # α cutoff
            break
    return v, best_move
