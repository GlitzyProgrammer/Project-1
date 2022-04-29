class Television:
    """
    This class is used to represent the Television object and also establish four variables for
    which the methods would call upon.
    """

    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create a starter status of the Television object.
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Method to change the self.__status when the method is called.
        """
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method to incrimate the self.__channel by 1.
        """

        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to change the self.__channel by -1.
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to modify the self.__volume by 1.
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to change the self.__volume by -1.
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return a string to tell the Television's object status.
        :return: returns status, tv volume and channle number
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
