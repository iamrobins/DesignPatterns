from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

# Base State class with unimplemented state transition methods
class State:
    def __init__(self, player: AudioPlayer) -> None:
        self.player = player

    def clickLock(self) -> None:
        raise NotImplementedError

    def clickPlay(self) -> None:
        raise NotImplementedError

    def clickNext(self) -> None:
        raise NotImplementedError

    def clickPrevious(self) -> None:
        raise NotImplementedError

# Concrete State for Locked behavior
class LockedState(State):
    def clickLock(self) -> None:
        if self.player.playing:
            self.player.changeState(PlayingState(self.player))
        else:
            self.player.changeState(ReadyState(self.player))

    def clickPlay(self) -> None:
        pass

    def clickNext(self) -> None:
        pass

    def clickPrevious(self) -> None:
        pass

# Concrete State for Ready behavior
class ReadyState(State):
    def clickLock(self) -> None:
        self.player.changeState(LockedState(self.player))

    def clickPlay(self) -> None:
        self.player.startPlayback()
        self.player.changeState(PlayingState(self.player))

    def clickNext(self) -> None:
        self.player.nextSong()

    def clickPrevious(self) -> None:
        self.player.previousSong()

# Concrete State for Playing behavior
class PlayingState(State):
    def clickLock(self) -> None:
        self.player.changeState(LockedState(self.player))

    def clickPlay(self) -> None:
        self.player.stopPlayback()
        self.player.changeState(ReadyState(self.player))

    def clickNext(self) -> None:
        if self.player.event.doubleclick:
            self.player.nextSong()
        else:
            self.player.fastForward(5)

    def clickPrevious(self) -> None:
        if self.player.event.doubleclick:
            self.player.previousSong()
        else:
            self.player.rewind(5)

# Context class that changes behavior based on its state
class AudioPlayer:
    def __init__(self) -> None:
        self.state: State = ReadyState(self)  # Initial state
        self.UI = UserInterface()
        self.UI.lockButton.onClick(self.clickLock)
        self.UI.playButton.onClick(self.clickPlay)
        self.UI.nextButton.onClick(self.clickNext)
        self.UI.prevButton.onClick(self.clickPrevious)
        self.volume = 0
        self.playlist = []
        self.currentSong = None
        self.playing = False
        self.event = Event()

    def changeState(self, state: State) -> None:
        self.state = state

    def clickLock(self) -> None:
        self.state.clickLock()

    def clickPlay(self) -> None:
        self.state.clickPlay()

    def clickNext(self) -> None:
        self.state.clickNext()

    def clickPrevious(self) -> None:
        self.state.clickPrevious()

    def startPlayback(self) -> None:
        self.playing = True
        print("Playback started")

    def stopPlayback(self) -> None:
        self.playing = False
        print("Playback stopped")

    def nextSong(self) -> None:
        print("Next song")

    def previousSong(self) -> None:
        print("Previous song")

    def fastForward(self, time: int) -> None:
        print(f"Fast forward {time} seconds")

    def rewind(self, time: int) -> None:
        print(f"Rewind {time} seconds")

# Button class that can assign click handlers
class Button:
    def __init__(self) -> None:
        self.onclick = None

    def onClick(self, handler: Any) -> None:
        self.onclick = handler

# User interface class containing the player controls
class UserInterface:
    def __init__(self) -> None:
        self.lockButton = Button()
        self.playButton = Button()
        self.nextButton = Button()
        self.prevButton = Button()

# Event class to simulate double-click events
class Event:
    def __init__(self) -> None:
        self.doubleclick = False
