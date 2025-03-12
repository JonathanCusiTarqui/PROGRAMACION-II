public class FiguraGeometrica {

    public static double area(double radio) {
        return Math.PI * Math.pow(radio, 2);  // Área del círculo
    }

    public static double area(double base, double altura) {
        return base * altura;  // Área del rectángulo
    }

    
    public static double areaTriangulo(double base, double altura) {
        return (base * altura) / 2;  // Área del triángulo rectángulo
    }

    public static double area(double baseMayor, double baseMenor, double altura) {
        return (baseMayor + baseMenor) * altura / 2;  // Área del trapecio
    }

    
    public static double areapentagono(double lado, double apotema) {
        return 5 * lado * apotema / 2;  // Área del pentágono
    }
   
    public static void main(String[] args) {
        // Imprimir resultados
        System.out.println(area(5));  // Círculo
        System.out.println(area(4, 6));  // Rectángulo
        System.out.println(areaTriangulo(3, 5));  // Triángulo rectángulo
        System.out.println(area(8, 6, 5));  // Trapecio
        System.out.println(areapentagono(7, 4.8));  // Pentágono
    }
}