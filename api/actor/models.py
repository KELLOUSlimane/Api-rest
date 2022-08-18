# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Entreprise(models.Model):
    nomentreprise = models.CharField(db_column='NomEntreprise', max_length=45)  # Field name made lowercase.
    adressent = models.CharField(db_column='AdressEnt', max_length=45)  # Field name made lowercase.
    
    def coco(self):
        return {
            self.nomentreprise,
            self.identreprise,
            self.adressent
        }    
    #class Meta:
     #   managed = True
      #  db_table = 'entreprise'

class Employes(models.Model):
    nomemp = models.CharField(db_column='NomEmp', max_length=45)  # Field name made lowercase.
    preemp = models.CharField(db_column='PreEmp', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=45)  # Field name made lowercase.
    tel = models.IntegerField(db_column='Tel', blank=True, null=True)  # Field name made lowercase.
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    
    
    class Meta:
        managed = True
        db_table = 'employes'
