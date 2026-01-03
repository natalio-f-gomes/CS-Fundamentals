public class Calculator {

    public int[][] store(int[] nums1, int[] nums2 ){
      int[][] multiArray = {nums1, nums2};
      for(int i: multiArray[0]){

          for(int j: multiArray[1])

          System.out.println(i+" - " +j);
      }
        return multiArray;
    }
}
