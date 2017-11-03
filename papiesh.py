import datetime as dt
import threading
from time import sleep

def papiesh(cls: type):
    """
    Created By Mikhail Bialkov
    :param cls:
    :return:
    """

    class Jp2(cls):
        instances = {}

        @staticmethod
        def kurdabelaPoraSpac():
            while dt.datetime.now().minute != 37 or dt.datetime.now().hour != 21:
                sleep(1)
            for ins in Jp2.instances:
                for att in dir(ins):
                    if '__' not in att:
                        setattr(ins, att, "Jan Pawel II byl wielkim polakiem")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            Jp2.instances[self] = self

    threading.Thread(target=Jp2.kurdabelaPoraSpac).start()
    return Jp2
