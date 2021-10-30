from django.db import models

# Create your models here.

class CadastroEmpresa(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='Sem_Nome_Cadastrado')
    doc = models.CharField(max_length=18, unique=True, blank=False)
    about = models.CharField(max_length=250)
    active = models.BooleanField()
    site = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return str(self.id)

class CadastroCliente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='Sem_Nome_Cadastrado')
    doc = models.CharField(max_length=18, unique=True, blank=False)
    about = models.CharField(max_length=250)
    active = models.BooleanField()
    site = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return str(self.id)


class CadastroOferta(models.Model):
    id_customer = models.ForeignKey(CadastroCliente, on_delete=models.SET_DEFAULT,default=1)
    from_de = models.CharField(max_length=20, blank=False)
    to_para = models.CharField(max_length=20, blank=False)
    initial_value = models.FloatField(max_length=20)
    amount = models.FloatField(max_length=20)
    amount_type = models.CharField(max_length=10, blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.from_de

class Lance(models.Model):
    id_provider = models.ForeignKey(CadastroCliente, on_delete=models.SET_DEFAULT,default=1)
    id_offer = models.ForeignKey(CadastroEmpresa, on_delete=models.SET_DEFAULT,default=1)
    value = models.FloatField(max_length=20)
    amount = models.FloatField(max_length=20)

    objects = models.Manager()

