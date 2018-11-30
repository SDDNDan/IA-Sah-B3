import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.util.List;

public class StockfishTest {
    private Stockfish stockfish;

    private String enginePath = "engines/stockfish-8-win/Windows/stockfish_8_x64.exe";

    private String fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";

    @Before
    public void setUp() throws IOException, InterruptedException {
        stockfish = new Stockfish(enginePath);
    }

    @Test
    public void getBestMoveMillisTest() throws IOException, InterruptedException {
        String result = stockfish.getBestMoveByMillis(fen, 1000);
        //System.out.println(result);
    }

    @Test
    public void getBestMoveDepthTest() throws IOException, InterruptedException {
        String result = stockfish.getBestMoveInDepth(fen, 13);
        //System.out.println(result);
    }

    @Test
    public void getLegalMovesTest() throws IOException, InterruptedException {
        List<String> moves = stockfish.getLegalMoves(fen);
//        for (String move : moves) {
//            System.out.println(move);
//        }
//        System.out.println(moves.size());
    }

    @Test
    public void getEvaluationMillisTest() throws IOException, InterruptedException {
        float result = stockfish.getEvaluationInTime(fen, 5000);
        //System.out.println(result);
    }

    @Test
    public void getEvaluationDepthTest() throws IOException, InterruptedException {
        float result = stockfish.getEvaluationByDepth(fen, 15);
        //System.out.println(result);
    }
}
