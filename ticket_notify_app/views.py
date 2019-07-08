from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from ticket_notify_app.models import Concert
from ticket_notify_app.forms import ConcertForm
from django.contrib import messages
import logging


def concert_list(request):
    """公演の一覧"""
    concerts = Concert.objects.all().order_by('id')
    return render(request,
                  'ticket_notify_app/concert_list.html',  # 使用するテンプレート
                  {'concerts': concerts})  # テンプレートに渡すデータ


def concert_edit(request, concert_id=None):
    """公演の編集"""
    if concert_id:  # concert_id が指定されている (修正時)
        concert = get_object_or_404(Concert, pk=concert_id)
    else:  # concert_id が指定されていない (追加時)
        concert = Concert()

    if request.method == 'POST':
        form = ConcertForm(request.POST, instance=concert)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            concert = form.save(commit=False)
            concert.save()
            if concert_id:
                messages.success(request, "ID:" + str(concert_id) + 'の公演を更新しました')
            else:
                messages.success(request, '公演を追加しました')
            return redirect('ticket_notify_app:concert_list')
    else:  # GET の時
        form = ConcertForm(instance=concert)  # concert インスタンスからフォームを作成

    return render(request, 'ticket_notify_app/concert_edit.html', dict(form=form, concert_id=concert_id))


def concert_delete(request, concert_id):
    """公演の削除"""
    concert = get_object_or_404(Concert, pk=concert_id)
    concert.delete()
    messages.success(request, "ID:" + str(concert_id) + 'の公演を削除しました')

    return redirect('ticket_notify_app:concert_list')
