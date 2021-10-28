from django.db import models

# Create your models here.

class CadastroEmpresa(models.Model):

    name = models.CharField(max_length=50, default='Sem_Nome_Cadastrado')
    doc = models.CharField(max_length=14, unique=True, blank=False)
    about = models.CharField(max_length=250)
    active = models.BooleanField()
    site = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CadastroCliente(models.Model):
    name = models.CharField(max_length=50, default='Sem_Nome_Cadastrado')
    doc = models.CharField(max_length=14, unique=True, blank=False)
    about = models.CharField(max_length=250)
    active = models.BooleanField()
    site = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CadastroOferta(models.model):
    id_customer = models.ForeignKey(CadastroCliente, on_delete=models.SET_DEFAULT,default=1) # mudar para ID
    from_ = models.CharField(max_length=20, blank=False)
    to_ = models.CharField(max_length=20, blank=False)
    initial_value = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    amount_type = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.id_customer

class Lance(models.Model):
    id_provider = models.ForeignKey(CadastroCliente, on_delete=models.SET_DEFAULT,default=1) #mudar para ID
    id_offer = models.ForeignKey(CadastroEmpresa, on_delete=models.SET_DEFAULT,default=1) #mudar para ID
    value = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)