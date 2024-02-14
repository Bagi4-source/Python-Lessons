from django.db import models


class Star(models.Model):
    name = models.CharField(verbose_name="Название", max_length=30, null=False, blank=False)
    mass = models.FloatField(verbose_name="Масса")

    def __str__(self):
        return f"Звезда #{self.pk} {self.name}"

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"


class Planet(models.Model):
    name = models.CharField(verbose_name="Название", max_length=30, null=False, blank=False)
    radius = models.FloatField(verbose_name="Радиус")
    star_id = models.ForeignKey(Star, verbose_name="ID звезды", on_delete=models.CASCADE)

    def __str__(self):
        return f"Планета #{self.pk} {self.name}"

    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"


class Moon(models.Model):
    name = models.CharField(verbose_name="Название", max_length=30, null=False, blank=False)
    planet_id = models.ForeignKey(Planet, verbose_name="ID планеты", on_delete=models.CASCADE)

    def __str__(self):
        return f"Спутник #{self.pk} {self.name}"

    class Meta:
        verbose_name = "Спутник"
        verbose_name_plural = "Спутники"
