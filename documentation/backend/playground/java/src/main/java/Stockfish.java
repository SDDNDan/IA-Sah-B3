import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Stockfish implements Player {

    private BufferedReader processReader;
    private OutputStreamWriter processWriter;

    public Stockfish() {
        this("stockfish-8-win/Windows/stockfish_8_x64.exe");
    }

    public Stockfish(String enginePath) {
        try {
            startEngine(enginePath);
            getOutputAsString(0);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void startEngine(String enginePath) throws IOException {
        Process engineProcess = Runtime.getRuntime().exec(enginePath);
        processReader = new BufferedReader(new InputStreamReader(engineProcess.getInputStream()));
        processWriter = new OutputStreamWriter(engineProcess.getOutputStream());
    }

    List<String> getLegalMoves(String fen) throws IOException, InterruptedException {
        sendCommand("position fen " + fen);
        sendCommand("perft 4");
        List<String> lines = getOutputAsLines();
        List<String> moves = new ArrayList<>();
        for (String line : lines) {
            moves.add(line.split(":")[0]);
        }
        return moves;
    }

    String getBestMoveByMillis(String fen, int waitTime) throws IOException {
        sendCommand("position fen " + fen);
        sendCommand("go movetime " + waitTime);
        return getOutputLineContaining("bestmove").split(" ")[1];
    }

    String getBestMoveInDepth(String fen, int depth) throws IOException {
        sendCommand("position fen " + fen);
        sendCommand("go depth " + depth);
        return getOutputLineContaining("bestmove").split(" ")[1];
    }

    float getEvaluationInTime(String fen, int waitTime) throws IOException, InterruptedException {
        sendCommand("position fen " + fen);
        sendCommand("go movetime " + waitTime);
        float evalScore = 0.0f;
        List<String> lines = getOutputAsLines();
        evalScore = getEvalScoreFromLines(evalScore, lines);
        return evalScore / 100;
    }

    float getEvaluationByDepth(String fen, int depth) throws IOException, InterruptedException {
        sendCommand("position fen " + fen);
        sendCommand("go depth " + depth);
        float evalScore = 0.0f;
        List<String> lines = getOutputAsLines();
        evalScore = getEvalScoreFromLines(evalScore, lines);
        return evalScore / 100;
    }

    private float getEvalScoreFromLines(float evalScore, List<String> lines) {
        for (String line : lines) {
            if (line.startsWith("info depth ") && line.contains("score cp")) {
                try {
                    evalScore = Float.parseFloat(line.split("score cp ")[1]
                            .split(" nodes")[0]);
                } catch (Exception e) {
                    evalScore = Float.parseFloat(line.split("score cp ")[1]
                            .split(" upperbound nodes")[0]);
                }
            }
        }
        return evalScore;
    }


    String getOutputAsString(int waitTime) throws InterruptedException, IOException {
        StringBuilder buffer = new StringBuilder();
        Thread.sleep(waitTime);
        sendCommand("isready");
        while (true) {
            String text = processReader.readLine();
            if (text.equals("readyok"))
                break;
            else
                buffer.append(text).append("\n");
        }
        return buffer.toString();
    }

    List<String> getOutputAsLines() throws IOException {
        List<String> lines = new ArrayList<>();
        String line;
        try {
            Thread.sleep(300);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        //https://stackoverflow.com/questions/6792835/how-do-you-set-a-timeout-on-bufferedreader-and-printwriter-in-java-1-4
        do {
            processReader.read(new char[50], 0, 0);
            line = processReader.readLine();
            lines.add(line);
        } while (line != null && line.length()>0);
        return lines;
    }

    String getOutputLineContaining(String middle) throws IOException {
        String line;
        do {
            line = processReader.readLine();
        } while (line == null || !line.contains(middle));
        return line;
    }

    public void drawBoard(String fen) throws IOException, InterruptedException {
        sendCommand("position fen " + fen);
        sendCommand("d");

        String[] rows = getOutputAsString(0).split("\n");

        for (int i = 1; i < 18; i++) {
            System.out.println(rows[i]);
        }
    }

    void stopEngine() {
        try {
            sendCommand("quit");
            processReader.close();
            processWriter.close();
        } catch (IOException ignored) {
        }
    }

    void sendCommand(String command) throws IOException {
        processWriter.write(command + "\n");
        processWriter.flush();
    }

    public void finalize() {
        stopEngine();
    }

    @Override
    public String getBestMove(String fen) {
        try {
            return this.getBestMoveInDepth(fen, 12);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
