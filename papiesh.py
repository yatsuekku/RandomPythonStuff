import datetime as dt
import threading
from time import sleep


def papiesh(cls: type):
    """
    Created by Mikhail Bialkov
    :param cls:
    :return:
    """
    rozum_i_godnosc_czlowieka = """Jan Pawel II byl wielkim polakiem"""

    class Jp2(cls):
        instances = {}

        @staticmethod
        def kurdabelaPoraSpac():
            while dt.datetime.now().minute != 37 or dt.datetime.now().hour != 21:
                sleep(1)
            for ins in Jp2.instances:
                for att in dir(ins):
                    setattr(ins, att, rozum_i_godnosc_czlowieka)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            Jp2.instances[self] = self

    threading.Thread(target=Jp2.kurdabelaPoraSpac).start()
    return Jp2
