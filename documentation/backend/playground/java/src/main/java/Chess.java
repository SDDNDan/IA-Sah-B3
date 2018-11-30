import com.github.bhlangonijr.chesslib.Board;
import com.github.bhlangonijr.chesslib.Side;
import com.github.bhlangonijr.chesslib.move.Move;

import java.io.IOException;
import java.util.List;

public class Chess {
    private Board board;

    private String enginePath = "engines/stockfish-8-win/Windows/stockfish_8_x64.exe";

    private Stockfish stockfish;

    public Chess() {
        startNewGame();
    }

    public void startNewGame() {
        board = new Board();
        stockfish = new Stockfish(enginePath);
    }

    public boolean isOver() {
        return board.isMated() || board.isDraw();
    }

    public Stockfish getStockfish() {
        return stockfish;
    }

    public String getFen() {
        return this.board.getFen();
    }

    public boolean whiteWon() {
        return board.getSideToMove() == Side.BLACK;
    }

    public String getBestMoveInTime(int timeMillis) throws IOException {
        return stockfish.getBestMoveByMillis(board.getFen(), timeMillis);
    }

    public String getBestMoveInDepth(int depth) throws IOException {
        return stockfish.getBestMoveInDepth(board.getFen(), depth);
    }

    public float getEvaluationInTime(int timeMillis) throws IOException, InterruptedException {
        return stockfish.getEvaluationInTime(board.getFen(), timeMillis);
    }

    public float getEvaluationInDepth(int depth) throws IOException, InterruptedException {
        return stockfish.getEvaluationByDepth(board.getFen(), depth);
    }

    public void move(String move, Side sideToMove) {
        Move moveM = new Move(move, sideToMove);
        if (!board.isMoveLegal(moveM, true)) {
            System.out.println(board.getFen());
            System.out.println("Invalid move");
        }
        if(sideToMove!=board.getSideToMove()){
            System.out.println("Wrong side to move");
        }
        board.doMove(moveM);
        if(sideToMove==board.getSideToMove()){
            System.out.println("Not update who has to move");
        }
//            if(board.getSideToMove() == Side.BLACK)
//                board.setSideToMove(Side.WHITE);
//            else board.setSideToMove(Side.BLACK);
    }

    public List<String> getLegalMoves() throws IOException, InterruptedException {
        String fen = board.getFen();
        return stockfish.getLegalMoves(fen);
    }
}
