# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# constants
google_mail = 'google_mail'
twiki = 'twiki'
bn = 'bn'
shared = 'shared'
schedule = 'schedule'
translator = 'translator'
ushare = 'ushare'
chat = 'chat'
vision = 'vision'
uber = 'uber'
nagios = 'nagios'
hic = 'hic'
dhs = 'dhs'
qc1 = 'qc1'
wwi = 'wwi'
dsj = 'dsj'
mp = 'mp'
mp_100 = 'mp_100'

left_coord = [61, 124, 1650, 954]
middle_coord = [177, 52, 1632, 1028]
right_coord = [432, 228, 1488, 852]

deploy_flow = [google_mail, shared, schedule, translator, twiki, ushare, chat, vision, uber, nagios, bn, hic, dhs, qc1,
               wwi, dsj, mp, mp_100]


class Window(object):
    absolute_list = [google_mail, twiki, bn]
    cred_list = [google_mail, ushare, chat, vision, uber, nagios, bn, hic, dhs, qc1, wwi, dsj, mp, mp_100]
    index_ = 0

    def __init__(self):
        self.name = str(deploy_flow[Window.index_])
        self.index_ = Window.index_
        Window.index_ += 1

    @property
    def is_absolute(self):
        return True if self.name in Window.absolute_list else False

    @property
    def has_credentials(self):
        return True if self.name in Window.cred_list else False

    @staticmethod
    def take_info():
        with open('creds.txt', 'r') as f:
            return list(f)

    def new_window(self):
        pass

    def new_tab(self):
        pass


class CertainWindow(Window):

    def __init__(self, link):
        super().__init__()
        self.link = link

    def position(self):
        if self.is_absolute:
            if self.name == google_mail:
                return left_coord
            elif self.name == twiki:
                return middle_coord
            elif self.name == bn:
                return right_coord
            else:
                pass
        else:
            raise ValueError("This service must be addicted to absolute")

    def deploy(self):
        if self.is_absolute:
            self.new_window()
        else:
            self.new_tab()


def main():
    some_job = []
    for _ in deploy_flow:
        some_job.append(CertainWindow(_))

    for instance_ in some_job:
        instance_.deploy()


if __name__ == '__main__':
    main()
