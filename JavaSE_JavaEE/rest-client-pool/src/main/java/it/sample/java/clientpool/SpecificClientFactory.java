package it.sample.java.clientpool;

import javax.ws.rs.client.Client;

import org.glassfish.jersey.client.ClientProperties;

public class SpecificClientFactory extends AbstractRestClientFactory {
	
	private int connectTimeout = 100; //in milliseconds
	private int readTimeout = 400; //in milliseconds
	
	@Override
	protected void configureClient(Client client) {
		
		//Timeout property è specifica per implementazione
		client.property(ClientProperties.CONNECT_TIMEOUT, connectTimeout);
		client.property(ClientProperties.READ_TIMEOUT, readTimeout);
	}
}
