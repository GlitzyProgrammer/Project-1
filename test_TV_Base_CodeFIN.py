import tkinter

from TV_Base_Code import *

class TestWindow:
    def __init__(self,root):
        self.root = tkinter.Tk
        self.root.mainloop()

    def powerbutton(self,root):
        self.p = tkinter.Button(root)





    def setup(self,window):
        self.tv = Television(window)
        self.tv = tkinter.Tk()
        self.window = window



    def teardown(self, window):
        del self.tv

    def test_init(self, window):
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self, window):
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
       # self.test_power(self, window)
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_up(self, window):
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'

    def test_channel_down(self, window):
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'

        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'

    def test_volume_up(self,window):
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'