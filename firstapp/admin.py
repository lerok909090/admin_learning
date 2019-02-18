from django.contrib import admin
from .models import teacher, faculty, course


#admin.site.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'display_faculty')
admin.site.register(course, courseAdmin)
#admin.site.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
admin.site.register(teacher, teacherAdmin)
#admin.site.register(faculty)

admin.site.register(faculty)


# Register your models here.
