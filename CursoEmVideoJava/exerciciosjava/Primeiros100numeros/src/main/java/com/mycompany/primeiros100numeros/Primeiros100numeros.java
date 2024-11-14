
package com.mycompany.primeiros100numeros;
import javax.swing.JOptionPane;
public class Primeiros100numeros {

    public static void main(String[] args) {
         
        String msg = "os cem primeiros numéros são: \n";
       
        int num = 0;
        
        
      while (num <= 100){
      
        if (num == 100){
             
            msg += num + ".";
         
        }else{
         
            msg += num + ",";
            
        } 
      
       //System.out.println(num);
       
       num++;
      
      }	
      
        JOptionPane.showMessageDialog(null, msg);
        
        

    }
}
