import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class trickyRecursive44{

  public static int f(int n){
    if (n<=1){
      return 1;
    }
    return f(n-1) + f(n-1);
  }

  public static int fibonacci(int n){
    if (n<=2){
      return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
  }


  public static void main(String[] args){

    int res = f(4);
    /*
    f
    total time : O(n), thinking about depth.
    total space : O(n), because essentially spaces for results of f(n)....1 are needed.
    function calls : 2^n+1 - 1 = 2^0 + 2^1 + ... + 2^n
    */

    int res2 = fibonacci(4);
    /*
    fibonacci
    total time : O(2^n) because recursive solution.
    total space : O(n), just for storing result of each fibonnaci(n....1)
    function calls : O(n-1) + O(n-2) + 1 = 2*fibonacci(n) - 1
    */

    System.out.print(res + "\n");
    System.out.print(res2+ "\n");
  }
}
