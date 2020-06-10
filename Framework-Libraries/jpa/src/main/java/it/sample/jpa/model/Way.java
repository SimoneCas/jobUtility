package it.sample.jpa.model;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Date;

public class Way implements Serializable {
	private static final long serialVersionUID = 1L;
	
	public enum WIN {
		WIN, LOSE, CANCEL;
	}
	
	private String wayId; //id esito
	private String win; //vincente/perdente (true/false)
	private BigDecimal odds; //quota
	private Date insertDate; //data inserimento in cache
	private long timestamp;
	private WayStatus status;
	private WayStatus statusOld;
	
	public Way() {
	}
	
	public Way(Way other) {
		this.wayId = other.wayId;
		this.win = other.win;
		this.odds = other.odds;
		this.insertDate = other.insertDate;
		this.timestamp = other.timestamp;
		this.status = other.status;
		this.statusOld = other.statusOld;
	}
	
	public String getWayId() {
		return wayId;
	}
	public void setWayId(String wayId) {
		this.wayId = wayId;
	}
	public WayStatus getStatus() {
		return status;
	}
	public void setStatus(WayStatus status) {
		this.statusOld= this.status;
		if (this.statusOld == null) {
			this.statusOld = status;
		}
		this.status = status;
	}
	public String getWin() {
		return win;
	}
	public void setWin(String win) {
		this.win = win;
	}
	public Date getInsertDate() {
		return insertDate;
	}
	public void setInsertDate(Date insertDate) {
		this.insertDate = insertDate;
	}
	public BigDecimal getOdds() {
		return odds;
	}
	public void setOdds(BigDecimal odds) {
		this.odds = odds;
	}
	public long getTimestamp() {
		return timestamp;
	}
	public void setTimestamp(long timestamp) {
		this.timestamp = timestamp;
	}
	public WayStatus getStatusOld() {
		return statusOld;
	}
	public void setStatusOld(WayStatus statusOld) {
		this.statusOld = statusOld;
	}
	
	public boolean isVoid() {
		return this.status == WayStatus.VOID;
	}
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((insertDate == null) ? 0 : insertDate.hashCode());
		result = prime * result + ((odds == null) ? 0 : odds.hashCode());
		result = prime * result + ((status == null) ? 0 : status.hashCode());
		result = prime * result + ((statusOld == null) ? 0 : statusOld.hashCode());
		result = prime * result + (int) (timestamp ^ (timestamp >>> 32));
		result = prime * result + ((wayId == null) ? 0 : wayId.hashCode());
		result = prime * result + ((win == null) ? 0 : win.hashCode());
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
		Way other = (Way) obj;
		if (insertDate == null) {
			if (other.insertDate != null)
				return false;
		} else if (!insertDate.equals(other.insertDate))
			return false;
		if (odds == null) {
			if (other.odds != null)
				return false;
		} else if (!odds.equals(other.odds))
			return false;
		if (status != other.status)
			return false;
		if (statusOld != other.statusOld)
			return false;
		if (timestamp != other.timestamp)
			return false;
		if (wayId == null) {
			if (other.wayId != null)
				return false;
		} else if (!wayId.equals(other.wayId))
			return false;
		if (win == null) {
			if (other.win != null)
				return false;
		} else if (!win.equals(other.win))
			return false;
		return true;
	}
	@Override
	public String toString() {
		return "Way [wayId=" + wayId + ", win=" + win + ", odds=" + odds + ", insertDate=" + insertDate + ", timestamp="
				+ timestamp + ", status=" + status + ", statusOld=" + statusOld + "]";
	}
}