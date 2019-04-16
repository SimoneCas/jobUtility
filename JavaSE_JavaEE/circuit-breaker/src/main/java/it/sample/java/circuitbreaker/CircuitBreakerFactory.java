package it.sample.java.circuitbreaker;

import java.util.function.Function;

import javax.inject.Inject;

public class CircuitBreakerFactory {
	@Inject private CircuitBreakerDelegate delegate;
	
	public void setCircuitBreakerDelegate(CircuitBreakerDelegate delegate) {
		this.delegate = delegate;
	}

	public <T,R> CircuitBreaker<T,R> createFor(Function<T,R> f) {
		return new CircuitBreaker<>(delegate, f);
	}
	
}
