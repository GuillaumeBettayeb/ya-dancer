from django.db import models

class HealthTable(models.Model):
	health_field = models.CharField(max_length=20)
