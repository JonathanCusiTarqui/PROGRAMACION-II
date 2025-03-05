/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practica3;

/**
 *
 * @author HP
 */
public class cola {
    private int inicio;
    private int fin;
    private int max;
    private String arreglo[];
    
    public cola(int n){
        this.arreglo = new String[n+1];
        this.inicio = 0;
        this.fin = 0;
        this.max = n;
        
    }
    
    public void adicionar(String d){
        if (this.fin==this.max){
            System.out.println("cola llena");
        }
    }
    
    public String eliminar(){
        if (this.inicio==0){
            return "vacio";
        }else{
            this.inicio=this.inicio+1;
            String dato = arreglo[this.inicio];
            if (this.inicio==this.fin){
                this.inicio=0;
                this.fin=0;
            }
            return dato;
        }
    }
    
    public String peek(){
        String dato= arreglo[this.inicio+1];
        return dato;
    }
    
    public boolean isEmpty(){
        if(this.inicio==0 && this.fin==0){
            return true;
        }else{
            return false;
        }
    }
    
    public boolean isFull(){
        if(this.fin==this.max){
            return true;
        }else{
            return false;
        }
    }
}
