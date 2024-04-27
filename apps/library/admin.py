from django.contrib import admin
from apps.library.models import Book, BookCover, Author


class BookCoverInline(admin.TabularInline):
    model = BookCover
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'created_at', 'book_cover')
    readonly_fields = ('book_cover',)
    inlines = [BookCoverInline]

    def book_cover(self, obj):
        return obj.book_cover

    book_cover.short_description = 'book_cover'
    book_cover.allow_tags = True


admin.site.register(Book, BookAdmin)
# admin.site.register(BookCover)
admin.site.register(Author)
