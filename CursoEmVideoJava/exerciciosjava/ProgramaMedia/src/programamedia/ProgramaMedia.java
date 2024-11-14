/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package programamedia;

import java.util.Scanner;

/**
 *
 * @author andre
 */
public class ProgramaMedia {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o ano de nasscimento:");
        
        int nasc = teclado.nextInt();
        int i = 2023 - nasc ;
        System.out.println("Sua idade é " + i);
        if (i>=18){
            System.out.println("MAIOR DE IDADE");
        }
        else {
            System.out.println("MENOR DE IDADE");
        }
        
    }
    
}
