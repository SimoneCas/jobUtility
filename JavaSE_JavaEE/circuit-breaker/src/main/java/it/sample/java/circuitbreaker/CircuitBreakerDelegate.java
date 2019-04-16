package it.sample.java.circuitbreaker;

import javax.inject.Inject;
import javax.inject.Singleton;

@Singleton
public class CircuitBreakerDelegate {
	@Inject private CircuitBreakerConfig config;
	private int errorCount = 0;
	private long lastError = 0;
	
	public void setConfig(CircuitBreakerConfig config) {
		this.config = config;
	}

	public boolean shouldTry() {
		int currErrorCount;
		long currLastError;
		synchronized (this) {
			currErrorCount = this.errorCount;
			currLastError = this.lastError;
		}
		long now = System.currentTimeMillis();
		long currMaxErrorDelay = getErrorDelay(currErrorCount);
		long currErrorDelay = now - currLastError;
		boolean result = (currErrorCount < getMaxError()) || (currErrorDelay > currMaxErrorDelay);
		return result;
	}
	
	public synchronized void reset() {
		lastError = 0;
		errorCount = 0;
	}
	
	public synchronized void success() {
		lastError = 0;
		errorCount = 0;
	}
	
	public synchronized void error() {
		lastError = System.currentTimeMillis();
		errorCount++;
	}

	private int getMaxError() {
		return config.getMaxError();
	}

	private long getErrorDelay(int currErrorCount) {
		return Math.min(config.getMaxErrorDelay(), (currErrorCount-config.getMaxError()+1)*config.getErrorDelay());
	}
	
}
