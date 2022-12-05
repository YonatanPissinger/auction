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

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Enter = wx.Button( self, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enter.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.Enter.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.Enter.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer6.Add( self.Enter, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 5, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )


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

	def __del__( self ):
		pass


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

		self.type.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.type.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.type, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer17, 1, wx.EXPAND, 0 )

		self.color = wx.StaticText( self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.color.Wrap( -1 )

		self.color.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.color, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		productColorChoices = [ u"White", u"Black", u"Red", u"Green", u"Blue" ]
		self.productColor = wx.ComboBox( self, wx.ID_ANY, u"Transparent", wx.DefaultPosition, wx.DefaultSize, productColorChoices, 0 )
		self.productColor.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer21.Add( self.productColor, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer21, 1, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Coments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		gSizer1.Add( self.m_listBox2, 1, wx.ALL|wx.EXPAND, 5 )

		self.name = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name.Wrap( -1 )

		self.name.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.name, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_textCtrl21, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer19, 1, wx.EXPAND, 0 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Phone Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )


		bSizer13.Add( gSizer1, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		Description.Add( bSizer13, 1, wx.EXPAND, 0 )


		self.SetSizer( Description )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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
		bSizer22.Add( self.ButtonClose, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


