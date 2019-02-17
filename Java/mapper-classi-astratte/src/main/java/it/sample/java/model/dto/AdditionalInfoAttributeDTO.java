package it.sample.java.model.dto;

public abstract class AdditionalInfoAttributeDTO extends AttributeDTO implements java.io.Serializable {

	private static final long serialVersionUID = 1L;

	private Integer ordinal;


	public AdditionalInfoAttributeDTO() {}

	public AdditionalInfoAttributeDTO(Integer ordinal) {
		this.ordinal = ordinal;
	}

	public Integer getOrdinal() {
		return this.ordinal;
	}

	public void setOrdinal(Integer ordinal) {
		this.ordinal = ordinal;
	}

}