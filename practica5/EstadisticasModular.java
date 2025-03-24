//MODULAR-ESTRUCTURA
import java.util.Scanner;

public class EstadisticasModular {

    public static double promedio(double[] lista) {
        double suma = 0;
        for (double num : lista) {
            suma += num;
        }
        return suma / lista.length;
    }

    public static double desviacion(double[] lista, double prom) {
        double sumatoria = 0;
        for (double num : lista) {
            sumatoria += Math.pow(num - prom, 2);
        }
        return Math.sqrt(sumatoria / (lista.length - 1));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[10];

        System.out.println("Ingrese num");
        for (int i = 0; i < 10; i++) {
            numeros[i] = scanner.nextDouble();
        }
        scanner.close();

        double promedioCalculado = promedio(numeros);
        double desviacionCalculada = desviacion(numeros, promedioCalculado);

        System.out.printf("El promedio es %.2f%n", promedioCalculado);
        System.out.printf("La desviacion estandar es %.5f%n", desviacionCalculada);
    }
}


//POO

/*


public class EstadisticasPOO {
    static class Estadisticas {
        private double[] lista;

        public Estadisticas(double[] lista) {
            this.lista = lista;
        }
        public double promedio() {
            double suma = 0;
            for (double num : lista) {
                suma += num;
            }
            return suma / lista.length;
        }
        public double desviacion() {
            double prom = promedio();
            double sumatoria = 0;
            for (double num : lista) {
                sumatoria += Math.pow(num - prom, 2);
            }
            return Math.sqrt(sumatoria / (lista.length - 1));
        }
        @Override
        public String toString() {
            return String.format("El promedio es %.2f%nLa desviaciOn estandar es %.5f", promedio(), desviacion());
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[10];

        System.out.println("Ingrese num:");
        for (int i = 0; i < 10; i++) {
            numeros[i] = scanner.nextDouble();
        }
        scanner.close();

        Estadisticas estadisticas = new Estadisticas(numeros);
        System.out.println(estadisticas);
    }
}
 */