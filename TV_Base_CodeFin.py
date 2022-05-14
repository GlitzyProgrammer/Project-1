#Project link https://github.com/GlitzyProgrammer/Project-1
# Added features like a GUI  that functioned as a pseudo remote

from tkinter import *
class Television:
    """
    This class is used to represent the Television object and also establish four variables for
    which the methods would call upon.
    """
    global count
    count = 0
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume


    def __init__(self,window, *args, **kvargs)-> None:
        """
        Constructor to create a starter status of the Television object and creates the remote widget
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

        self.window = window
        self.Volume_Down = Button(window,command=self.volume_down, text="Volume Down", font=("Comic Sans", 12))
        self.Volume_Up = Button(window,command=self.volume_up, text='Volume Up', font=("Comic Sans", 12))
        self.Channel_Up = Button(window,command=self.channel_up, text='Channel Up', font=("Comic Sans", 12))
        self.Channel_Down = Button(window,command=self.channel_down, text='Channel Down', font=("Comic Sans", 12))
        self.Power = Button(window,command=self.power, text='Power', font=("Comic Sans", 12))
        self.ChannelLabel_0 = Label(window, text='0',font=('Comic Sans', 12))
        self.ChannelLabel_1 = Label(window, text='1',font=('Comic Sans', 12))
        self.ChannelLabel_2 = Label(window, text='2',font=('Comic Sans', 12))
        self.ChannelLabel_3 = Label(window, text='3',font=('Comic Sans', 12))
        self.VolumeLabel_0 = Label(window, text='0',font=('Comic Sans', 12))
        self.VolumeLabel_1 = Label(window, text='1', font=('Comic Sans', 12))
        self.VolumeLabel_2 = Label(window, text='2', font=('Comic Sans', 12))


        self.Power.grid(row=6, column=1, pady=10)
        self.Volume_Up.grid(row=2, column=0, padx=10)
        self.VolumeLabel_0.grid(row=3, column=0)
        self.Volume_Down.grid(row=4, column=0, padx=10)
        self.Channel_Down.grid(row=4, column=2)
        self.ChannelLabel_0.grid(row=3, column=2)
        self.Channel_Up.grid(row=2, column=2)

    def power(self) -> bool:
        """
        Method to change the self.__status when the method is called.
        """
        if self.__status == False:
            self.__status = True
            return self.__status
        elif self.__status == True:
            self.__status = False
            return self.__status


    def channel_up(self) -> None:
        """
        Method to incrimate the self.__channel by 1.
        """

        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.ChannelLabel_3.grid_remove()
                self.ChannelLabel_0.grid()
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
                if self.__channel == 1:
                    self.ChannelLabel_0.grid_remove()
                    self.ChannelLabel_1.grid(row=3,column=2)
                elif self.__channel == 2:
                    self.ChannelLabel_1.grid_remove()
                    self.ChannelLabel_2.grid(row=3,column=2)
                else:
                    self.ChannelLabel_2.grid_remove()
                    self.ChannelLabel_3.grid(row=3, column=2)

    def channel_down(self) -> None:
        """
        Method to change the self.__channel by -1.
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
                self.ChannelLabel_0.grid_remove()
                self.ChannelLabel_3.grid(row=3,column=2)
            else:
                self.__channel -= 1
                if self.__channel == 3:
                    self.ChannelLabel_2.grid_remove()
                    self.ChannelLabel_1.grid(row=3,column=2)
                elif self.__channel == 2:
                    self.ChannelLabel_3.grid_remove()
                    self.ChannelLabel_2.grid(row=3,column=2)
                elif self.__channel == 1:
                    self.ChannelLabel_2.grid_remove()
                    self.ChannelLabel_1.grid(row=3,column=2)
                else:
                    self.ChannelLabel_1.grid_remove()
                    self.ChannelLabel_0.grid(row=3,column=2)





    def volume_up(self) -> None:
        """
        Method to modify the self.__volume by 1.
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                if self.__volume == 1:
                    self.VolumeLabel_0.grid_remove()
                    self.VolumeLabel_1.grid(row=3,column=0)
                elif self.__volume == 2:
                    self.VolumeLabel_1.grid_remove()
                    self.VolumeLabel_2.grid(row=3,column=0)


    def volume_down(self) -> None:
        """
        Method to change the self.__volume by -1.
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                print(self.__volume)
                if self.__volume == 1:
                    self.VolumeLabel_2.grid_remove()
                    self.VolumeLabel_1.grid(row=3,column=0)
                elif self.__volume == 0:
                    self.VolumeLabel_1.grid_remove()
                    self.VolumeLabel_0.grid(row=3,column=0)


    def __str__(self) -> str:
        """
        Method to return a string to tell the Television's object status.
        :return: returns status, tv volume and channle number
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

    def status_display_on(self):
        global count
        count += 1
        if count <= 1:
         self.event()

    def event(self):
        global count
        while count <= 1:
            self.StatusBox.insert(1.0,f' TV status: Is on = {self.__status} \nChannel = {self.__channel}\nVolume = {self.__volume}')
            break

    def status_display_off(self):
        global count
        count = 0
        self.StatusBox.delete(1.0,'end')
