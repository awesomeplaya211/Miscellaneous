// Another FizzBuzz challenge, but this time in Java
public class FizzBuzz {
  public static void main(String[] args) {
    for (int i = 0; i <= 100; i++) {
      String string = "";
      boolean isDivisible = false;
      if (i % 3 == 0) {
        string += "Fizz";
        isDivisible = true;
      }
      if (i % 5 == 0) {
        string += "Buzz";
        isDivisible = true;
      }
      if (isDivisible) {
        System.out.println(string);
        continue;
      }
      System.out.println(i);
    }
  }
}
