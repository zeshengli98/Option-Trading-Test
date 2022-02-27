import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class InputTest {

    @Test
    void inputKeyword() {
        Input input = new Input();
        input.inputfile("/Users/zesheng.li/IdeaProjects/fintech512-assignment2-KWIC/src/main/resources/sample.txt");
        //assertEquals(input.getIgnores(),2);
        String inputStr = "Descent of Man" + "\n"+
                "The Ascent of Man"+ "\n"+
                "The Old Man and The Sea"+ "\n"+
                "A Portrait of The Artist As a Young Man"+ "\n"+
                "A Man is a Man but Bubblesort IS A DOG";

        assertEquals(input.printLine(),inputStr);

    }
}