from typing import cast
from PyQt6 import QtCore, QtGui, QtWidgets
from gotify_tray import gotify


class MessagesModelItem(QtGui.QStandardItem):
    def __init__(self, message: gotify.GotifyMessageModel, *args, **kwargs):
        super(MessagesModelItem, self).__init__()
        self.message = message


class MessagesModel(QtGui.QStandardItemModel):
    def setItem(self, row: int, column: int, item: MessagesModelItem) -> None:
        super(MessagesModel, self).setItem(row, column, item)

    def itemFromIndex(self, index: QtCore.QModelIndex) -> MessagesModelItem:
        return cast(MessagesModelItem, super(MessagesModel, self).itemFromIndex(index))