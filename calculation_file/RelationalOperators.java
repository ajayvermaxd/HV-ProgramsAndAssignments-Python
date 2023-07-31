public class RelationalOperators {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;

        boolean equal = (num1 == num2);
        boolean notEqual = (num1 != num2);
        boolean greaterThan = (num1 > num2);
        boolean lessThan = (num1 < num2);

        System.out.println("Equal: " + equal);
        System.out.println("Not Equal: " + notEqual);
        System.out.println("num1 is Greater Than num2: " + greaterThan);
        System.out.println("num1 is Less Than num2: " + lessThan);
    }
}
