#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graphics
import sys

from PyQt4.QtGui import QApplication

sys.path.append("/usr/lib/freecad/lib")
import FreeCADGui


def main():
	app = QApplication(sys.argv)
	
	FreeCADGui.setupWithoutGUI()
	d=FreeCAD.newDocument()
	o=d.addObject("Part::Box")
	d.recompute()
	s=FreeCADGui.subgraphFromObject(o)
	
	mdi = graphics.MdiMainWindow(app, s)
	mdi.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
