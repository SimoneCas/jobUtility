package it.sample.java.model.dto;

public class LineAdditionalInfoAttributeDTO extends AdditionalInfoAttributeDTO implements java.io.Serializable {

	private static final long serialVersionUID = 1L;

	private LineTypeDTO lineTypeDTO;
	private LineSpecializationDTO lineSpecializationDTO;


	public LineAdditionalInfoAttributeDTO() {}

	public LineAdditionalInfoAttributeDTO(LineTypeDTO lineTypeDTO, LineSpecializationDTO lineSpecializationDTO) {
		this.lineTypeDTO = lineTypeDTO;
		this.lineSpecializationDTO = lineSpecializationDTO;
	}

	public LineTypeDTO getLineTypeDTO() {
		return this.lineTypeDTO;
	}

	public void setLineTypeDTO(LineTypeDTO lineTypeDTO) {
		this.lineTypeDTO = lineTypeDTO;
	}

	public LineSpecializationDTO getLineSpecializationDTO() {
		return this.lineSpecializationDTO;
	}

	public void setLineSpecializationDTO(LineSpecializationDTO lineSpecializationDTO) {
		this.lineSpecializationDTO = lineSpecializationDTO;
	}

}