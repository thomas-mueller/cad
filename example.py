#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graphics
import sys
import os

from PyQt4.QtGui import QApplication

sys.path.append("/usr/lib/freecad/lib")
import FreeCAD as App
import FreeCADGui as Gui


def main():
	app = QApplication(sys.argv)
	
	Gui.setupWithoutGUI()
	document = App.newDocument()
	box = document.addObject("Part::Box")
	
	document.recompute()
	
	projectFilename = "example.fcstd"
	if os.path.exists(projectFilename):
		os.remove(projectFilename)
	document.saveAs(projectFilename)
	
	graph = Gui.subgraphFromObject(box)
	
	mdi = graphics.MdiMainWindow(app, graph)
	mdi.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
