package it.sample.java.clientpool;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class TestClientPool {

	private SpecificClientRegistry clientRegistry;

	@Before
	public void init() {
		SpecificClientFactory clientFactory = new SpecificClientFactory();

		clientRegistry = new SpecificClientRegistry();
		clientRegistry.setClientFactory(clientFactory);
		clientRegistry.init();
	}

	@After
	public void release() {
		clientRegistry.close();
	}

	/*
	 * Utilizzo sempre lo stesso client perchè le richieste del client sono sequenziali e ogni volta chiudo il pooledClient ricevuto.
	 */
	@Test
	public void testClientPoolInvocation() throws IOException {
		Set<String> clients = new HashSet<>();
		for (int i = 0; i < 100; i++) {
			PooledRestClient pooledClient = clientRegistry.borrow();
			System.out.println("Client " + pooledClient.getClient());
			clients.add(pooledClient.getClient().toString());
			//Response response = pooledClient.getClient().target("http://fake-endpoint").request().get();
			
			pooledClient.close();
		}
		System.out.println("Clients used " + clients.size());
		Assert.assertEquals(1, clients.size());
	}
	
	/*
	 * Utilizzo ogni volta un nuovo client presente nel pool perchè non chiudo mai il pooledClient ricevuto
	 */
	@Test
	public void testMultiClientPoolInvocation() throws IOException {
		Set<String> clients = new HashSet<>();
		for (int i = 0; i < 100; i++) {
			PooledRestClient pooledClient = clientRegistry.borrow();
			System.out.println("Client " + pooledClient.getClient());
			clients.add(pooledClient.getClient().toString());
			//Response response = pooledClient.getClient().target("http://fake-endpoint").request().get();
		}
		System.out.println("Clients used " + clients.size());
		Assert.assertEquals(100, clients.size());
	}
	
	/*
	 * Tipico utilizzo:
	 * try (PooledRestClient pooledClient = clientRegistry.borrow()) {
	 * 	pooledClient.getClient().target("http://fake-endpoint").request().get();
	 * }
	 */
}
