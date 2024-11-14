
package poo02;

public class Caneta {
    String modelo;
    String cor;
    float ponta;
    int carga;
    boolean tampada;
    
    public void status(){
        System.out.println("Uma caneta" + this.cor );
        System.out.println("Está tampada? " + this.tampada);
    }
    
    public void rabiscar(){
        if(tampada == true){
            System.out.println("Erro, a caneta está tampada");
        }
        else{
            System.out.println("Rabiscado");
        }
    }
    
    public void tampar(){
        this.tampada = true;
    }
    public void destampar(){
        this.tampada = false;
    }
}
