package nz.ac.massey.cs.pp.tutorial6.id15398663;

public class student {
    public String student_id = null;
    public String name = null;
    public String fname = null;
    public String program = null;
    public String major = null;
    public student(){

    }

    @Override
    public String toString(){
        return this.student_id + "," + this.fname + "," + this.name + "," + this.major + "," + this.program + "\n";
    }

}
