## ----------------------------------------------------------------------------
## Gimel Studio Copyright 2020 Noah Rahm, Correct Syntax. All rights reserved.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##    http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## FILE: export.py
## AUTHOR(S): Noah Rahm
## PURPOSE: Define the image export options tab of the Image Viewport
## ----------------------------------------------------------------------------

import wx
import wx.adv

from PIL import Image

from GimelStudio.utils import ConvertImageToWx, DrawCheckerBoard
from GimelStudio.datafiles.icons import *



class ExportOptionsPnl(wx.StaticBox):
    def __init__(self, parent, label="Export Options", size=wx.DefaultSize):
        wx.StaticBox.__init__(self, parent, label=label, size=size)

        # This gets the recommended amount of border space to use for items
        # within in the static box for the current platform.
        top_bd, other_bd = self.GetBordersForSizer()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(top_bd)

        self._exportForWebCheckBox = wx.CheckBox(self, label="Export for web")
        self._opimizedImageCheckBox = wx.CheckBox(self, label="Optimize image (if available)")

        self._imageQualitySliderLbl = wx.StaticText(self, -1, "Image quality (if available)")
        self._imageQualitySlider = wx.Slider(
            self, value=75, minValue=0, maxValue=95, size=(250, -1),
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS
            )
        self._imageQualitySlider.SetTickFreq(5)

        sizer.Add(self._exportForWebCheckBox, flag=wx.LEFT|wx.TOP, border=other_bd+10)
        sizer.Add((1,5))
        sizer.Add(self._opimizedImageCheckBox, flag=wx.LEFT, border=other_bd+10)
        sizer.Add((1,20))
        sizer.Add(self._imageQualitySliderLbl, flag=wx.LEFT, border=other_bd+10)
        sizer.Add(self._imageQualitySlider, flag=wx.LEFT, border=other_bd+10)


        self.SetSizer(sizer)



class ImagePreviewPnl(wx.Panel):
    def __init__(self, parent, size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, size=size)


        bmp = ICON_NODE_IMAGE_DARK.GetBitmap()
        img_preview = wx.StaticBitmap(self, -1, bmp, (80, 50), (bmp.GetWidth(), bmp.GetHeight()))









class ImageExportPnl(wx.Panel):
    def __init__(self, parent, size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, size=size)

        self._parent = parent

        self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_BORDER|wx.SP_LIVE_UPDATE)
        self.splitter.SetMinimumPaneSize(50)

        p1 = ExportOptionsPnl(self.splitter)
        p2 = ImagePreviewPnl(self.splitter)
        self.splitter.SplitVertically(p1, p2)





        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        button1 = wx.Button(self, -1, "Export Image...")


        self.sizer2.Add(button1, 1, wx.ALIGN_CENTER)


        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.splitter, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        self.SetSizer(self.sizer)


        self.Bind(wx.EVT_SIZE, self.OnSize)



    def OnSize(self, event):
        size = self.GetSize()
        self.splitter.SetSashPosition(size.x / 2)
        event.Skip()
















        # self.mainSizer = wx.BoxSizer(wx.VERTICAL)


        # self.innerSizer = wx.BoxSizer(wx.HORIZONTAL)


        # self.panel_staticbox = wx.StaticBox(
        #     self, id=wx.ID_ANY, 
        #     , 
        #     )

        # self.innerSizer.Add(img_preview, wx.EXPAND|wx.ALL)
        # self.innerSizer.Add(self.panel_staticbox, wx.EXPAND|wx.ALL)





        
        
        # self.mainSizer.Add(self.innerSizer, wx.EXPAND|wx.ALL)

        # btn1 = wx.Button(self, label="Export Image")
        # self.mainSizer.Add(btn1, wx.ALIGN_RIGHT)

        # self.SetSizer(self.mainSizer)







        # This gets the recommended amount of border space to use for items
        # within in the static box for the current platform.
        # top_bd, other_bd = self.panel_staticbox.GetBordersForSizer()

        # staticbox_sizer = wx.BoxSizer(wx.VERTICAL)
        # staticbox_sizer.AddSpacer(top_bd)

        # self.panel_staticbox.SetSizer(staticbox_sizer)

        # panel_sizer = wx.BoxSizer(wx.VERTICAL)
        # panel_sizer.Add(self.panel_staticbox, 1, wx.EXPAND|wx.ALL, other_bd+10)

        # # Node Properties UI
        # #selected_node.PropertiesUI(selected_node, self.panel_staticbox, staticbox_sizer)

        # self.optionsPnlSizer.Add(panel_sizer, wx.EXPAND|wx.ALL)

        # self._mainSizer.Add(self.optionsPnlSizer, wx.EXPAND|wx.ALL)

        # #
        # #self._mainSizer.Add(btn1, wx.EXPAND|wx.ALL)

        # 