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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selles App", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.OpenScreen = wx.StaticText( self, wx.ID_ANY, u"HELLO YOU!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenScreen.Wrap( -1 )

		self.OpenScreen.SetFont( wx.Font( 30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.OpenScreen.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer1.Add( self.OpenScreen, 2, wx.ALIGN_CENTER_HORIZONTAL, 22 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 3 )

		self.Enter = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enter.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		self.SignIn = wx.Panel( self.Enter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 5, 2, 0, 0 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.OldUserNameBox = wx.TextCtrl( self.SignIn, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.OldUserNameBox, 0, wx.ALL, 5 )


		gSizer1.Add( bSizer17, 1, wx.EXPAND, 0 )

		self.UserName = wx.StaticText( self.SignIn, wx.ID_ANY, u":שם משתמש", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UserName.Wrap( -1 )

		self.UserName.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.UserName.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.UserName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.OldUserPasswordBox = wx.TextCtrl( self.SignIn, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.OldUserPasswordBox, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.Password = wx.StaticText( self.SignIn, wx.ID_ANY, u":סיסמה", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password.Wrap( -1 )

		self.Password.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.Password.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer1.Add( self.Password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SignIn.SetSizer( gSizer1 )
		self.SignIn.Layout()
		gSizer1.Fit( self.SignIn )
		self.Enter.AddPage( self.SignIn, u"התחבר", False )
		self.SignUp = wx.Panel( self.Enter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer11 = wx.GridSizer( 5, 2, 0, 0 )

		bSizer171 = wx.BoxSizer( wx.VERTICAL )

		self.NewUserNameBox = wx.TextCtrl( self.SignUp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer171.Add( self.NewUserNameBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer11.Add( bSizer171, 1, wx.EXPAND, 0 )

		self.UserName1 = wx.StaticText( self.SignUp, wx.ID_ANY, u":שם משתמש", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UserName1.Wrap( -1 )

		self.UserName1.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.UserName1.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer11.Add( self.UserName1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		self.NewUserPasswordBox = wx.TextCtrl( self.SignUp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.NewUserPasswordBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer11.Add( bSizer151, 1, wx.EXPAND, 5 )

		self.m_staticText111 = wx.StaticText( self.SignUp, wx.ID_ANY, u":סיסמה", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText111.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer11.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer17111 = wx.BoxSizer( wx.VERTICAL )

		self.NewUserPhoneBox = wx.TextCtrl( self.SignUp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17111.Add( self.NewUserPhoneBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer11.Add( bSizer17111, 1, wx.EXPAND, 5 )

		self.m_staticText11111 = wx.StaticText( self.SignUp, wx.ID_ANY, u": מספר טלפון", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11111.Wrap( -1 )

		self.m_staticText11111.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText11111.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer11.Add( self.m_staticText11111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Status = wx.BoxSizer( wx.HORIZONTAL )

		self.CustomerButton = wx.RadioButton( self.SignUp, wx.ID_ANY, u"לקוח", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CustomerButton.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.CustomerButton.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		Status.Add( self.CustomerButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer11.Add( Status, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		self.SellerButton = wx.RadioButton( self.SignUp, wx.ID_ANY, u"מוכר", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SellerButton.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.SellerButton.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer52.Add( self.SellerButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer11.Add( bSizer52, 1, wx.EXPAND, 5 )


		self.SignUp.SetSizer( gSizer11 )
		self.SignUp.Layout()
		gSizer11.Fit( self.SignUp )
		self.Enter.AddPage( self.SignUp, u"הרשם", True )

		bSizer18.Add( self.Enter, 0, wx.BOTTOM|wx.ALIGN_BOTTOM, 5 )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer18, 1, wx.ALIGN_CENTER_HORIZONTAL, 50 )

		self.EnterButton = wx.Button( self, wx.ID_ANY, u"כנס", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.EnterButton, 0, wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Enter.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.EnterOnNotebookPageChanged )
		self.CustomerButton.Bind( wx.EVT_RADIOBUTTON, self.CustomerButtonOnRadioButton )
		self.SellerButton.Bind( wx.EVT_RADIOBUTTON, self.SellerButtonOnRadioButton )
		self.EnterButton.Bind( wx.EVT_BUTTON, self.EnterButtonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def EnterOnNotebookPageChanged( self, event ):
		event.Skip()

	def CustomerButtonOnRadioButton( self, event ):
		event.Skip()

	def SellerButtonOnRadioButton( self, event ):
		event.Skip()

	def EnterButtonOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class CustomerScreen
###########################################################################

class CustomerScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Product Description", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		Description = wx.BoxSizer( wx.VERTICAL )

		self.Header = wx.StaticText( self, wx.ID_ANY, u"Your products:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Header.Wrap( -1 )

		self.Header.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, True, "Arial Black" ) )
		self.Header.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		Description.Add( self.Header, 2, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		Description.Add( ( 0, 0), 3, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 3 )

		self.CustomerProducts = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CustomerProducts.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		self.ProductsList = wx.Panel( self.CustomerProducts, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer97 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self.ProductsList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow2.SetSizer( bSizer20 )
		self.m_scrolledWindow2.Layout()
		bSizer20.Fit( self.m_scrolledWindow2 )
		bSizer97.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )

		self.DownloadButton = wx.Button( self.ProductsList, wx.ID_ANY, u"טען מוצרים קודמים", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer97.Add( self.DownloadButton, 0, wx.ALL, 5 )


		self.ProductsList.SetSizer( bSizer97 )
		self.ProductsList.Layout()
		bSizer97.Fit( self.ProductsList )
		self.CustomerProducts.AddPage( self.ProductsList, u"מוצרים קודמים", True )
		self.NewProduct = wx.Panel( self.CustomerProducts, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer11 = wx.GridSizer( 5, 2, 0, 0 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer171 = wx.BoxSizer( wx.VERTICAL )

		self.ProductTypeBox = wx.TextCtrl( self.NewProduct, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer171.Add( self.ProductTypeBox, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer11.Add( bSizer171, 1, wx.EXPAND, 0 )

		self.UserName1 = wx.StaticText( self.NewProduct, wx.ID_ANY, u":סוג המוצר", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UserName1.Wrap( -1 )

		self.UserName1.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.UserName1.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer11.Add( self.UserName1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		self.NoteBox = wx.TextCtrl( self.NewProduct, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.NoteBox, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer11.Add( bSizer151, 1, wx.EXPAND, 5 )

		self.Note = wx.StaticText( self.NewProduct, wx.ID_ANY, u":הערות ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Note.Wrap( -1 )

		self.Note.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.Note.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer11.Add( self.Note, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.AddButton = wx.Button( self.NewProduct, wx.ID_ANY, u"העלה מוצר", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AddButton.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.AddButton.SetForegroundColour( wx.Colour( 0, 128, 64 ) )
		self.AddButton.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		gSizer11.Add( self.AddButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.NewProduct.SetSizer( gSizer11 )
		self.NewProduct.Layout()
		gSizer11.Fit( self.NewProduct )
		self.CustomerProducts.AddPage( self.NewProduct, u"מוצר חדש", False )

		bSizer18.Add( self.CustomerProducts, 0, wx.BOTTOM|wx.ALIGN_BOTTOM, 5 )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		Description.Add( bSizer18, 1, wx.EXPAND, 5 )


		Description.Add( ( 0, 0), 3, wx.EXPAND, 5 )


		self.SetSizer( Description )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.DownloadButton.Bind( wx.EVT_BUTTON, self.DownloadedButton_OnButtonClick )
		self.AddButton.Bind( wx.EVT_BUTTON, self.AddButtonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def DownloadedButton_OnButtonClick( self, event ):
		event.Skip()

	def AddButtonOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class SellerRequestScreen
###########################################################################

class SellerRequestScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"suggestion", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		self.ProductTypeBox_Seller = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.ProductTypeBox_Seller, 0, wx.ALL|wx.EXPAND, 5 )


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
## Class SellerResultScreen
###########################################################################

class SellerResultScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"\"רשימת \"סוג ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY, False, "Arial Black" ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer21.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		GridOfPreviousProducts = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow3.SetSizer( GridOfPreviousProducts )
		self.m_scrolledWindow3.Layout()
		GridOfPreviousProducts.Fit( self.m_scrolledWindow3 )
		bSizer22.Add( self.m_scrolledWindow3, 4, wx.EXPAND |wx.ALL, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


