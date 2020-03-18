package it.sample.mapstruct;

import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.Mappings;
import org.mapstruct.factory.Mappers;

@Mapper
public interface OrderMapper {

	OrderMapper INSTANCE = Mappers.getMapper(OrderMapper.class);
	
	
	@Mappings({
		@Mapping(target="clientId", source="orderData.customerId")
	})
	public Order toOrder(OrderData orderData);
}
