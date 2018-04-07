# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QWorkspace

from pivy.quarter import QuarterWidget


class MdiQuarterWidget(QuarterWidget):
	def __init__(self, parent, sharewidget):
		QuarterWidget.__init__(self, parent=parent, sharewidget=sharewidget)

	def minimumSizeHint(self):
		return QtCore.QSize(640, 480)


class MdiMainWindow(QMainWindow):
	def __init__(self, qApp, freecadGraph):
		QMainWindow.__init__(self)
		self._firstwidget = None
		self._workspace = QWorkspace()
		self.setCentralWidget(self._workspace)
		self.setAcceptDrops(True)
		self.setWindowTitle("Pivy Quarter MDI example")

		child = self.createMdiChild()
		child.show()
		child.setSceneGraph(freecadGraph)

		windowmapper = QtCore.QSignalMapper(self)
		self.connect(QtCore.QSignalMapper(self), QtCore.SIGNAL("mapped(QWidget *)"), self._workspace.setActiveWindow)

	def closeEvent(self, event):
		self._workspace.closeAllWindows()

	def createMdiChild(self):
		widget = MdiQuarterWidget(None, self._firstwidget)
		self._workspace.addWindow(widget)
		if not self._firstwidget:
			self._firstwidget = widget
		return widget

