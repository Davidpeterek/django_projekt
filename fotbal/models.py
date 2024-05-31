
from django.db import models

class Tym(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název týmu', help_text='Napiš název týmu')
    mesto = models.CharField(max_length=100, verbose_name='Město týmu', help_text='Napiš město, kde tým leží')

    def __str__(self):
        return self.nazev

class Hrac(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name='Jméno hráče', help_text='Zadej jméno hráče')
    prijmeni = models.CharField(max_length=100, verbose_name='Příjmení hráče', help_text='Zadej příjmení hráče')
    tym = models.ForeignKey(Tym, on_delete=models.CASCADE, verbose_name='Tym hráče', help_text='Vyber tým za který hráč hraje')
    pozice = models.CharField(max_length=50, verbose_name='Pozice hráče', help_text='Vyber pozici hráče')
    cislo_dresu = models.PositiveIntegerField(verbose_name='Číslo dresu hráče', help_text='Vyber číslo dresu se kterým hráč hraje')

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'

class Zapas(models.Model):
    domaci_tym = models.ForeignKey(Tym, related_name='domaci_tymy', on_delete=models.CASCADE, verbose_name='domaci tým', help_text='Vyber domácí tým')
    hostujici_tym = models.ForeignKey(Tym, related_name='hostujici_tymy', on_delete=models.CASCADE, verbose_name='hostující tým', help_text='Vyber tým hostů')
    datum = models.DateTimeField(verbose_name='Datum zápasu')
    domaci_skore = models.PositiveIntegerField(verbose_name='Skóre domácího týmu', help_text='Vyber skóre domácího týmu')
    hostujici_skore = models.PositiveIntegerField(verbose_name='Skóre hostujícího týmu', help_text='Vyber skóre hostujícího týmu')

    def __str__(self):
        return f'{self.domaci_tym} vs {self.hostujici_tym} - {self.datum}'
