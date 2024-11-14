/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package comparacaostring;

/**
 *
 * @author andre
 */
public class ComparacaoString {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       String nome1 = "Andrey";
       String nome2 = "Andrey";
       String nome3 = new String("Andrey");
       String res;
       res = (nome1.equals(nome3))?"igual":"diferente";
        System.out.println(res); 
    }
    
}
