import os
import chess
import chess.engine
import shutil

def main():
    print("===============================")
    print("   SCHACH-TRAINER (ANDROID)")
    print("===============================\n")

    # Stockfisch-Pfad für Android/Linux ermitteln
    engine_path = shutil.which("stockfish")
    if not engine_path:
        for path in ["/system/bin/stockfish", "/usr/games/stockfish", "/usr/bin/stockfish", "/usr/local/bin/stockfish"]:
            if os.path.exists(path):
                engine_path = path
                break

    if not engine_path:
        print("❌ Stockfisch Engine nicht gefunden!")
        return

    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    print("Brett erfolgreich initialisiert. Das Spiel kann beginnen!\n")
    print(board)

    while not board.is_game_over():
        user_input = input("\nDein Zug (z.B. e2e4): ").strip().lower()
        
        try:
            move = chess.Move.from_uci(user_input)
            if move in board.legal_moves:
                board.push(move)
                print("\nDein Zug:")
                print(board)
                
                if board.is_game_over():
                    break
                    
                print("\nStockfisch überlegt...")
                result = engine.play(board, chess.engine.Limit(time=0.5))
                stockfisch_move = result.move
                
                board.push(stockfisch_move)
                print(f"Stockfisch hat gezogen: {stockfisch_move}")
                print("\nAktuelles Brett:")
                print(board)
                
            else:
                print("❌ Ungültiger Zug! Probiere es noch einmal.")
                
        except ValueError:
            print("⚠️ Falsches Format! Nutze z.B. 'e2e4'.")

    engine.quit()
    print("Das Spiel ist beendet!")

if __name__ == "__main__":
    main()