/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package livrodenotas;

import javax.swing.JOptionPane;

/**
 *
 * @author andre
 */
public class Teste {
   public static void main (String[] args){
    LivroDeNotas livroDeNotas = new LivroDeNotas();
    String nomeDoCurso = JOptionPane.showInputDialog("Prof, qual o nome do curso?");
    livroDeNotas.exibirMensagem(nomeDoCurso);
} 
}
