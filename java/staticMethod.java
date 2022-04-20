// Method가 instance 소속일 경우 -> static을 넣으면 안된다.
// Method가 class 소속일 경우 -> static이 있어야 한다.

class Print{
    public String delimiter;
    public void a() {
        System.out.println(this.delimiter);
        System.out.println("a");
        System.out.println("a");
    }
    public void b() {
        System.out.println(this.delimiter);
        System.out.println("b");
        System.out.println("b");

    }
    public static void c(String delimiter) {
        System.out.println(delimiter);
        System.out.println("b");
        System.out.println("b");
    }
}
public class staticMethod {

    public static void main(String[] args) {
//      Print.a("-");
//      Print.b("-");

        // instance
        Print t1 = new Print();
        t1.delimiter = "-";
        t1.a(); // 인스턴스 소속
        t1.b();
        Print.c("$"); // 클래스 소속


//      Print.a("*");
//      Print.b("*");

        Print t2 = new Print();
        t2.delimiter = "*";
        t2.a();
        t2.b();
    }


}