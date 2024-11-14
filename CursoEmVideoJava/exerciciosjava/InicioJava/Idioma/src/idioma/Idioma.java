package idioma;


import java.util.Locale;

public class Idioma {

    public static void main(String[] args) {

        Locale loc = Locale.getDefault();

        String idioma = loc.toString();

        System.out.println("Seu sistema está em " + idioma);
        System.out.println("Seu sistema esta em " + loc.toString());
    }    
}