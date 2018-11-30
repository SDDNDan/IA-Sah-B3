import com.github.bhlangonijr.chesslib.Board;
import com.github.bhlangonijr.chesslib.Side;
import com.github.bhlangonijr.chesslib.game.Game;
import com.github.bhlangonijr.chesslib.move.Move;
import com.github.bhlangonijr.chesslib.move.MoveList;
import com.github.bhlangonijr.chesslib.pgn.PgnHolder;
import net.lingala.zip4j.core.ZipFile;
import net.lingala.zip4j.exception.ZipException;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;

//Use this to downloadFile again the database. (either for an update, either in case of ruined files)
//add a file in sitetext.txt the source of the http://www.pgnmentor.com/
//the program computes all pgn's that can be downloaded and downloads them somewhere...
//https://chess.stackexchange.com/questions/12518/java-library-for-pgn-parser
//https://github.com/bhlangonijr/chesslib

public class DownloadKit {

    private static Map<String, String> fileNameToFileTypeMap = new LinkedHashMap<>();

    private static String responsePath = "pgnmentor.html";

    public static void main(String[] args) throws Exception {
//        saveHtmlResponse();
//        computePlayerNames();
//        downloadAllDatabase();
//        unzipFiles();
//        computeAndWriteFens();
        //loadFens();
        Chess chess = new Chess();
        Random random = new Random();
        int stockfishWins = 0;
        int randomPlayerWins = 0;
        boolean sfWhite;
        int gameCount = 5;
        for (int i = 0; i < gameCount; i++) {
            sfWhite = random.nextBoolean();
            sfWhite = true;
            Player white = null;
            Player black = null;
            if(sfWhite){
                white = new Stockfish();
                black = new RandomPlayer();
            }
            else {
                white = new RandomPlayer();
                black = new Stockfish();
            }
            chess.startNewGame();
            while (!chess.isOver()){
                System.out.println(chess.getFen());
                chess.move(white.getBestMove(chess.getFen()), Side.WHITE);
                System.out.println("Black to move");
                if(!chess.isOver()){
                    String fen = chess.getFen();
                    System.out.println("Fen: " + fen);
                    String bestMove = black.getBestMove(fen);
                    System.out.println(bestMove);
                    chess.move(bestMove, Side.BLACK);
                }
            }
            if (sfWhite && chess.whiteWon()){
                stockfishWins++;
            }
            else randomPlayerWins++;
        }
        System.out.println("Stockfish wins: " + stockfishWins);
        System.out.println("Random player wins: " + randomPlayerWins);
    }

    private static void saveHtmlResponse() throws IOException {
        String siteUrl = "http://www.pgnmentor.com/files.html";
        writeTextToFile(responsePath, GET(siteUrl));
    }

    private static void computePlayerNames() throws FileNotFoundException {
        FileReader fileReader = new FileReader(responsePath);
        Scanner scanner = new Scanner(fileReader);
        String line;
        String startToken;
        String endToken;
        while (scanner.hasNextLine()) {
            line = scanner.nextLine();
            startToken = "\"";
            endToken = ".pgn";
            if (!line.contains(startToken) || !line.contains(endToken))
                continue;
            if (line.contains(".zip"))
                endToken = ".zip";
            String name = line.substring(line.indexOf(startToken) + 1, line.indexOf(endToken));
            if (!name.contains("www"))
                fileNameToFileTypeMap.put(name, endToken);
        }
    }

    private static void downloadAllDatabase() {
        fileNameToFileTypeMap.forEach(DownloadKit::downloadFile);
    }

    private static void unzipFiles() {
        fileNameToFileTypeMap.forEach(
                (fileName, fileFormat) -> {
                    if (fileFormat.equals(".zip")) {
                        System.out.println("Unzipping: " + fileName);
                        try {
                            String path;
                            if (fileName.contains("openings"))
                                path = "data/unzipped/openings/";
                            else path = "data/unzipped/players/";
                            unzip("data/downloadtest/" + fileName + fileFormat, path);
                        } catch (Exception e) {
                            System.out.println("wtf");
                        }
                    }
                }
        );
    }

    private static void computeAndWriteFens() throws Exception {
        List<String> fileNames = new ArrayList<>(fileNameToFileTypeMap.keySet());
        List<Game> corruptedGames = new ArrayList<>();
        int totalGamesCount = 0;
        for (String fileName : fileNames) {
            List<String> fensMoves = new ArrayList<>();
            String filePath = "data/" + fileName + ".pgn";
            String fenOutputPath = "fens/" + fileName + ".txt";
            System.out.println(fileName);
            PgnHolder pgn = new PgnHolder(filePath);
            pgn.loadPgn();
            for (Game game : pgn.getGame()) {
                try {
                    ++totalGamesCount;
                    game.loadMoveText();
                    MoveList moves = game.getHalfMoves();
                    Board board = new Board();

                    for (Move move : moves) {
                        fensMoves.add(board.getFen() + " " + move);
                        board.doMove(move);
                    }
                    fensMoves.add(board.getFen() + " " + "z0z0");
                } catch (Exception e) {
                    corruptedGames.add(game);
                }
            }
            StringBuilder fenStringBuilder = new StringBuilder();
            fensMoves.forEach(fen -> fenStringBuilder.append(fen).append("\n"));
            writeTextToFile(fenOutputPath, fenStringBuilder.toString());
        }
        System.out.println(corruptedGames.size() + " corrupted games. " + totalGamesCount + " total games count.");
    }


    private static List<String> getLinesFromFile(String sourceFilePath) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(sourceFilePath))) {
            List<String> lines = new ArrayList<>();
            String line = br.readLine();
            while (line != null) {
                lines.add(line);
                line = br.readLine();
            }
            return lines;
        }
    }

    private static void writeTextToFile(String path, String text) {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(path))){
            writer.write(text);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String GET(String urlString) throws IOException {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        InputStream inputStream = connection.getInputStream();
        BufferedReader rd = new BufferedReader(new InputStreamReader(inputStream));
        StringBuilder sb = new StringBuilder();
        String line = rd.readLine();
        while (line != null) {
            sb.append(line);
            sb.append(System.lineSeparator());
            line = rd.readLine();
        }
        return sb.toString();
    }

    private static void downloadFile(String fileName, String fileType) {
        System.out.println("Downloading " + fileName);
        try {
            URL url = new URL("http://www.pgnmentor.com/" + fileName + fileType);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            InputStream in = connection.getInputStream();
            String path = "pgns/" + fileName + fileType;
            createNewFile(path);
            FileOutputStream out = new FileOutputStream(path);
            copy(in, out, 1024);
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void createNewFile(String path) {
        File file = new File(path);
        file.setWritable(true);
        file.setReadable(true);
        file.getParentFile().mkdirs();
        try {
            file.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void copy(InputStream input, OutputStream output, int bufferSize) throws IOException {
        byte[] buf = new byte[bufferSize];
        int n = input.read(buf);
        while (n >= 0) {
            output.write(buf, 0, n);
            n = input.read(buf);
        }
        output.flush();
    }

    public static void unzip(String source, String destination) {
        try {
            ZipFile zipFile = new ZipFile(source);
            zipFile.extractAll(destination);
        } catch (ZipException e) {
            e.printStackTrace();
        }
    }

    public static void loadFens() throws IOException {
        int count = 0;
        long startTime = System.currentTimeMillis();
        List<String> fileNames = new ArrayList<>(fileNameToFileTypeMap.keySet());
        Set<String> fens = new HashSet<>();
        for (String fileName : fileNames)
            if (fileName.contains("players")) {
                String sourcePath = "fens/" + fileName + ".txt";
                System.out.println(sourcePath);
                List<String> lines = getLinesFromFile(sourcePath);
                count += lines.size();
                String fen;
                //              String move;
                for (String line : lines) {
                    fen = line.substring(0, line.length() - 5);
//                    move = line.substring(line.length() - 4);
                    fens.add(fen);
                }
            }
        System.out.println("Loaded " + count + " positions in " + (System.currentTimeMillis() - startTime) / 1000.0 + " seconds");
        System.out.println(fens.size() + " unique positions");
    }
}
