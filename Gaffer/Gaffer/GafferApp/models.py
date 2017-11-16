# need to install pillow with pip install pillow for Imagefield
from django.db import models

# Create your models here.
class Coach(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    coachEmail = models.EmailField(max_length=50,unique=True)
    coachUsername = models.CharField(max_length=50,unique=True)



    def __str__(self):
        return self.first_name + " " + self.last_name

class CoachProfile(models.Model):
    profileOwner = models.ForeignKey(Coach,on_delete=models.CASCADE)
    biosketch = models.TextField()
    profilePic = models.ImageField()

    def __str__(self):
        return self.first_name + " " + self.last_name



class Drill(models.Model):
    drillTitle = models.CharField(max_length = 20)
    drillOwner = models.ForeignKey(Coach,on_delete=models.CASCADE)
    drillImage = models.ImageField()
    drillDescription = models.TextField()
    drillType = models.CharField(max_length = 20)
    drillRate = models.IntegerField()
    drillSetup = models.TextField()
    drillInstruction = models.TextField()
    drillDate = models.DateField()


    def __str__(self):
        return self.drillId + " " + self.drillOwner

class CoachingPlan(models.Model):
    coachingPlanOwner = models.ForeignKey(Coach,on_delete=models.CASCADE)
    coachingPlanTitle = models.CharField(max_length = 20)
    coachingPlanType = models.CharField(max_length = 20)
    coachingPlanDescription = models.TextField()
    coachingPlanDrill = models.ManyToManyField(Drill)

class Player(models.Model):
    playerJerseyLabel = models.CharField(max_length = 3)
    playerGoalCount = models.IntegerField()
    playerYellowCard= models.IntegerField()
    PlayerRedCard = models.BooleanField()
    playersCoach= models.ForeignKey(Coach)

class Lineup(models.Model):
    LineupStyle = models.CharField(max_length = 12)
    LineupPlayers = models.ManyToManyField(Player)
    LineupOwner = models.ForeignKey(Coach)
		
