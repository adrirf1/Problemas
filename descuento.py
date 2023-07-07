def desc(precio,descuento):
    return round(precio - (precio*(descuento/100)),2)

print(desc(100,20))