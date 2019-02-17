package it.sample.java.model;

public class LineAdditionalInfoAttribute extends AdditionalInfoAttribute{

	private static final long serialVersionUID = 1L;

	private LineType lineType;

	private LineSpecialization lineSpecialization;

	public LineAdditionalInfoAttribute(){
	}

	public LineType getLineType() {
		return lineType;
	}

	public void setLineType(LineType lineType) {
		this.lineType = lineType;
	}

	public LineSpecialization getLineSpecialization() {
		return lineSpecialization;
	}

	public void setLineSpecialization(LineSpecialization lineSpecialization) {
		this.lineSpecialization = lineSpecialization;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + ((lineSpecialization == null) ? 0 : lineSpecialization.hashCode());
		result = prime * result + ((lineType == null) ? 0 : lineType.hashCode());
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
		LineAdditionalInfoAttribute other = (LineAdditionalInfoAttribute) obj;
		if (lineSpecialization != other.lineSpecialization)
			return false;
		if (lineType != other.lineType)
			return false;
		return true;
	}
}
