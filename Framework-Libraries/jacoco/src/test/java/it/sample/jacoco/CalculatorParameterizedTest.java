package it.sample.jacoco;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.Collection;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(Parameterized.class)
public class CalculatorParameterizedTest {

	private int operator1;
	private int operator2;
	private double expectedResult;
	private Exception exception;

	public CalculatorParameterizedTest(int operator1, int operator2, double expetedResult, Exception exception) {
		this.operator1 = operator1;
		this.operator2 = operator2;
		this.expectedResult = expetedResult;
		this.exception = exception;
	}

	@Parameters(name = "{index}: CalculatorParameterizedTest({0},{1})={2}, throws {3}")
	public static Collection<Object[]> data() {
		return Arrays.asList(
				new Object[][] { { 10, 10, 1, null }, { 10, 5, 2, null }, { 10, 0, 0, new ArithmeticException() } });
	}

	@Test
	public void testCalculator() {
		Calculator c = new Calculator();
		try {
			double result = c.div(operator1, operator2);

			if (this.exception != null) {
				fail("should have thrown an exception: " + exception);
			}
			assertEquals(expectedResult, result, 0.000001);
		} catch (Exception e) {
			if (this.exception == null) {
		        fail("should not have thrown an exception, but threw " + e);
		      }
			
			if (!this.exception.getClass().equals(e.getClass())) {
		        fail("expected exception " + this.exception + "; got exception " + e);
		      }
		}

	}
}
