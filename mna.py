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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 513,276 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.OpenScreen = wx.StaticText( self, wx.ID_ANY, u"HELLO YOU!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenScreen.Wrap( -1 )

		self.OpenScreen.SetFont( wx.Font( 30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.OpenScreen.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer1.Add( self.OpenScreen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 60 )

		self.Enter = wx.Button( self, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enter.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.Enter.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer1.Add( self.Enter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Header = wx.StaticText( self, wx.ID_ANY, u"What i'm want to do?", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.Header = wx.StaticText( self, wx.ID_ANY, u"The product description you want to upload as a request:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Header.Wrap( -1 )

		self.Header.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		self.Header.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer9.Add( self.Header, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer9.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		m_comboBox3Choices = []
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		bSizer9.Add( self.m_comboBox3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer9.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		bSizer9.Add( self.m_listBox2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


