from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    cnpj = models.CharField(max_length=150, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    email = models.CharField(max_length=300, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    estado = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return f"{self.cnpj} {self.nome}"


class OurLogo(models.Model):
    title = models.CharField(max_length=40, default='Logo Title', null=False, blank=True)
    logo_img = models.ImageField(null=False, blank=False, upload_to='midea/images/')
    logo_alt = models.CharField(max_length=100, null=True, blank=True, default='')

    def __str__(self):
        return self.title



