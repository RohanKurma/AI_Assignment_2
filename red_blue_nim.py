# ===============================================================
# red_blue_nim.py
# ---------------------------------------------------------------
# Main driver for Red-Blue Nim game.
# Usage:
#   python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>
#
# Example:
#   python red_blue_nim.py 3 4 standard computer 3
#
# Default behavior:
#   version = "standard"
#   first-player = "computer"
#   depth = None  (unlimited)
# ---------------------------------------------------------------

import sys
from game import RedBlueNim
from minimax import minimax_search, alpha_beta_search, alpha_beta_limited


# ---------------------------------------------------------------
# EVALUATION FUNCTION for depth-limited Alpha-Beta (Extra Credit)
# ---------------------------------------------------------------
def eval_fn(state, player):
    """
    Simple heuristic evaluation function.
    Estimates goodness of a non-terminal state based on remaining marbles.
    Lower marble count is worse for the player whose turn it is.
    """
    red, blue, to_move = state
    value = 2 * red + 3 * blue
    # Favor states where the opponent faces fewer marbles
    if to_move == player:
        return -value
    else:
        return value


# ---------------------------------------------------------------
# PROMPT for HUMAN MOVE
# ---------------------------------------------------------------
def get_human_move(game, state):
    """Prompt the human player to enter a valid move."""
    while True:
        try:
            pile = input("Choose pile (red/blue): ").strip().lower()
            count = int(input("How many marbles to remove (1 or 2)? ").strip())
            move = (pile, count)
            if move in game.actions(state):
                return move
            else:
                print("Invalid move! Try again.\n")
        except Exception:
            print("Invalid input! Try again.\n")


# ---------------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------------
def main():
    # Handle command-line arguments
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: python red_blue_nim.py <num-red> <num-blue> [version] [first-player] [depth]")
        return

    num_red = int(args[0])
    num_blue = int(args[1])
    version = args[2] if len(args) >= 3 else "standard"
    first_player = args[3] if len(args) >= 4 else "computer"
    depth = int(args[4]) if len(args) == 5 else None

    # Initialize game
    game = RedBlueNim(num_red, num_blue, version, first_player)
    state = game.initial

    print("\n===== Red-Blue Nim =====")
    print(f"Version: {version} | First player: {first_player} | Depth: {depth if depth else 'Full search'}\n")

    # Game loop
    while not game.is_terminal(state):
        game.display(state)
        current_player = game.to_move(state)

        if current_player == "human":
            move = get_human_move(game, state)
        else:
            print("\nComputer thinking...\n")
            if depth is not None:
                move = alpha_beta_limited(game, state, depth, eval_fn)
            else:
                move = alpha_beta_search(game, state)
            print(f"Computer chooses: {move}\n")

        # Apply the move
        state = game.result(state, move)

    # Game over
    game.display(state)
    print("\n===== Game Over =====")
    for player in ["computer", "human"]:
        print(f"{player.capitalize()} utility: {game.utility(state, player)}")


# ---------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------
if __name__ == "__main__":
    main()
    # ------------------------------------------------------------  