from django.db import models

class Application(models.Model):
    name = models.CharField("Имя", max_length=100)
    contact = models.CharField("Контакт", max_length=150)
    goal = models.TextField("Цель/Уровень", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.contact}"
