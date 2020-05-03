package it.sample.java.optional;

import java.util.Optional;

public class Application {

	private static final String DEFAULT_VALUE = "name";

	public static void main (String[] args) {
		
		//Per evitare controlli sui null si può ricorrere all'uso di Optional
		Person person = Person.getInstance();
		Optional<String> optName = Optional.ofNullable(person.getName());
		
		//get default value in caso di null
		Optional<String> optNullName = Optional.ofNullable(null);
		String name1 = optNullName.orElse(DEFAULT_VALUE);
		System.out.println(name1);
		
		//ritorna il valore se presente altrimenti Exception
		String name2 = optName.get();
		System.out.println(name2);
		
		Optional<String> name3 = optName.filter(value -> value.length() > 3).map(value -> value.toUpperCase());
		System.out.println(name3.get());
		
		boolean present = optName.isPresent();
		System.out.println("Is Presente: " + present);
	}
}
