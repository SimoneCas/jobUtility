package initial;

import java.io.FileNotFoundException;
import java.io.IOException;

import controller.WorkFile;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        try{
        	if(args[0].length()==0)
        		throw new Exception();
        }catch(Exception e){
        	System.out.println("Nome file da modificare errato. "
        			+ "Lanciare il programma con un parametro "
        			+ "che indica il nome del file da modificare, "
        			+ "comprensivo di estensione");
        }
    	String nameFile = args[0];
        System.out.println("Nome File: "+nameFile);

        try {
			WorkFile.workFile(nameFile);
		} catch (FileNotFoundException e) {
			System.out.println("Errore durante l'apertura del file "+ nameFile);
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("Errore durante la generazione del nuovo file");
			e.printStackTrace();
		}
		
    }
}
