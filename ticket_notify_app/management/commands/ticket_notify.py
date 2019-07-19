from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import sys
from time import sleep
from ticket_notify_app.models import Concert
from django.core.management.base import BaseCommand
from ticket_notify_app.models import Concert
from datetime import datetime as dt
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        concerts = Concert.objects.all()
        driver = webdriver.Chrome(executable_path=settings.BASE_DIR + "/chromedriver")
        for concert in concerts:
            tstr = concert.concert_date.strftime('%Y%m%d')
            target_url = "https://www.ticket.co.jp/sys/d/" + str(concert.artist_id) + ".htm?st=" + tstr + "&orderable=1&order=price"
            driver.get(target_url)
            print(driver.current_url)
            if target_url != driver.current_url:
                continue

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            cheapest_ticket_price = int(soup.find(class_='ticket-price').get_text().replace('￥', '').replace(',', ''))
            print(cheapest_ticket_price)
            # 最安金額が設定金額以下だった場合、ラインに通知
            if cheapest_ticket_price <= concert.max_price:
                url = "https://notify-api.line.me/api/notify"
                token = '3bmXn7c7x6VZ2iF83RANGMiOyfOjgjOfMAEHMW6ytBa'
                headers = {"Authorization": "Bearer " + token}
                payload = {"message": driver.current_url}

                try:
                    requests.post(url, headers=headers, params=payload)
                except Exception as e:
                    print(e)

        driver.close()
        driver.quit()
