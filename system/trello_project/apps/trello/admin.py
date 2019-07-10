from django.contrib import admin

from .models import MyUser, Board, Column, Card, Tag, Task

class MyUserAdmin(admin.ModelAdmin):
    pass

class BoardAdmin(admin.ModelAdmin):
    pass


class ColumnAdmin(admin.ModelAdmin):
    pass


class CardAdmin(admin.ModelAdmin):
    pass



class TagAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)

