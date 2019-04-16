package it.sample.java.circuitbreaker;

import javax.inject.Singleton;

@Singleton
/*
 * Classe che restituisce le configurazione del CircuitBreaker.
 * Per utilizzo in progetti rendere configurabile a runtime parametri tramite lettura su file o in cache o su database
 */
public class CircuitBreakerConfig {
	private static final int MAX_ERROR = 10;
	private static final long ERROR_DELAY = 1000;
	private static final long MAX_ERROR_DELAY = 100000;
	private int maxError = MAX_ERROR;
	private long errorDelay = ERROR_DELAY;
	private long maxErrorDelay = MAX_ERROR_DELAY;
	
	public int getMaxError() {
		return maxError;
	}
	
	public long getErrorDelay() {
		return errorDelay;
	}
	
	public long getMaxErrorDelay() {
		return maxErrorDelay;
	}
	
}
