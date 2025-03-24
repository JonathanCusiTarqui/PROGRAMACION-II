import java.util.Scanner;

//MODULAR ESTRUCTURA

public class EcuacionCuadraticaModular {

    public static double getDiscriminante(double a, double b, double c) {
        return b * b - 4 * a * c;
    }

    public static double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public static double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese a, b, c: ");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        scanner.close();

        double discriminante = getDiscriminante(a, b, c);

        if (discriminante > 0) {
            double raiz1 = getRaiz1(a, b, discriminante);
            double raiz2 = getRaiz2(a, b, discriminante);
            System.out.println("La ecuacion tiene dos raices " + raiz1 + " y " + raiz2);
        } else if (discriminante == 0) {
            double raiz = getRaiz1(a, b, discriminante);
            System.out.println("La ecuacion tiene una raiz " + raiz);
        } else {
            System.out.println("La ecuacion no tiene raices reales");
        }
    }
}


//POO

/*

public class EcuacionCuadraticaPOO {

    static class EcuacionCuadratica {
        private double a;
        private double b;
        private double c;

        public EcuacionCuadratica(double a, double b, double c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public double getDiscriminante() {
            return b * b - 4 * a * c;
        }

        public double getRaiz1() {
            double discriminante = getDiscriminante();
            return (-b + Math.sqrt(discriminante)) / (2 * a);
        }

        public double getRaiz2() {
            double discriminante = getDiscriminante();
            return (-b - Math.sqrt(discriminante)) / (2 * a);
        }

        @Override
        public String toString() {
            double discriminante = getDiscriminante();
            if (discriminante > 0) {
                return "La ecuacion tiene dos raices " + getRaiz1() + " y " + getRaiz2();
            } else if (discriminante == 0) {
                return "La ecuaciOn tiene una raiz " + getRaiz1();
            } else {
                return "La ecuaciOn no tiene raices reales";
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese a, b, c: ");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        scanner.close();

        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);
        System.out.println(ecuacion);
    }
} 

 */