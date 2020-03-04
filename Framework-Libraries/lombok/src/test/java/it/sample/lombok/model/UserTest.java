package it.sample.lombok.model;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

import org.junit.Test;
import org.junit.Assert;

import lombok.NonNull;

public class UserTest {

	private static final Integer AGE = 25;
	private static final @NonNull BigInteger BANK_AMOUND = BigInteger.valueOf(256987);
	private static final @NonNull String ID = "ZK-25698745";
	private static final String NAME = "Jones";
	private static final String SURNAME = "Red";

	@Test
	public void testGetAndSetId(){
		User user = this.createDefaultUser();
		
		Assert.assertEquals(ID, user.getId());
		String newId = "890";
		user.setId(newId);
		Assert.assertEquals(newId, user.getId());
	}
	
	@Test
	public void testGetAndSetName(){
		User user = this.createDefaultUser();
		
		Assert.assertEquals(NAME, user.getName());
		String newName = "Patrick";
		user.setName(newName);
		Assert.assertEquals(newName, user.getName());
	}

	
	private User createDefaultUser(){
		User user = new User();
		user.setAge(AGE);
		user.setBankAmount(BANK_AMOUND);
		user.setId(ID);
		user.setName(NAME);
		List<String> orderIds = new ArrayList<>();
		orderIds.add("121");
		orderIds.add("447");
		user.setOrderIds(orderIds);
		user.setSurname(SURNAME);
		return user ;
	}
}
