package it.sample.lombok.model;

import java.math.BigInteger;
import java.util.List;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@EqualsAndHashCode
@NoArgsConstructor
@AllArgsConstructor
public class User {

	@NonNull private String id;
	private String name;
	private String surname;
	private Integer age;
	@NonNull private BigInteger bankAmount;
	private List<String> orderIds;
	
}
