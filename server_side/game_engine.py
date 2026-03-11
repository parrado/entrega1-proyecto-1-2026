import uuid
from random import randint

# game_engine.py
# -------------------------------------------------
# You must implement ALL game logic in this file.
# You must design:
#   - Game state structure
#   - Board representation
#   - Player representation
#   - Turn control
# -------------------------------------------------


# =================================================
# INITIALIZATION
# =================================================

def initialize_game():
    """
    Create and reset the entire game state.

    You must:
    - Define board structure
    - Define player storage
    - Define turn order
    - Define game phase (waiting, playing, finished)
    """
    pass


def reset_game():
    """
    Optional: Reset game to initial conditions.
    """
    pass


# =================================================
# PLAYER MANAGEMENT
# =================================================

def add_player(player_name):
    """
    Add a new player (max 4).

    Must:
    - Assign unique player_id
    - Prevent adding more than 4 players
    - Prevent duplicates if desired

    Return:
        {
            "status": "ok" or "error",
            "player_id": <int_if_ok>,
            "message": <optional_message>
        }
    """
    return {
        "status": "ok", 
        "player_id": str(uuid.uuid4())  # Example: generate unique ID
    }


def remove_player(player_id):
    """
    Optional: Remove player from game.
    """
    pass


def get_players():
    """
    Return current players and their states.
    """
    pass


# =================================================
# TURN MANAGEMENT
# =================================================

def get_current_player():
    """
    Return player_id whose turn it is.
    """
    pass


def next_turn():
    """
    Advance turn to next eligible player.
    """
    pass


def is_player_turn(player_id):
    """
    Return True if it is player's turn.
    """
    pass


# =================================================
# DICE LOGIC
# =================================================

def roll_dice(player_id):
    """
    Handle dice roll.

    Must:
    - Validate turn
    - Store dice result in game state
    - Handle extra turn rules if needed

    Return dice value and status.
    """
    pass


def get_last_dice():
    """
    Return last rolled dice value.
    """
    pass


# =================================================
# PIECE MANAGEMENT
# =================================================

def get_player_pieces(player_id):
    """
    Return all pieces of player and their positions.
    """
    pass


def get_piece_position(player_id, piece_id):
    """
    Return current position of selected piece.
    """
    pass


def can_piece_move(player_id, piece_id, dice_value):
    """
    Validate if selected piece can move.

    Must check:
    - Piece in jail
    - Dice allows exit
    - Movement does not exceed home
    - Blockades
    """
    pass


def move_piece(player_id, piece_id):
    """
    Perform movement.

    Must:
    - Validate turn
    - Validate dice was rolled
    - Validate move legality
    - Update board
    - Handle captures
    - Check win condition
    - Possibly change turn

    Return result dictionary.
    """
    pass


# =================================================
# BOARD LOGIC
# =================================================

def get_board():
    """
    Return full board representation.
    """
    pass


def update_board():
    """
    Recalculate board if needed after movement.
    """
    pass


def is_safe_square(position):
    """
    Return True if square is safe.
    """
    pass


def detect_blockade(position):
    """
    Return True if position contains a blockade.
    """
    pass


# =================================================
# CAPTURE & RULES
# =================================================

def check_capture(player_id, position):
    """
    Determine if a capture occurs.
    """
    pass


def send_piece_home(player_id, piece_id):
    """
    Return a captured piece to jail/start.
    """
    pass


def can_exit_jail(player_id, dice_value):
    """
    Validate if player can leave jail.
    """
    pass


# =================================================
# WIN CONDITION
# =================================================

def has_player_won(player_id):
    """
    Return True if all pieces reached home.
    """
    pass


def check_game_finished():
    """
    Determine if game is over.
    """
    pass


# =================================================
# GAME STATE
# =================================================

def get_game_status():
    """
    Return:
    - waiting_for_players
    - in_progress
    - finished
    """
    pass


def get_state():
    """
    Return COMPLETE game state.

    You define structure.
    """
    pass