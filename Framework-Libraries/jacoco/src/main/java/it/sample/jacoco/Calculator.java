package it.sample.jacoco;

public class Calculator {

	public int sum(int a, int b) {
		return a + b;
	}
	
	public int diff(int a, int b) {
		if (a < b) {
			return b - a;
		} else {
			return a - b;
		}
	}
	
	public double div(int a, int b) {
		//if (b == 0) {
			//return 0;
		//} else {
			return a/b;
	//	}
	}
}
