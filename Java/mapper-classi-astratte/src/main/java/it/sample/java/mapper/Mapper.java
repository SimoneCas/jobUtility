package it.sample.java.mapper;

public interface Mapper<S,T> {

	T map(S source);
	
}
