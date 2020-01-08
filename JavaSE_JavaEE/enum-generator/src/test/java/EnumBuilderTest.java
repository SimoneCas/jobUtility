import org.junit.Assert;
import org.junit.Test;

import it.sample.java.EnumBuilder;
import it.sample.java.FirstEnum;
import it.sample.java.SecondEnum;

public class EnumBuilderTest {

	@Test
	public void testEnumBuilder() {
		String one = "ONE";
		FirstEnum enumProperty = EnumBuilder.getEnumProperty(one, FirstEnum.class);
		Assert.assertEquals(FirstEnum.ONE, enumProperty);
		
		String two = "TWO";
		SecondEnum enumProperty2 = EnumBuilder.getEnumProperty(two, SecondEnum.class);
		Assert.assertEquals(SecondEnum.TWO, enumProperty2);
	}
}
