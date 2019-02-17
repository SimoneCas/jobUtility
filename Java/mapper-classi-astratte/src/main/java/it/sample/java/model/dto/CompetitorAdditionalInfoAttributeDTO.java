package it.sample.java.model.dto;

public class CompetitorAdditionalInfoAttributeDTO extends AdditionalInfoAttributeDTO implements java.io.Serializable {

	private static final long serialVersionUID = 1L;

	private CompetitorTypeDTO competitorTypeDTO;


	public CompetitorAdditionalInfoAttributeDTO() {}

	public CompetitorAdditionalInfoAttributeDTO(CompetitorTypeDTO competitorTypeDTO) {
		this.competitorTypeDTO = competitorTypeDTO;
	}

	public CompetitorTypeDTO getCompetitorTypeDTO() {
		return this.competitorTypeDTO;
	}

	public void setCompetitorTypeDTO(CompetitorTypeDTO competitorTypeDTO) {
		this.competitorTypeDTO = competitorTypeDTO;
	}

}