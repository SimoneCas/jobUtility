package it.sample.java.mapper;

import it.sample.java.model.LineSpecialization;
import it.sample.java.model.dto.LineSpecializationDTO;

public class LineSpecializationMapper implements Mapper<LineSpecialization, LineSpecializationDTO> {

	@Override
	public LineSpecializationDTO map(LineSpecialization source) {
		if (source == null) {
			return null;
		}
		return LineSpecializationDTO.valueOf(source.name());
	}

}
