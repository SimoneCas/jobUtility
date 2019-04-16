package it.sample.java.circuitbreaker;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class CircuitBreakerTest {

	private CircuitBreakerFactory factory;

	@Before
	public void init() {
		this.factory = new CircuitBreakerFactory();
		CircuitBreakerDelegate delegate = new CircuitBreakerDelegate();
		delegate.setConfig(new CircuitBreakerConfig());
		this.factory.setCircuitBreakerDelegate(delegate);

	}

	@Test
	public void testCircuitBreakerNoError() {
		RemoteSystemMock remoteSystem = new RemoteSystemMock();
		remoteSystem.setNumKOResponse(0);
		int numInvocation = 0;
		boolean continueLoop = true;

		while (continueLoop) {
			try {
				numInvocation++;
				String response = factory.createFor(remoteSystem::invoke).applyProtected("requestPayload");

				System.out.println("**** Remote response ok " + response);
				continueLoop = false;
			} catch (RuntimeException e) {
				System.out.println("Exception by remote system");
			}
		}
		
		Assert.assertEquals(1, numInvocation);
	}
	
	@Test
	public void testKoAndCircuitBreakerNotCloseConnection() {
		RemoteSystemMock remoteSystem = new RemoteSystemMock();
		remoteSystem.setNumKOResponse(5);
		int numInvocation = 0;
		int numBrokenCircuitException = 0;
		boolean continueLoop = true;

		while (continueLoop) {
			try {
				numInvocation++;
				String response = factory.createFor(remoteSystem::invoke).applyProtected("requestPayload");

				System.out.println("**** Remote response ok " + response);
				continueLoop = false;
			} catch (BrokenCircuitException e) {
				numBrokenCircuitException++;
				continueLoop = false;
			} catch (RuntimeException e) {
				System.out.println("Exception by remote system");
			}
		}
		Assert.assertEquals(0, numBrokenCircuitException);
		Assert.assertEquals(6, numInvocation);
	}
	
	@Test
	public void testKoAndCircuitBreakerCloseConnection() {
		RemoteSystemMock remoteSystem = new RemoteSystemMock();
		remoteSystem.setNumKOResponse(10);
		int numInvocation = 0;
		int numBrokenCircuitException = 0;
		boolean continueLoop = true;

		while (continueLoop) {
			try {
				numInvocation++;
				String response = factory.createFor(remoteSystem::invoke).applyProtected("requestPayload");

				System.out.println("**** Remote response ok " + response);
				continueLoop = false;
			} catch (BrokenCircuitException e) {
				numBrokenCircuitException++;
				continueLoop = false;
			} catch (RuntimeException e) {
				System.out.println("Exception by remote system");
			}
		}
		Assert.assertEquals(1, numBrokenCircuitException);
		Assert.assertEquals(11, numInvocation);
	}
	
	@Test
	public void testCircuitBreakerReOpenConnectionAfterKO() throws InterruptedException {
		RemoteSystemMock remoteSystem = new RemoteSystemMock();
		remoteSystem.setNumKOResponse(10);
		int numInvocation = 0;
		int numBrokenCircuitException = 0;
		boolean continueLoop = true;

		while (continueLoop) {
			try {
				numInvocation++;
				String response = factory.createFor(remoteSystem::invoke).applyProtected("requestPayload");

				System.out.println("**** Remote response ok " + response);
				continueLoop = false;
			} catch (BrokenCircuitException e) {
				numBrokenCircuitException++;
				Thread.sleep(2000l);
			} catch (RuntimeException e) {
				System.out.println("Exception by remote system");
			}
		}
		Assert.assertEquals(1, numBrokenCircuitException);
		Assert.assertEquals(12, numInvocation);
	}

}
