# ===============================================================
# game.py
# ---------------------------------------------------------------
# Implements the Red-Blue Nim game following AIMA-style structure.
# Each game state is represented as a tuple: (num_red, num_blue, to_move)
# ---------------------------------------------------------------
# Methods correspond to textbook notation:
#   S0             → initial state
#   TO-MOVE(s)     → to_move(state)
#   ACTIONS(s)     → actions(state)
#   RESULT(s, a)   → result(state, action)
#   IS-TERMINAL(s) → is_terminal(state)
#   UTILITY(s, p)  → utility(state, player)
# ===============================================================

class RedBlueNim:
    

    """
     A class representing the Red-Blue Nim game.

    Each state consists of two integer piles (red, blue) and an indicator
    of which player is to move next.  The rules are:

        • On a player's turn, they choose one pile (red or blue) and
          remove either 1 or 2 marbles from that pile.
        • The game ends immediately when *either* pile becomes empty.
        • In the STANDARD version, the player who empties a pile loses.
        • In the MISÈRE version, the player who empties a pile wins.

    This class provides the methods required by the generic
    Minimax and Alpha-Beta algorithms (ref: Russell, S. & Norvig, P.,
    "Artificial Intelligence: A Modern Approach", 4th Edition, Pearson, 2021):
    TO-MOVE, ACTIONS, RESULT, IS-TERMINAL, and UTILITY.


    """
    def __init__(self, num_red, num_blue, version="standard", first_player="computer"):
        
        """
        Initialize the game and construct the initial state S₀.

        Args:
            num_red (int):  Initial number of red marbles.
            num_blue (int): Initial number of blue marbles.
            version (str):  "standard" or "misere" determining win condition.
            first_player (str): "computer" or "human" indicating who moves first.

        Attributes:
            version (str):  The rule variant ("standard" or "misere").
            initial (tuple): The initial game state (num_red, num_blue, to_move).
        """

        self.version = version
        self.initial = (num_red, num_blue, first_player)  # (R, B, to_move)

    # ------------------------------------------------------------
    # TO-MOVE(s)
    # ------------------------------------------------------------
    def to_move(self, state):
        """
        Return the player whose turn it is to move in state s.

        Args:
            state (tuple): Current game state (red, blue, to_move).

        Returns:
            str: "computer" or "human" indicating the player to move next.
        """
        return state[2]

    # ------------------------------------------------------------
    # ACTIONS(s)
    # ------------------------------------------------------------
    def actions(self, state):
        """
        Return the list of all legal actions available in state s.

        Each legal action is represented as a tuple (pile, count),
        where 'pile' ∈ {"red", "blue"} and count ∈ {1, 2}.
        Only moves that remove available marbles are included.

        Args:
            state (tuple): Current game state (red, blue, to_move).

        Returns:
            list[tuple]: All valid moves in this state.
                         e.g., [("red", 1), ("blue", 2)]
        """
        red, blue, _ = state
        legal_moves = []

        if red >= 1:
            legal_moves.append(("red", 1))
        if red >= 2:
            legal_moves.append(("red", 2))
        if blue >= 1:
            legal_moves.append(("blue", 1))
        if blue >= 2:
            legal_moves.append(("blue", 2))

        return legal_moves

    # ------------------------------------------------------------
    # RESULT(s, a)
    # ------------------------------------------------------------
    def result(self, state, action):
        """
        Apply action a in state s and return the resulting state.

        Args:
            state (tuple):  The current game state (red, blue, to_move).
            action (tuple): A valid action (pile, count).

        Returns:
            tuple: New game state (new_red, new_blue, next_player)
                   after executing the action.
        """
        red, blue, to_move = state
        pile, count = action

        if pile == "red":
            red -= count
        elif pile == "blue":
            blue -= count

        next_player = "human" if to_move == "computer" else "computer"
        return (red, blue, next_player)

    # ------------------------------------------------------------
    # IS-TERMINAL(s)
    # ------------------------------------------------------------
    def is_terminal(self, state):
        """
        Determine whether the game has reached a terminal state.

        A terminal state occurs when *either* pile becomes empty.

        Args:
            state (tuple): Current game state (red, blue, to_move).

        Returns:
            bool: True if the game has ended, False otherwise.
        """
        red, blue, _ = state
        return red == 0 or blue == 0

    # ------------------------------------------------------------
    # UTILITY(s, p)
    # ------------------------------------------------------------
    def utility(self, state, player):
        """
        Return the utility value for the given player in this terminal state.
        Scoring rule:
            - Standard: player loses if pile is empty → negative score
            - Misère: player wins if pile is empty → positive score
        Score = ±(2 * red + 3 * blue)
        """
        red, blue, to_move = state
        score = 2 * red + 3 * blue

        if self.version == "standard":
        # The player who just moved caused empty pile → loses
            if to_move != player:
                return -score
            else:
                return score

        elif self.version == "misere":
            # The player who just moved caused empty pile → wins
            if to_move != player:
                return score
            else:
                return -score

    # ------------------------------------------------------------
    # Helper: DISPLAY(s)
    # ------------------------------------------------------------
    def display(self, state):
        """
        Print a human-readable description of the current game state.

        Args:
            state (tuple): Current state (red, blue, to_move).

        Side Effects:
            Prints the number of red and blue marbles and the next player.
        """
        red, blue, to_move = state
        print(f"Red marbles: {red} | Blue marbles: {blue} | To move: {to_move}")

