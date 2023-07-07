def profit(info):
	costo = info["cost_price"] 
	venta = info["sell_price"]
	inventario = info["inventory"]
	return(round((venta-costo)*inventario))
	
print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))