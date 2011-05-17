#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import os, os.path, sys, pygtk, gtk

class pyWine:
    """This is the PyWine application"""

    def __init__(self):

        # Set the Glade file
        self.gladefile = "MainWindow.ui"
        self.wTree = gtk.Builder()
        self.wTree.add_from_file(os.path.join(os.path.dirname("__file__"), self.gladefile))

        # Create our dictionary and connect it
        dic = {"on_MainWindow_destroy" : gtk.main_quit
               , "on_AddWine" : self.onAddWine
               }
        self.wTree.connect_signals(dic)

        # Here are some variables that can be resued later
        self.cWine = 0
        self.cWinery = 1
        self.cGrape = 2
        self.cYear = 3

        self.sWine = "Wine"
        self.sWinery = "Winery"
        self.sGrape = "Grape"
        self.sYear = "Year"

        # Get the treeView from the widget Tree
        self.wineView = self.wTree.get_object("wineView")
        # Add all of the List Columns to the wineView
        self.AddWineListColumn(self.sWine, self.cWine)
        self.AddWineListColumn(self.sWinery, self.cWinery)
        self.AddWineListColumn(self.sGrape, self.cGrape)
        self.AddWineListColumn(self.sYear, self.cYear)

        # Create the listStore Model to use with the wineView
        self.wineList = gtk.ListStore(str, str, str, str)
        # Attatch the model to the treeView
        self.wineView.set_model(self.wineList)

        self.mainWindow = self.wTree.get_object("MainWindow")
        self.mainWindow.show_all()

    def onAddWine(self, widget):
        """Called when the use wants to add a wine"""
        # Create the dialog, show it, and stre the results
        wineDlg = wineDialog();
        result, newWine = wineDlg.run()

        if (result == gtk.RESPONSE_OK):
            """The use clicked Ok, so let's add this
            wine to the wine list"""
            self.wineList.append(newWine.getList())

    def AddWineListColumn(self, title, columnId):
        """This function adds a column to the list view.
        First it creates the gtk.TreeViewColumn and then set
        some needed properties"""
        column = gtk.TreeViewColumn(title, gtk.CellRendererText() \
                                    , text = columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.wineView.append_column(column)

class Wine:
    """This class represents all the wine information"""

    def __init__(self, wine = "", winery = "", grape = "", year = ""):
        self.wine = wine
        self.winery = winery
        self.grape = grape
        self.year = year

    def getList(self):
        """This function returns a list made up of the
        wine information. It is used to add a wine to the
        wineList easily"""
        return [self.wine, self.winery, self.grape, self.year]

class wineDialog:
    """This class is used to show winDlg"""

    def __init__(self, wine = "", winery = "", grape = "", year = ""):

        # setup the glade file
        self.gladefile = "WineDlg.ui"
        # setup the wine that we will return
        self.wine = Wine(wine, winery, grape, year)

    def run(self):
        """This function will show the wine Dlg"""
        self.gladefile = "wineDlg.ui"

        # load the dialog from the glade file
        self.wTree = gtk.Builder()
        self.wTree.add_from_file(os.path.join(os.path.dirname("__file__"), self.gladefile))
        # Get the actual dialog widget
        self.dlg = self.wTree.get_object("wineDlg")
        # Get all of the Entry Widgets and set their text
        self.enWine = self.wTree.get_object("enWine")
        self.enWine.set_text(self.wine.wine)
        self.enWinery = self.wTree.get_object("enWinery")
        self.enWinery.set_text(self.wine.winery)
        self.enGrape = self.wTree.get_object("enGrape")
        self.enGrape.set_text(self.wine.grape)
        self.enYear = self.wTree.get_object("enYear")
        self.enYear.set_text(self.wine.year)

        # run the dialog and store the response
        self.result = self.dlg.show_all()
        # get the value of the entry fields
        self.wine.wine = self.enWine.get_text()
        self.wine.winery = self.enWinery.get_text()
        self.wine.grape = self.enGrape.get_text()
        self.wine.year = self.enYear.get_text()

        # we are done with the dialog, destroy it
        self.dlg.destroy()

        # return the result and the wine
        return self.result, self.wine

if __name__ == '__main__':
    wine = pyWine()
    gtk.main()
