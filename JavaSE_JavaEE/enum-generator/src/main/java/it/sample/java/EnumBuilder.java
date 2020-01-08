package it.sample.java;

public class EnumBuilder {

	public static <E extends Enum<E>> E getEnumProperty(final String value, final Class<E> myClass) {

		// Map the property to the ENUM
		return Enum.valueOf(myClass, value.toUpperCase());
	}
}
