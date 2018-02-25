import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class SpaceComplexity41{

  public static int sum(int n){
    if (n<=0) {
      return 0;
    }
    return n + sum(n-1);
  }

  public static int pairSum(int a, int b){
    return a+b;
  }

  public static int pairSumSequence(int n){
    int sum=0;
    for (int i=0; i<n; i++){
      sum += pairSum(i, i + 1);
    }
    return sum;
  }

  public static void main(String[] args){


    int res = sum(5);

    /*
    sum
    time complexity : O(n)
    space complexity : O(n) each cell stack adds to the memory
    function calls : O(n)
    */

    int res2 = pairSumSequence(5);

    /*
    pairSumSequence
    time complexity : O(n)
    space complexity : O(1) because calls do not exist simultaneously on the call stack.
    function calls for pairSum: O(n)
    */


    System.out.print(res + "\n");
    System.out.print(res2 + "\n");


  }

}
