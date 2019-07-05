package it.sample.java.clientpool;

import java.io.Closeable;
import java.io.IOException;

import javax.ws.rs.client.Client;

import org.apache.commons.pool2.ObjectPool;

public class PooledRestClient  implements Closeable {

	private Client client;
	private ObjectPool<Client> pool;
	
	public PooledRestClient(ObjectPool<Client> pool) throws Exception {
		this.client = pool.borrowObject();
		this.pool = pool;
	}
	
	public Client getClient() {
		return client;
	}

	@Override
	public void close() throws IOException {
		try {
			pool.returnObject(client);
		} catch(Exception e) {
			throw new RuntimeException(e);
		}
	}
}
