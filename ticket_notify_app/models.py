from django.db import models
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator


class Concert(models.Model):
    class Meta:
        db_table = 'concert'  # 使用テーブル

    artist_name = models.CharField(verbose_name='アーティスト名', max_length=100)
    artist_id = models.IntegerField(verbose_name='アーティストid', default=0, validators=[MinValueValidator(0)])
    concert_date = models.DateField(verbose_name='公演日')
    max_price = models.IntegerField(verbose_name='価格', default=0, validators=[MinValueValidator(0)])
    # auto_now_add はインスタンスの作成(DBにINSERT)する度に更新
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    # # auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.artist_name
