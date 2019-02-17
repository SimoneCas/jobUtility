package it.sample.java.mapper;

import static org.apache.commons.lang3.StringUtils.substringAfterLast;

import it.sample.java.model.Attribute;
import it.sample.java.model.dto.AttributeDTO;

public class AttributeMapper implements Mapper<Attribute, AttributeDTO> {

	@Override
	public AttributeDTO map(Attribute source) {
		String sourceClassName = source.getClass().getName();
		String mapperClassName = this.getClass().getPackage().getName() + "." + substringAfterLast(sourceClassName,".") + "Mapper";
		Mapper mapper;
		try {
			mapper = (Mapper)Class.forName(mapperClassName).newInstance();
		} catch (InstantiationException | IllegalAccessException | ClassNotFoundException e) {
			throw new RuntimeException(e);
		}
		return (AttributeDTO)mapper.map(source);
	}

}
