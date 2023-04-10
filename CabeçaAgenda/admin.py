from django.contrib import admin

from .models import tarefas,full_tasks

class organização_do_board(admin.TabularInline):
    modelo = full_tasks
    extra = 2


class inclusão_do_nome(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["tasks"]}),("Data de informação",{"fields":["tasks_time"],"classes" : ["collapse"]})
    ]
    na_linha = [organização_do_board]
    list_display = ["tasks","tasks_time","foi_publicado"]
    list_filter = ["tasks_time"]
    search_fields = ["tasks"]


admin.site.register(tarefas,inclusão_do_nome)
