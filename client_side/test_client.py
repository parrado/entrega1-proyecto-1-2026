# test_client.py

from client_transport import GameClient


def main():

    client = GameClient()
    client.connect()

    print("\n--- INITIALIZE GAME ---")
    print(client.send_action("initialize"))

    print("\n--- ADD PLAYER ---")
    print(client.send_action("join", player_name="Alice"))
    

    print("\n--- GET PLAYERS ---")
    print(client.send_action("get_players"))

    print("\n--- CURRENT PLAYER ---")
    print(client.send_action("current_player"))

    print("\n--- ROLL DICE ---")
    print(client.send_action("roll_dice"))

    print("\n--- MOVE PIECE 0 ---")
    print(client.send_action("move_piece", piece_id=0))

    print("\n--- GET BOARD ---")
    print(client.send_action("get_board"))

    print("\n--- GET FULL STATE ---")
    print(client.send_action("get_state"))

    client.close()


if __name__ == "__main__":
    main()