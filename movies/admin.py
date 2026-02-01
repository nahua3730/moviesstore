from django.contrib import admin

# Register your models here.
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
class ReviewAdmin(admin.ModelAdmin):
    list_display=('id', 'movie', 'user', 'comment', 'is_reported', 'date')
    list_filter=['is_reported']
    actions=['restore_reviews']
    def restore_reviews(self, request, queryset):
        queryset.update(is_reported=False)
        self.message_user(request, "Selected reviews have been restored.")
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin) 