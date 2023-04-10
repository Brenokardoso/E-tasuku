from django.db import models
from django.contrib import admin
import datetime


class tarefas(models.Model):
    tasks = models.CharField(max_length=100)
    tasks_time = models.DateTimeField("Data da tarefa")
    @admin.display(boolean = True,
                   ordering= "Data de publicação",
                   description= "Recentemente publicado?",
                   )
    
    def __str__(self):
        return(self.tasks)
    
    def foi_publicado(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        return(now - datetime.timedelta(days=1)<= self.tasks_time <= now)


class full_tasks(models.Model):
    complete_tasks = models.ForeignKey(tarefas,on_delete=models.CASCADE)
    all_complete = models.BooleanField(default=None)

    def __str__(self):
        return(self.complete_tasks)