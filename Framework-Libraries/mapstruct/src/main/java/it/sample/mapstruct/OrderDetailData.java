package it.sample.mapstruct;

import java.math.BigDecimal;

public class OrderDetailData {

		private String description;
		private Integer quantity;
		private BigDecimal singlePrice;

		public OrderDetailData() {
			
		}
		
		public OrderDetailData(String description, Integer quantity, BigDecimal singlePrice) {
			this.description = description;
			this.quantity = quantity;
			this.singlePrice = singlePrice;
		}

		public String getDescription() {
			return description;
		}

		public void setDescription(String description) {
			this.description = description;
		}

		public Integer getQuantity() {
			return quantity;
		}

		public void setQuantity(Integer quantity) {
			this.quantity = quantity;
		}

		public BigDecimal getSinglePrice() {
			return singlePrice;
		}

		public void setSinglePrice(BigDecimal singlePrice) {
			this.singlePrice = singlePrice;
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + ((description == null) ? 0 : description.hashCode());
			result = prime * result + ((quantity == null) ? 0 : quantity.hashCode());
			result = prime * result + ((singlePrice == null) ? 0 : singlePrice.hashCode());
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
			OrderDetailData other = (OrderDetailData) obj;
			if (description == null) {
				if (other.description != null)
					return false;
			} else if (!description.equals(other.description))
				return false;
			if (quantity == null) {
				if (other.quantity != null)
					return false;
			} else if (!quantity.equals(other.quantity))
				return false;
			if (singlePrice == null) {
				if (other.singlePrice != null)
					return false;
			} else if (!singlePrice.equals(other.singlePrice))
				return false;
			return true;
		}
		
}
