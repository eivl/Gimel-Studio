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
## FILE: image.py
## AUTHOR(S): Noah Rahm
## PURPOSE: Defines a generic image for the Image Viewport
## ----------------------------------------------------------------------------

import wx

from GimelStudio.utils import ConvertImageToWx


class GenericImage(object):
    def __init__(self, parent, image, pos=wx.Point(0, 0), _id=wx.ID_ANY):
        self._parent = parent
        self._image = image
        self._pos = pos

        if _id == wx.ID_ANY:
            self._id = wx.NewId()
        else:
            self._id = _id

        self._rect = wx.Rect(
            self._pos.x, 
            self._pos.y, 
            self._image.size[0], 
            self._image.size[1]
            )

    def GetParent(self):
        return self._parent

    def GetId(self):
        return self._id

    def SetId(self, id_):
        self._id = id_

    def GetRect(self):
        return self._rect

    def SetRect(self, rect):
        self._rect = rect

    def SetPosition(self, x, y):
        self._pos = wx.Point(x, y)

    def GetPosition(self):
        return self._pos

    def SetImage(self, image):
        self._image = image

    def GetImage(self):
        return self._image

    def Draw(self, dc):
        dc.ClearId(self.GetId())
        dc.SetId(self.GetId())

        dc.DrawBitmap(
            ConvertImageToWx(self.GetImage()),
            self._pos[0],
            self._pos[1],
            True # Use alpha mask
            )
