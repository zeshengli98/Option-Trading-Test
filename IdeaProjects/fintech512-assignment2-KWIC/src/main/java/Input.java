import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

public class Input {

    private ArrayList<String> ignoreWords;
    private ArrayList<String> lines;
    private ArrayList<ArrayList<String>> words;


    public void inputfile(String pathname) {
        this.ignoreWords = new ArrayList<String>();
        this.lines = new ArrayList<String>();
        this.words = new ArrayList<ArrayList<String>> ();
        try {
            File myObj = new File(pathname);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data.equals("::")){
                    break;
                }
                ignoreWords.add(data);
            }
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                addLine(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public ArrayList<String> getIgnores() {
        return ignoreWords;
    }
    public ArrayList<String> getLines() {
        return lines;
    }
    public ArrayList<ArrayList<String>> getWords() {
        return words;
    }

    public void addLine(String line) {
        lines.add(line);
        words.add(splitLine(line));
    }

    private ArrayList<String> splitLine(String line) {
        return new ArrayList<String>(Arrays.asList(line.split(" ")));
    }

    public String printLine(){
        String line = "";
        for(int i=0;i<this.lines.size();i++){
            //System.out.println(linesKey.get(i).line);
            line+=lines.get(i);
            line+="\n";
        }
        line = line.substring(0,line.length() - 1);
        return line;
    }
}