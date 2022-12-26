from django.db import models

# ItemOderStatus
ORDER_STATUS = [
    ('PD' , 'pendenting'),
    ('DN', 'done')
]




class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_promo = models.BooleanField(default=False)
    promotional_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_promotional_price(self):
        if self.is_promo == True:
            return self.promotional_price
        else:
            return self.price



class ItemOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=2, choices=ORDER_STATUS, )

    def __str__(self):
        return f'{self.item.name} -> {self.total_price}'

    def get_total_price(self):
        if not self.total_price:
            total = self.item.get_promotional_price() * self.quantity
            self.total_price = total
    
    def save(self):
        self.get_total_price()
        return super().save()