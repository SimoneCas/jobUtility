package it.sample.java.model;

public abstract class AdditionalInfoAttribute extends Attribute {

	private static final long serialVersionUID = 1L;

	private Integer ordinal;

	public Integer getOrdinal() {
		return ordinal;
	}

	public void setOrdinal(Integer ordinal) {
		this.ordinal = ordinal;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + ((ordinal == null) ? 0 : ordinal.hashCode());
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
		AdditionalInfoAttribute other = (AdditionalInfoAttribute) obj;
		if (ordinal == null) {
			if (other.ordinal != null)
				return false;
		} else if (!ordinal.equals(other.ordinal))
			return false;
		return true;
	}
	
	
}
