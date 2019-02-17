package it.sample.java;

import it.sample.java.mapper.AttributeMapper;
import it.sample.java.mapper.Mapper;
import it.sample.java.model.AttributeType;
import it.sample.java.model.CompetitorAdditionalInfoAttribute;
import it.sample.java.model.CompetitorType;
import it.sample.java.model.dto.CompetitorAdditionalInfoAttributeDTO;

public class Main {

	public static void main(String[] args){
		CompetitorAdditionalInfoAttribute competitorAttribute = new CompetitorAdditionalInfoAttribute();
		competitorAttribute.setAttributeType(AttributeType.COMPETITOR_ADDITIONAL_INFO);
		competitorAttribute.setCompetitorType(CompetitorType.PLAYER);
		competitorAttribute.setOrdinal(1);
		
		Mapper mapper = new AttributeMapper();
		Object attributeDTO = mapper.map(competitorAttribute);
		CompetitorAdditionalInfoAttributeDTO competitorAttributeDTO = (CompetitorAdditionalInfoAttributeDTO) attributeDTO;
		System.out.println("Competitor dto " + competitorAttributeDTO.toString());
	}
}
