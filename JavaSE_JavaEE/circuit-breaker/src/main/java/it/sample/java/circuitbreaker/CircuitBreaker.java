package it.sample.java.circuitbreaker;

import java.util.function.Function;

public class CircuitBreaker<T,R> {
	private CircuitBreakerDelegate delegate;
	private Function<T,R> f;
	
	public CircuitBreaker(CircuitBreakerDelegate delegate, Function<T,R> f) {
		this.delegate = delegate;
		this.f = f;
	}

	public R applyProtected(T t) {
		if (!delegate.shouldTry()) {
			System.out.println("CircuitBreaker is currently closed");
			throw new BrokenCircuitException();
		}
		try {
			R result = f.apply(t);
			delegate.success();
			return result;
		} catch(Throwable e) {
			delegate.error();
			throw new RuntimeException(e);
		}
	}
	
}
