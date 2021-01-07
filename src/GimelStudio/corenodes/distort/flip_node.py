# THIS FILE IS A PART OF GIMEL STUDIO AND IS LICENSED UNDER THE SAME TERMS:
# ----------------------------------------------------------------------------
# Gimel Studio Copyright 2019-2020 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import numpy as np

from GimelStudio import api


class FlipNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Flip",
            "author": "iwoithe",
            "version": (0, 0, 1),
            "supported_app_version": (0, 5, 0),
            "category": "DISTORT",
            "description": "Flips the image horizontally or vertically.",
        }
        return meta_info

    def NodeInitProps(self):
        p = api.ChoiceProp(
            idname="Direction",
            default="Horizontal",
            label="Direction:",
            choices=["Horizontal", "Vertical"],
        )
        self.NodeAddProp(p)

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')

        self.NodeAddParam(p)

    def NodeEvaluation(self, params, props):
        image1 = params['Image']
        direction = props['Direction']

        render_image = api.RenderImage()

        if direction == 'Horizontal':
            render_image.SetAsImage(np.fliplr(image1.GetImage()))
        else:
            render_image.SetAsImage(np.flipud(image1.GetImage()))

        return render_image


api.RegisterNode(FlipNode, "corenode_flip")
