#!/usr/bin/env python

import os
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QWorkspace, QAction, QApplication

from pivy.quarter import QuarterWidget

sys.path.append("/usr/lib/freecad/lib")
import FreeCADGui


class MdiQuarterWidget(QuarterWidget):
	def __init__(self, parent, sharewidget):
		QuarterWidget.__init__(self, parent=parent, sharewidget=sharewidget)

	def minimumSizeHint(self):
		return QtCore.QSize(640, 480)


class MdiMainWindow(QMainWindow):
	def __init__(self, qApp):
		QMainWindow.__init__(self)
		self._firstwidget = None
		self._workspace = QWorkspace()
		self.setCentralWidget(self._workspace)
		self.setAcceptDrops(True)
		self.setWindowTitle("Pivy Quarter MDI example")

		self.createBoxInFreeCAD()

		windowmapper = QtCore.QSignalMapper(self)
		self.connect(windowmapper, QtCore.SIGNAL("mapped(QWidget *)"), self._workspace.setActiveWindow)

		self.dirname = os.curdir

	def closeEvent(self, event):
		self._workspace.closeAllWindows()

	def createBoxInFreeCAD(self):
		d=FreeCAD.newDocument()
		o=d.addObject("Part::Box")
		d.recompute()
		s=FreeCADGui.subgraphFromObject(o)
		child = self.createMdiChild()
		child.show()
		child.setSceneGraph(s)

	def createMdiChild(self):
		widget = MdiQuarterWidget(None, self._firstwidget)
		self._workspace.addWindow(widget)
		if not self._firstwidget:
			self._firstwidget = widget
		return widget


def main():
	app = QApplication(sys.argv)
	FreeCADGui.setupWithoutGUI()
	mdi = MdiMainWindow(app)
	mdi.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
