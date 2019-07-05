package it.sample.java.clientpool;

import javax.inject.Inject;
import javax.ws.rs.client.Client;

import org.apache.commons.pool2.impl.GenericObjectPoolConfig;

public class SpecificClientRegistry extends AbstractClientRegistry{

	private int poolMinIdle = 10;
	private int poolMaxIdle = 20;
	private int poolMaxTotal = 150;
	
	@Inject
	private SpecificClientFactory clientFactory;
	
	public void setClientFactory(SpecificClientFactory clientFactory) {
		this.clientFactory = clientFactory;
	}

	@Override
	protected AbstractRestClientFactory getRestClientFactory() {
		return clientFactory;
	}
	
	@Override
	protected GenericObjectPoolConfig<Client> configuration() {
		GenericObjectPoolConfig<Client> config = new GenericObjectPoolConfig<>();
		config.setMinIdle(poolMinIdle);
		config.setMaxIdle(poolMaxIdle);
		config.setMaxTotal(poolMaxTotal);
		return config;
	}
}
