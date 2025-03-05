/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practica3;

/**
 *
 * @author HP
 */
public class pila {
    private float arreglo[];
    private int top;
    private int n;
    
    public pila(int n){
        this.top = 0;
        this.n = n;
        arreglo = new float[n+1];
            
    }
    
    public void push(float e){
        this.top =this.top+1;
        arreglo[this.top+1]= e;
        
    }
    
    public float pop(){
        float dato = 0;
        dato = arreglo[this.top];
        this.top = this.top-1;
        return dato;
    }
    
    public float peek(){
        return arreglo[this.top];
    }
    
    public boolean isEmpty(){
        if(this.top == 0){
            return true;
        }else{
            return false;
        }
    }
    public boolean isFull(){
        if(this.top == n){
            return true;
        }else{
            return false;
        } 
    }
        
}
