import java.util.ArrayList;
public class Stack {
    private ArrayList<String> stack;

    public Stack(){
        this.stack = new ArrayList<>();
    }

    public boolean isEmpty(){
        if(this.stack.size() == 0){
            return true;
        }
        else{
            return false;
        }
    }
}
