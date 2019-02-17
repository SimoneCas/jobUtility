package it.sample.java.model;

public class CompetitorAdditionalInfoAttribute extends AdditionalInfoAttribute {

	private static final long serialVersionUID = 1L;

	private CompetitorType competitorType;

	public CompetitorType getCompetitorType() {
		return competitorType;
	}

	public void setCompetitorType(CompetitorType competitorType) {
		this.competitorType = competitorType;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + ((competitorType == null) ? 0 : competitorType.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		CompetitorAdditionalInfoAttribute other = (CompetitorAdditionalInfoAttribute) obj;
		if (competitorType != other.competitorType)
			return false;
		return true;
	}
	
}
