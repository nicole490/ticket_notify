from django.contrib import admin
from ticket_notify_app.models import Concert


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'artist_id', 'concert_date', 'max_price', 'created_at', 'updated_at')  # 一覧に出したい項目
    list_display_links = ('artist_name',)  # 修正リンクでクリックできる項目


admin.site.register(Concert, ConcertAdmin)
