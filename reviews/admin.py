from django.contrib import admin
from reviews.models import Book, Publisher, Review, Contributor, BookContributor

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    search_fields = ('title', 'isbn', 'publisher__name')
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date',)
    # def isbn13(self, obj):
    #     return f"{obj.isbn[0:3]}-{obj.isbn[3:4]}-{obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}"

# def initialled_name(obj):
#     initials = ''.join([name[0] for name in obj.first_names.split(" ")])
#     return f"{obj.last_names}, {initials}"

class ContributorAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names")
    search_fields = ("last_names__startswith", "first_names")
    list_filter = ("last_names", )

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited', 'date_created')

    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content', {'fields': ('content', 'rating')}))

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(BookContributor)

admin.site.site_header = "Bookr Adminstration"
admin.site.site_title = "Bookr Site Admin"
admin.site.title_header = "Bookr Admin"

# class BookrAdminSite(AdminSite):
#     title_header = 'Bookr Admin'
#     site_header = 'Bookr administration'
#     index_title = 'Bookr site admin'

# admin_site = BookrAdminSite(name='bookr')

# # Register your models here
# admin_site.register(Publisher)
# admin_site.register(Contributor)
# admin_site.register(Book)
# admin_site.register(BookContributor)
# admin_site.register(Review)

