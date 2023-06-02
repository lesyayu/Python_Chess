import chess.pgn

def filter_games_by_player(pgn_file, player_name, new_pgn_file):
    new_pgn = chess.pgn.Game()
    filtered_games = []
    with open(pgn_file) as file:
        while True:
            game = chess.pgn.read_game(file)
            if game is None:
                break

            headers = game.headers

            if headers["White"] == player_name or headers["Black"] == player_name:
                filtered_games.append(game)

    with open(new_pgn_file, "w") as file:
        for game in filtered_games:
            file.write(str(game) + "\n\n")

    return new_pgn_file

# Pfad zur Eingabe-PGN-Datei
input_pgn_file = "lichess_broadcast_dem-u10-und-u10w_DB0R5egO_2023.06.02.pgn"
# Name des Spielers, den du suchen möchtest (z.B. "John Doe")
target_player = "Burban, Bogdan"
# Pfad zur Ausgabe-PGN-Datei
new_pgn_file = "output_Bo.pgn"

filtered_pgn = filter_games_by_player(input_pgn_file, target_player, new_pgn_file)
