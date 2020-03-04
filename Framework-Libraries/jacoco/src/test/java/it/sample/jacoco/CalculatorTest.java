package it.sample.jacoco;

import org.junit.Assert;
import org.junit.Test;

public class CalculatorTest {

	@Test
	public void testSum() {
		Calculator calculator = new Calculator();
		int sum = calculator.sum(8, 9);
		Assert.assertEquals(17, sum);
	}
	
	@Test
	public void testDiff() {
		Calculator calculator = new Calculator();
		int diff = calculator.diff(8, 9);
		Assert.assertEquals(1, diff);
	}
}
