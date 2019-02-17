package it.sample.java.mapper;

import it.sample.java.model.LineAdditionalInfoAttribute;
import it.sample.java.model.dto.AttributeTypeDTO;
import it.sample.java.model.dto.LineAdditionalInfoAttributeDTO;

public class LineAdditionalInfoAttributeMapper implements Mapper<LineAdditionalInfoAttribute, LineAdditionalInfoAttributeDTO> {
	private LineTypeMapper lineTypeMapper = new LineTypeMapper();
	private LineSpecializationMapper lineSpecializationMapper = new LineSpecializationMapper();
	
	@Override
	public LineAdditionalInfoAttributeDTO map(LineAdditionalInfoAttribute source) {
		LineAdditionalInfoAttributeDTO result = new LineAdditionalInfoAttributeDTO();
		result.setAttributeTypeDTO(AttributeTypeDTO.LINE_ADDITIONAL_INFO);
		result.setOrdinal(source.getOrdinal());
		result.setLineTypeDTO(lineTypeMapper.map(source.getLineType()));
		result.setLineSpecializationDTO(lineSpecializationMapper.map(source.getLineSpecialization()));
		return result;
	}

}
