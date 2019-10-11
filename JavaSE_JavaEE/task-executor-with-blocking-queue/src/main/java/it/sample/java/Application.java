package it.sample.java;

public class Application {

	public static void main(String[] args) {
		//Esempio di utilizzo del KeyBasedExecutor
		Integer[] partitionKeys = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		
		for(int i=0; i<100; i++) {
			int index = i%10;
			int j = i;
			KeyBasedExecutor.INSTANCE.submit(partitionKeys[index], () -> print(index + " - "  + j));
		}
	}

	private static Object print(String string) {
		System.out.println(string);
		return null;
	}

}
