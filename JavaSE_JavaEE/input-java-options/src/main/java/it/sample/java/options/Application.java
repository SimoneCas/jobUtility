package it.sample.java.options;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

public class Application {

	public static void main(String[] args) {
		String setPasswordOptionLabel = "setPassword";
		String healthCheckOptionLabel = "healthCheck";
		
		Options options = new Options();
       
		Option setPasswordOption = new Option(setPasswordOptionLabel, setPasswordOptionLabel, false, "Abilita funzione inserimento password");
        setPasswordOption.setRequired(false);
        options.addOption(setPasswordOption);
        
        Option healthCheckOption = new Option(healthCheckOptionLabel, healthCheckOptionLabel, false, "Funzionalità di test");
        healthCheckOption.setRequired(false);
        options.addOption(healthCheckOption);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd = null;

        try {
            cmd = parser.parse(options, args);
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("utility-name", options);

            System.exit(1);
        }

        boolean hasSetPasswordOption = cmd.hasOption(setPasswordOptionLabel);

        System.out.println("Option abilitata = " + hasSetPasswordOption);
        
        if(cmd.hasOption(healthCheckOptionLabel)) {
        	System.out.println("Test Client");
        }
        
        if(hasSetPasswordOption) {
        	//TODO: lettura password da shell
        	
        }
        
        

	}

}
