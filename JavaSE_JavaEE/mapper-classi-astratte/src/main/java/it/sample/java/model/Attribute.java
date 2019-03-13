package it.sample.java.model;


import java.io.Serializable;

public abstract class Attribute implements Serializable{

	private static final long serialVersionUID = 8925172397484968777L;

	private AttributeType attributeType;

	public AttributeType getAttributeType() {
		return attributeType;
	}

	public void setAttributeType(AttributeType attributeType) {
		this.attributeType = attributeType;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((attributeType == null) ? 0 : attributeType.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Attribute other = (Attribute) obj;
		if (attributeType != other.attributeType)
			return false;
		return true;
	}
}




