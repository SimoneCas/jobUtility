package it.sample.java.clientpool;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;

import org.apache.commons.pool2.BasePooledObjectFactory;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.impl.DefaultPooledObject;

public abstract class AbstractRestClientFactory extends BasePooledObjectFactory<Client>{

	@Override
	public Client create() throws Exception {
		Client newClient = ClientBuilder.newClient();
		configureClient(newClient);
		return newClient;
	}
	
	protected abstract void configureClient(Client client);

	@Override
	public PooledObject<Client> wrap(Client client) {
		return new DefaultPooledObject<>(client);
	}

	@Override
	public void destroyObject(PooledObject<Client> p) throws Exception {
		p.getObject().close();
		super.destroyObject(p);
	}
}
