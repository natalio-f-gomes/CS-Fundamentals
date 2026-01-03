public class TwoSum {
    public static void main(String[] args) {

        int[] array = {1,2,3,4,5,6,7,8,9,0};
        int[] result =  sumNums(array,10);
        for(int i: result){
            System.out.println(i);
        }
    }
    public static int[] sumNums(int[] array, int result){
        int[] nums = new int[2];
        for(int i : array){
            for(int j : array){
                if(!(array[i] == array[j])){
                    if(i + j== result){
                        nums[0] = i;
                        nums[1] = j;
                    }
                }
            }
        }
        return nums;
    }
}

