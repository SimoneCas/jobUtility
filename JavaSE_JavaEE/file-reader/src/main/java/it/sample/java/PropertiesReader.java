package it.sample.java;

import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Properties;

public class PropertiesReader {

	public static void main(String[] args) {
		String externalConfigPath;
		//utilizzato solo per test il path assoluto estratto a partire dal file presente nella cartella src/main/resources
		externalConfigPath = "externalConfig.property";

		try {
			if (Files.exists(Paths.get(ClassLoader.getSystemResource(externalConfigPath).toURI()))) {
				try (InputStream stream = new FileInputStream(ClassLoader.getSystemResource(externalConfigPath).toURI().getPath())) {

					Properties properties = new Properties();
					properties.load(stream);

					// Verifica delle properties caricate
					System.out.println("Name = " + properties.getProperty("name"));
					System.out.println("Version = " + properties.getProperty("version"));
				} catch (Exception e) {
					System.out.println("Exception");
				}
			} else {
				System.out.println("File not found");
			}
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
