package it.sample.java.mapper;

import it.sample.java.model.CompetitorAdditionalInfoAttribute;
import it.sample.java.model.dto.AttributeTypeDTO;
import it.sample.java.model.dto.CompetitorAdditionalInfoAttributeDTO;

public class CompetitorAdditionalInfoAttributeMapper implements Mapper<CompetitorAdditionalInfoAttribute, CompetitorAdditionalInfoAttributeDTO> {
	private CompetitorTypeMapper competitorTypeMapper = new CompetitorTypeMapper();
	
	@Override
	public CompetitorAdditionalInfoAttributeDTO map(CompetitorAdditionalInfoAttribute source) {
		CompetitorAdditionalInfoAttributeDTO result = new CompetitorAdditionalInfoAttributeDTO();
		result.setAttributeTypeDTO(AttributeTypeDTO.COMPETITOR_ADDITIONAL_INFO);
		result.setCompetitorTypeDTO(competitorTypeMapper.map(source.getCompetitorType()));
		result.setOrdinal(source.getOrdinal());
		return result;
	}

}
