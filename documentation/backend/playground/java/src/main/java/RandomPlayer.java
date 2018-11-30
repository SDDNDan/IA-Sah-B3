import java.io.IOException;
import java.util.List;
import java.util.Random;

public class RandomPlayer implements Player{
    @Override
    public String getBestMove(String fen) {
        try {
            Chess chess = new Chess();
            List<String> moves = chess.getLegalMoves();
            Random random = new Random();
            return moves.get(random.nextInt(moves.size()));
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return null;
    }
}
