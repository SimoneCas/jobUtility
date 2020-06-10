package it.sample.jpa.model;

import java.io.Serializable;
import java.util.Objects;

public class MatchId implements Serializable {
	private static final long serialVersionUID = 1L;
	
	private String brandId = "0";
	private String channelId = "0";
	private String matchId;

	public MatchId() {
		
	}
	
	public MatchId(String brandId, String channelId, String matchId) {
		this.brandId = brandId;
		this.channelId = channelId;
		this.matchId = matchId;
	}
	
	public MatchId(MatchId other) {
		this.brandId = other.brandId;
		this.channelId = other.channelId;
		this.matchId = other.matchId;
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

	@Override
	public int hashCode() {
		return Objects.hash(brandId, channelId, matchId);
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
		MatchId other = (MatchId) obj;
		return Objects.equals(brandId, other.brandId) 
				&& Objects.equals(channelId, other.channelId)
				&& Objects.equals(matchId, other.matchId);
	}

	@Override
	public String toString() {
		return "MatchId [brandId=" + brandId + ", channelId=" + channelId + ", matchId=" + matchId + "]";
	}

}
