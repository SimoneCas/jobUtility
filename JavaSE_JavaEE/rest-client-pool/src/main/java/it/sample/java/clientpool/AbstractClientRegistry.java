package it.sample.java.clientpool;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.ws.rs.client.Client;

import org.apache.commons.pool2.ObjectPool;
import org.apache.commons.pool2.impl.GenericObjectPool;
import org.apache.commons.pool2.impl.GenericObjectPoolConfig;

public abstract class AbstractClientRegistry {

	private ObjectPool<Client> pool;
	
	protected abstract AbstractRestClientFactory getRestClientFactory();
	
	protected abstract GenericObjectPoolConfig<Client> configuration();
	
	@PostConstruct
	public void init() {
		pool = new GenericObjectPool<Client>(getRestClientFactory(), configuration());
	}
	
	public PooledRestClient borrow() {
		try {
			return new PooledRestClient(pool);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	@PreDestroy
	public void close() {
		pool.close();
	}
}
