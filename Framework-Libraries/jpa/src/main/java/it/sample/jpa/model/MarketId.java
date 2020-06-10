package it.sample.jpa.model;

import java.io.Serializable;
import java.util.Objects;

public class MarketId implements Serializable{

	private static final long serialVersionUID = 1L;
	private String brandId = "0";
	private String channelId = "0";
	private String matchId; //id match
	private String marketId; //id market

	public MarketId() {
	}

//	public MarketId(String matchId, String marketId) {
//		this.matchId = matchId;
//		this.marketId = marketId;
//	}
	
	public MarketId(String brandId, String channelId, String matchId, String marketId) {
		this.brandId = brandId;
		this.channelId = channelId;
		this.matchId = matchId;
		this.marketId = marketId;
	}
	
	public String getBrandId() {
		return brandId;
	}

	public void setBrandId(String brandId) {
		this.brandId = brandId;
	}

	public String getChannelId() {
		return channelId;
	}

	public void setChannelId(String channelId) {
		this.channelId = channelId;
	}

	public String getMatchId() {
		return matchId;
	}
	
	public void setMatchId(String matchId) {
		this.matchId = matchId;
	}

	public String getMarketId() {
		return marketId;
	}
	
	public void setMarketId(String marketId) {
		this.marketId = marketId;
	}
	
	public MatchId getCompleteMatchId() {
		return new MatchId(brandId, channelId, matchId);
	}

	@Override
	public int hashCode() {
		return Objects.hash(brandId, channelId, marketId, matchId);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null) {
			return false;
		}
		if (getClass() != obj.getClass()) {
			return false;
		}
		MarketId other = (MarketId) obj;
		return Objects.equals(brandId, other.brandId) 
				&& Objects.equals(channelId, other.channelId)
				&& Objects.equals(marketId, other.marketId) 
				&& Objects.equals(matchId, other.matchId);
	}

	@Override
	public String toString() {
		return "MarketId [brandId=" + brandId + ", channelId=" + channelId + ", matchId=" + matchId + ", marketId="
				+ marketId + "]";
	}
	
}
