package it.sample.jpa.model;

import java.math.BigDecimal;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;

import org.junit.ClassRule;
import org.junit.Test;

public class MarketJpaTest {
	@ClassRule
	public static final JpaTestRule jpa = new JpaTestRule();
	
	@Test
	public void testMarket() throws Exception {
		SimpleDateFormat isoFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS");
		Date marketInsertDate = isoFormat.parse("2009-02-14T00:31:30.123");
		Date wayInsertDate = isoFormat.parse("2009-02-14T00:31:30.123");
		
		Market market = new Market();
		market.setMarketId(new MarketId("175",null,"1","11"));
		market.setExternalSystemStatus(ExternalSystemStatus.SENT);
		market.setName("1-X-2");
		market.setProviderId("2");
		market.setStatus(MarketStatus.OPEN);
		market.setTimestamp(1234567890L);
		market.setTransactionId("abcdef");
		market.setInsertDate(marketInsertDate);
		
		Way way = new Way();
		way.setWayId("3");
		way.setInsertDate(wayInsertDate);
		way.setOdds(BigDecimal.valueOf(12.3));
		way.setStatus(WayStatus.OPEN);
		way.setTimestamp(1234567890L);
		way.setWin("WIN");
		market.setWays(Arrays.asList(way));
		
		jpa.commitObj(market);
		
		jpa.assertTableContent("MARKETS", "it/sample/jpa/model/expected_market_dataset.xml");
		jpa.assertTableContent("MARKETS_WAYS", "it/sample/jpa/model/expected_market_ways_dataset.xml");
	}
	
}
