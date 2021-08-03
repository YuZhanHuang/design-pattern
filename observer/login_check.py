import time
from abc import ABCMeta, abstractmethod
from observer_model import Observer, Observable


class Account(Observable):
    def __init__(self):
        super().__init__()
        self._latest_ip = {}
        self._latest_region = {}

    def login(self, name, ip, times):
        region = self._get_region(ip)
        if self._is_long_distance(name, region):
            self.notify_observers({'name': name, 'ip': ip, 'region': region, 'time': times})
        self._latest_region[name] = region
        self._latest_ip[name] = ip

    def _get_region(self, ip):
        ip_regions = {
            '118.167.65.213': '三重',
            '67.218.147.69': '美國洛杉磯'
        }
        return ip_regions.get(ip, '')

    def _is_long_distance(self, name, region):
        latest_region = self._latest_region.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):
    def update(self, observable, obj):
        current_time = time.gmtime(obj["time"])
        msg = f'[郵件發送] {obj["name"]} 檢測到帳戶登入異常 ' \
              f'登入地區: {obj["region"]}' \
              f'登入時間: {obj["time"]} {time.strftime("%Y-%m-%d %H:%M:%S", current_time)}'
        print(msg)


class MailSender(Observer):
    def update(self, observable, obj):
        current_time = time.gmtime(obj["time"])
        msg = f'[郵件發送] {obj["name"]} 檢測到帳戶登入異常 ' \
              f'登入地區: {obj["region"]}' \
              f'登入時間: {obj["time"]} {time.strftime("%Y-%m-%d %H:%M:%S", current_time)}'
        print(msg)


def test_login():
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())
    account.login('Tony', '118.167.65.213', time.time())
    account.login('Tony', '67.218.147.69', time.time())


if __name__ == '__main__':
    test_login()
