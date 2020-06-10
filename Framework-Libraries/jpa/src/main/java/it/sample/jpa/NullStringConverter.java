package it.sample.jpa;

import org.eclipse.persistence.internal.helper.DatabaseField;
import org.eclipse.persistence.mappings.DatabaseMapping;
import org.eclipse.persistence.mappings.converters.Converter;
import org.eclipse.persistence.sessions.Session;

public class NullStringConverter implements Converter {
	private static final long serialVersionUID = 1L;
	private static final String NULL_REPRESENTATION = "**NULL**";
	
	@Override
	public Object convertDataValueToObjectValue(Object dataValue, Session session) {
		if (NULL_REPRESENTATION.equals(dataValue)) {
			return null;
		} else {
			return dataValue;
		}
	}

	@Override
	public Object convertObjectValueToDataValue(Object objectValue, Session session) {
		if (objectValue == null) {
			return NULL_REPRESENTATION;
		} else {
			return objectValue;
		}
	}

	@Override
	public void initialize(DatabaseMapping mapping, Session session) {
		final DatabaseField field = mapping.getField();
		field.setSqlType(java.sql.Types.VARCHAR);
	}

	@Override
	public boolean isMutable() {
		return true;
	}

}