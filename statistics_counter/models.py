from django.db import models

class statictics_data(models.Model):
    """Статистика"""
    date = models.DateField("Дата события", auto_now_add=True)
    views = models.IntegerField("Количество показов", default=0)
    clicks = models.IntegerField("Количество кликов", default=0)
    cost = models.FloatField("Стоимость кликов", default=0)
    cpc = models.FloatField("Cредняя стоимость клика", default=0)
    cpm = models.FloatField("Cредняя стоимость 1000 показов", default=0)

    def save(self, *args, **kwargs):
        self.cost = round(self.cost, 2)
        self.cpc = round(self.cpc, 2)
        self.cpm = round(self.cpm, 2)
        super(statictics_data, self).save(*args, **kwargs)