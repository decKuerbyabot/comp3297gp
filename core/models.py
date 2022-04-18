from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_code=models.CharField(primary_key=True, max_length=20)
    location=models.CharField(max_length=150)
    type=models.CharField(max_length=2)
    capacity=models.IntegerField()
    def __str__(self):
        return self.venue_code

class HKUMember(models.Model):
    hku_id=models.CharField(primary_key=True, max_length=10)
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Record(models.Model):
    # need to make sure that leave is larger than enter
    enter_datetime=models.DateTimeField()
    leave_datetime=models.DateTimeField()
    venue=models.ForeignKey(Venue, on_delete=models.CASCADE)
    member=models.ForeignKey(HKUMember, on_delete=models.CASCADE)

    def __str__(self):
        return "By "+self.member.name+" from "+self.enter_datetime.strftime("%m/%d/%Y, %H:%M:%S")+" to "+self.leave_datetime.strftime("%m/%d/%Y, %H:%M:%S")