package it.sample.java.model.dto;

public abstract class AttributeDTO implements java.io.Serializable {

	private static final long serialVersionUID = 1L;

	private AttributeTypeDTO attributeTypeDTO;


	public AttributeDTO() {}

	public AttributeDTO(AttributeTypeDTO attributeTypeDTO) {
		this.attributeTypeDTO = attributeTypeDTO;
	}

	public AttributeTypeDTO getAttributeTypeDTO() {
		return this.attributeTypeDTO;
	}

	public void setAttributeTypeDTO(AttributeTypeDTO attributeTypeDTO) {
		this.attributeTypeDTO = attributeTypeDTO;
	}

}