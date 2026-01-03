

public class BMI {
    private float weight;
    private float heigth;
    public BMI(float weight, float heigth){
        this.heigth = heigth;
        this.weight = weight;
    }
    public float GetBMI(){
        float bmi = (float) (this.weight/Math.pow(heigth, 2.0f));
        return bmi;
        
    }
    
}
