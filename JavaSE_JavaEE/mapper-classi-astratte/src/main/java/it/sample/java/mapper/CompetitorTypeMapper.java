package it.sample.java.mapper;

import it.sample.java.model.CompetitorType;
import it.sample.java.model.dto.CompetitorTypeDTO;

public class CompetitorTypeMapper implements Mapper<CompetitorType, CompetitorTypeDTO> {

	@Override
	public CompetitorTypeDTO map(CompetitorType source) {
		if (source == null) {
			return null;
		}
		return CompetitorTypeDTO.valueOf(source.name());
	}

}
