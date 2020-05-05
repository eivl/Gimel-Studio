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
## FILE: node_properties.py
## AUTHOR(S): Noah Rahm
## PURPOSE: -
## ----------------------------------------------------------------------------

import wx

from GimelStudio.datafiles.icons import *


class NodePropertyPanel(wx.Panel):
    def __init__(self, parent, size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, wx.ID_ANY, size=size)

        self._parent = parent
        self._selectednode = None

        self._mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(self._mainsizer)
        self._mainsizer.Fit(self)

        #self.SetBackgroundColour(wx.Colour('#4d4d4dff'))
        
 
    def UpdatePanelContents(self, selectednode):
        self._mainsizer.Clear(delete_windows=True)
 
        if selectednode != None:
            panel = wx.Panel(self)
            sizer = wx.GridBagSizer(5, 5)

            # Node Info
            icon = wx.StaticBitmap(panel,
                                   bitmap=ICON_NODE_IMAGE_DARK.GetBitmap())
            sizer.Add(icon, pos=(0, 0), flag=wx.TOP|wx.LEFT, border=10)

            labeltext = wx.StaticText(panel, label=selectednode.GetLabel())
            #labeltext.SetForegroundColour('white')
            sizer.Add(labeltext, pos=(0, 1),
                      flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)

            line = wx.StaticLine(panel)
            #line.SetForegroundColour('white')
            sizer.Add(line, pos=(1, 0), span=(1, self.Size[0]),
                      flag=wx.EXPAND|wx.BOTTOM, border=4)

            # Node Properties UI
            selectednode.PropertiesUI(selectednode, wx, panel, sizer)

            sizer.AddGrowableCol(2)
            panel.SetSizer(sizer)
            sizer.Fit(self)

            self._mainsizer.Add(panel, wx.EXPAND)
        else:
            self._mainsizer.Clear(delete_windows=True)

        self._parent._mgr.Update()
        self._parent.Refresh()
        self._parent.Update()
