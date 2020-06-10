package it.sample.jpa.model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import static java.util.stream.Collectors.toList;

public class Market implements Serializable {
	private static final long serialVersionUID = 1L;
	
	private MarketId marketId;
	private String name; //nome del market
	private List<Way> ways; //lista di esiti
	private Date insertDate; //data inserimento in cache
    private ExternalSystemStatus externalSystemStatus;
	private long timestamp;
	private String transactionId;
	private MarketStatus status;
	private MarketStatus statusOld;
	private String providerId;
	
	public Market() {
	}
	
	public Market(Market other) {
		this.marketId = other.marketId;
		this.name = other.name;
		if (other.ways != null) {
			this.ways = other.ways.stream().map(Way::new).collect(toList());
		}
		this.insertDate = other.insertDate;
		this.externalSystemStatus = other.externalSystemStatus;
		this.timestamp = other.timestamp;
		this.transactionId = other.transactionId;
		this.status = other.status;
		this.statusOld = other.statusOld;
		this.providerId = other.providerId;
	}
	
	public MarketStatus getStatus() {
		return status;
	}
	
	public void setStatus(MarketStatus status) {
		this.statusOld= this.status;
		if (this.statusOld == null) {
			this.statusOld = status;
		}
		this.status = status;
	}
	
	public MarketStatus getStatusOld() {
		return statusOld;
	}
	
	public void setStatusOld(MarketStatus statusOld) {
		this.statusOld = statusOld;
	}
	
	public MarketId getMarketId() {
		return marketId;
	}
	
	public void setMarketId(MarketId marketId) {
		this.marketId = marketId;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public Integer getWayCount() {
		if (getWays() == null) {
			return 0;
		}
		return (int)getWays().stream()
				.filter(way -> !way.isVoid())
				.count();
	}
	
	public List<Way> getWays() {
		return ways;
	}
	
	public void setWays(List<Way> ways) {
		this.ways = ways;
	}
	
	public Way getWay(String wayId) {
		return getWays().stream().filter(w -> wayId.equals(w.getWayId())).findFirst().orElse(null);
	}
	
	public Date getInsertDate() {
		return insertDate;
	}
	
	public void setInsertDate(Date insertDate) {
		this.insertDate = insertDate;
	}
	
	public ExternalSystemStatus getExternalSystemStatus(){
		return this.externalSystemStatus;
	}
	
	public void setExternalSystemStatus(ExternalSystemStatus s){
		this.externalSystemStatus=s;
	}
	
	public long getTimestamp() {
		return timestamp;
	}
	
	public void setTimestamp(long timestamp) {
		this.timestamp = timestamp;
	}
	
	public String getTransactionId() {
		return transactionId;
	}
	
	public void setTransactionId(String transactionId) {
		this.transactionId = transactionId;
	}
	
	public String getProviderId() {
		return providerId;
	}

	public void setProviderId(String providerId) {
		this.providerId = providerId;
	}

	public static MarketId calcKey(String brandId, String channelId, String matchId, String marketId){
		return new MarketId(brandId, channelId, matchId, marketId);
	}
	
	public Market mergeWays(Market newMarket) {
		List<Way> mergedWays = new ArrayList<>(getWays());
		if (newMarket.getWays() != null) {
			for (Way newWay: newMarket.getWays()) {
				String wayId = newWay.getWayId();
				Optional<Way> oldWay = mergedWays.stream().filter(w -> wayId.equals(w.getWayId())).findFirst();
				if (oldWay.isPresent()) {
					mergeWay(oldWay.get(), newWay);
				} else {
					mergedWays.add(newWay);
				}
			}
		}
		this.setWays(mergedWays);
		return this;
	}
	
	private void mergeWay(Way oldWay, Way newWay) {
		oldWay.setOdds(newWay.getOdds());
		if (oldWay.getStatus() != WayStatus.VOID) {
			oldWay.setStatus(newWay.getStatus());
		}
		oldWay.setTimestamp(newWay.getTimestamp());
	}
	
	
	public void rollbackStatus() {
		this.status = this.statusOld;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((externalSystemStatus == null) ? 0 : externalSystemStatus.hashCode());
		result = prime * result + ((insertDate == null) ? 0 : insertDate.hashCode());
		result = prime * result + ((marketId == null) ? 0 : marketId.hashCode());
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		result = prime * result + ((status == null) ? 0 : status.hashCode());
		result = prime * result + ((statusOld == null) ? 0 : statusOld.hashCode());
		result = prime * result + (int) (timestamp ^ (timestamp >>> 32));
		result = prime * result + ((transactionId == null) ? 0 : transactionId.hashCode());
		result = prime * result + ((ways == null) ? 0 : ways.hashCode());
		result = prime * result + ((providerId == null) ? 0 : providerId.hashCode());
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
		Market other = (Market) obj;
		if (externalSystemStatus != other.externalSystemStatus)
			return false;
		if (insertDate == null) {
			if (other.insertDate != null)
				return false;
		} else if (!insertDate.equals(other.insertDate))
			return false;
		if (marketId == null) {
			if (other.marketId != null)
				return false;
		} else if (!marketId.equals(other.marketId))
			return false;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		if (status != other.status)
			return false;
		if (statusOld != other.statusOld)
			return false;
		if (timestamp != other.timestamp)
			return false;
		if (transactionId == null) {
			if (other.transactionId != null)
				return false;
		} else if (!transactionId.equals(other.transactionId))
			return false;
		if (ways == null) {
			if (other.ways != null)
				return false;
		} else if (!ways.containsAll(other.ways) || !other.ways.containsAll(ways))
			return false;
		if (providerId == null) {
			if (other.providerId != null)
				return false;
		} else if (!providerId.equals(other.providerId))
			return false;
		return true;
	}
	
	@Override
	public String toString() {
		return "Market [marketId=" + marketId + ", name=" + name + ", ways=" + ways + ", insertDate=" + insertDate
				+ ", externalSystemStatus=" + externalSystemStatus + ", timestamp=" + timestamp + ", transactionId="
				+ transactionId + ", providerId=" + providerId + ", status=" + status + ", statusOld=" + statusOld + "]";
	}
	
}
