"""Models for char sheer app"""
from django.db import models

# Create your models here.


class SolarCharacter(models.Model):
    """Model for exalted character"""

    cast_choices = [
        ('1', 'Dawn'),
        ('2', 'Zenith'),
        ('3', 'Twilight'),
        ('4', 'Night'),
        ('5', 'Eclipse')
    ]
    # TODO: Add  in choices for all availble fields onfile / into db

    # Fields
    # TODO: Add help text for all fields
    # TODO: Add validators for fields

    # General
    name = models.CharField(max_length=40)
    cast = models.CharField(max_length=40, choices=cast_choices, default='1')
    concept = models.CharField(max_length=40)
    nature = models.CharField(max_length=40)
    anima = models.CharField(max_length=40)
    # Attributes - Physical
    strenght = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    # Attribues - Social
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    apperance = models.IntegerField(default=1)
    # Attributes - Mental
    intelligence = models.IntegerField(default=1)
    apperance = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    # Abilities - War
    archery = models.IntegerField(default=1)
    athletics = models.IntegerField(default=1)
    awareness = models.IntegerField(default=1)
    brawl = models.IntegerField(default=1)
    dodge = models.IntegerField(default=1)
    endurance = models.IntegerField(default=1)
    martial_arts = models.IntegerField(default=1)
    melee = models.IntegerField(default=1)
    resistance = models.IntegerField(default=1)
    thrown = models.IntegerField(default=1)
    # Abilities - life
    crafts = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    linguistics = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    presence = models.IntegerField(default=0)
    ride = models.IntegerField(default=0)
    sail = models.IntegerField(default=0)
    socialize = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    # Abilities - Wisdom
    bureaucracy = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)

    # hiearchy
    general_info = [name, cast, concept, nature, anima]
    physical = [strenght, dexterity, stamina]
    social = [charisma, manipulation, apperance]
    mental = [intelligence, apperance, wits]
    attributes = [physical, social, mental]
    war = [archery, athletics, awareness, brawl, dodge,
           endurance, martial_arts, melee, resistance, thrown]
    life = [crafts, larceny, linguistics, performance,
            presence, ride, sail, socialize, stealth, survival]
    wisdom = [bureaucracy, investigation, lore, medicine, occult]
    abilities = [war, life, wisdom]
