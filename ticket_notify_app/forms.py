from django.forms import ModelForm
from ticket_notify_app.models import Concert


class ConcertForm(ModelForm):
    """公演のフォーム"""
    class Meta:
        model = Concert
        fields = ('artist_name', 'artist_id', 'concert_date', 'max_price')
