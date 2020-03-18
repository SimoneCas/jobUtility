package it.sample.mapstruct;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

import org.junit.Assert;
import org.junit.Test;


public class OrderMapperTest {

	@Test
	public void testOrderMapper() {
		OrderData orderData = createOrderData();
		Order obtainedOrder = OrderMapper.INSTANCE.toOrder(orderData);
		
		Assert.assertEquals(getExpectedOrder(), obtainedOrder);
	}

	private Order getExpectedOrder() {
		List<OrderDetail> orderDetails = new ArrayList<OrderDetail>();
		orderDetails.add(new OrderDetail("description", 3, new BigDecimal("50")));
		
		Order order = new Order();
		order.setClientId(45455);
		order.setOrderDetails(orderDetails);
		order.setOrderId(2556);
		order.setPrice(new BigDecimal("150"));
		
		return order;
	}

	private OrderData createOrderData() {
		List<OrderDetailData> orderDetails = new ArrayList<>();
		orderDetails.add(new OrderDetailData("description", 3, new BigDecimal("50")));
		
		OrderData orderData = new OrderData();
		orderData.setCustomerId(45455);
		orderData.setOrderDetails(orderDetails);
		orderData.setOrderId(2556);
		orderData.setPrice(new BigDecimal("150"));
		
		return orderData;
	}
}
