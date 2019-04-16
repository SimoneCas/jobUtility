package it.sample.java.circuitbreaker;

public class RemoteSystemMock {

	private int invocationCounter = 0;
	private int invocationCounterOK = 0;
	private int invocationCounterKO = 0;
	
	private int numKOResponse = 0;
	
	public void resetCounters() {
		this.invocationCounter = 0;
		this.invocationCounterKO = 0;
		this.invocationCounterOK = 0;
		this.numKOResponse = 0;
	}
	
	public int getInvocationCounter() {
		return invocationCounter;
	}

	public int getInvocationCounterOK() {
		return invocationCounterOK;
	}

	public int getInvocationCounterKO() {
		return invocationCounterKO;
	}

	public int getNumKOResponse() {
		return numKOResponse;
	}

	public void setNumKOResponse(int numKOResponse) {
		this.numKOResponse = numKOResponse;
	}

	public String invoke(String request) {
		invocationCounter++;
		if (invocationCounter > numKOResponse) {
			invocationCounterOK++;
			return "OK";
		} else {
			invocationCounterKO++;
			throw new RuntimeException();
		}
	}
}
