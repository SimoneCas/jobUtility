package controller;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class WorkFile {
	// FileNotFoundException
	public static void workFile(String fileInput) throws FileNotFoundException, IOException {
		File fInput = new File(fileInput);

		FileReader frInput = new FileReader(fInput);
		BufferedReader bfInput = new BufferedReader(frInput);
		System.out.println("Aperto file " + fileInput);

		int sizeNameFile = fileInput.length();
		String logicNameFile = fileInput.substring(0, sizeNameFile - 4);

		File fOutput = new File(logicNameFile + ".csv");
		fOutput.createNewFile();
		System.out.println("Creato file " + fOutput.getName());
		PrintWriter pfOutput = new PrintWriter(fOutput);

		String line;
		int count = 1;
		while ((line = bfInput.readLine()) != null) {
			if (line.length() > 2) {
				System.out.println("DEBUG 1 " + line);
				line = line.substring(1);
				System.out.println("DEBUG 2 " + line);
				int sizeLine = line.length();
				line = line.substring(0, sizeLine - 1);
				System.out.println("DEBUG 3 " + line);
				pfOutput.println(line);

				pfOutput.flush();
			}
			System.out.println("Scritta riga " + count);
			count++;
		}
		pfOutput.close();
		bfInput.close();
		System.out.println("Conclusa lavorazione file");
	}
}
