# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class OpenScreen
###########################################################################

class OpenScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selles App", pos = wx.DefaultPosition, size = wx.Size( 550,307 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.OpenScreen = wx.StaticText( self, wx.ID_ANY, u"HELLO YOU!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenScreen.Wrap( -1 )

		self.OpenScreen.SetFont( wx.Font( 30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.OpenScreen.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer1.Add( self.OpenScreen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 60 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Enter = wx.Button( self, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enter.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.Enter.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.Enter.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer18.Add( self.Enter, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer18, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Enter.Bind( wx.EVT_BUTTON, self.EnterOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def EnterOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class SellerOrCustomer
###########################################################################

class SellerOrCustomer ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Enter", pos = wx.DefaultPosition, size = wx.Size( 451,282 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Header = wx.StaticText( self, wx.ID_ANY, u"What do you want to do?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Header.Wrap( -1 )

		self.Header.SetFont( wx.Font( 25, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.Header.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer8.Add( self.Header, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( ( 0, 0), 1, 0, 3 )

		self.Customer = wx.Button( self, wx.ID_ANY, u"I wnat enter as a customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Customer.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.Customer.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer8.Add( self.Customer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Seller = wx.Button( self, wx.ID_ANY, u"I want enter as a seller", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Seller.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.Seller.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer8.Add( self.Seller, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Customer.Bind( wx.EVT_BUTTON, self.CustomerOnClick )
		self.Seller.Bind( wx.EVT_BUTTON, self.SellerOnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def CustomerOnClick( self, event ):
		event.Skip()

	def SellerOnClick( self, event ):
		event.Skip()


###########################################################################
## Class CustomerScreen
###########################################################################

class CustomerScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Product Description", pos = wx.DefaultPosition, size = wx.Size( 610,415 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		Description = wx.BoxSizer( wx.VERTICAL )

		self.Header = wx.StaticText( self, wx.ID_ANY, u"The product description you want to upload as a request:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Header.Wrap( -1 )

		self.Header.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		self.Header.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		Description.Add( self.Header, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 5, 2, 0, 0 )

		self.type = wx.StaticText( self, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.type.Wrap( -1 )

		self.type.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.type.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.type, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.TypeBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.TypeBox, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer17, 1, wx.EXPAND, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Coments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.m_staticText11.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.ComentsBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.ComentsBox, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.name = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name.Wrap( -1 )

		self.name.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.name.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.name, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.NameBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.NameBox, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer19, 1, wx.EXPAND, 0 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Phone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.PhoneBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.PhoneBox, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )


		bSizer13.Add( gSizer1, 3, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		Description.Add( bSizer13, 1, wx.EXPAND, 0 )

		self.AddButton = wx.Button( self, wx.ID_ANY, u"Add My Product", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AddButton.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.AddButton.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		Description.Add( self.AddButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Description )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.AddButton.Bind( wx.EVT_BUTTON, self.AddButtonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def AddButtonOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class SuccessScreen
###########################################################################

class SuccessScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"uploaded", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"The request was successfully uploaded!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer22.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( ( 0, 0), 2, wx.EXPAND, 0 )

		self.ButtonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonClose.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.ButtonClose.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer22.Add( self.ButtonClose, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class SellerScreen
###########################################################################

class SellerScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"suggestion", pos = wx.DefaultPosition, size = wx.Size( 610,415 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		Description = wx.BoxSizer( wx.VERTICAL )

		self.Header = wx.StaticText( self, wx.ID_ANY, u"What do you suggest?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Header.Wrap( -1 )

		self.Header.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		self.Header.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		Description.Add( self.Header, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		Description.Add( ( 0, 0), 2, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

		self.type = wx.StaticText( self, wx.ID_ANY, u"Product Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.type.Wrap( -1 )

		self.type.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.type.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.type, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.ProductName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.ProductName, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer17, 2, wx.EXPAND, 0 )


		bSizer13.Add( gSizer1, 3, wx.ALL|wx.EXPAND, 0 )


		bSizer13.Add( ( 0, 0), 2, wx.EXPAND, 5 )


		Description.Add( bSizer13, 1, wx.EXPAND, 0 )


		Description.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer35.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.matchButton = wx.Button( self, wx.ID_ANY, u"Find a match", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.matchButton.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.matchButton.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.matchButton.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer35.Add( self.matchButton, 1, wx.ALL, 5 )


		bSizer35.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		Description.Add( bSizer35, 2, wx.EXPAND, 5 )


		self.SetSizer( Description )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.matchButton.Bind( wx.EVT_BUTTON, self.matchButtonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def matchButtonOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Solution
###########################################################################

class Solution ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Solution for Seller", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer36 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


