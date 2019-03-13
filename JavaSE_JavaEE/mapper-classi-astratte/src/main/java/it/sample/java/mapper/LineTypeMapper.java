package it.sample.java.mapper;

import it.sample.java.model.LineType;
import it.sample.java.model.dto.LineTypeDTO;

public class LineTypeMapper implements Mapper<LineType, LineTypeDTO> {

	@Override
	public LineTypeDTO map(LineType source) {
		if (source == null) {
			return null;
		}
		return LineTypeDTO.valueOf(source.name());
	}

}
