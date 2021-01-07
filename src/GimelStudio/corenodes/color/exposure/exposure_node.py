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

from GimelStudio import api


class ExposureNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Exposure",
            "author": "Correct Syntax",
            "version": (1, 0, 0),
            "supported_app_version": (0, 5, 0),
            "category": "COLOR",
            "description": "Adjusts the image exposure.",
            "gpu_support": "yes",
        }
        return meta_info

    def NodeInitProps(self):
        p = api.PositiveIntegerProp(
            idname="exposureValue",
            default=1,
            min_val=1,
            max_val=80,
            widget=api.SLIDER_WIDGET,
            label="Amount:",
        )
        self.NodeAddProp(p)

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')

        self.NodeAddParam(p)

    def NodeEvaluation(self, params, props):
        """
        render_image: the RenderImage class
        returns: the result of the image operation (Pillow Image, Numpy array, shader)
        """
        image1 = params['Image']

        render_image = api.RenderImage()

        result = self.RenderGLSL("./GimelStudio/corenodes/color/exposure/exposure.glsl", props, image1)
        render_image.SetAsImage(result)

        return render_image


api.RegisterNode(ExposureNode, "corenode_exposure")
