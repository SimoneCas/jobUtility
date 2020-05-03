package it.sample.java.optional;

public class Person {

	private String name = null;

	public Person() {
		
	}
	
	public Person(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "Person [name=" + name + "]";
	}
	
	public static Person getInstance() {
		Person person = new Person();
		person.setName("simone");
		return person;
	}
}
