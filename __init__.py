# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright (C) 2018 Amir Shehata
#  http://www.openmovie.com
#  amir.shehata@gmail.com

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import traceback
from bpy.props import EnumProperty, StringProperty, BoolVectorProperty
from .icon_list import icons

bl_info = {
    "name": "YAID",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > UI > YAID",
    "author": "Amir Shehata <amir.shehata@gmail.com>",
    "description": "Yet Another Icon Display",
    "category": "display all the icons"
}

class YAID_PT_display_icons(bpy.types.Panel):
    bl_label = "Icon Display"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'YAID'

    def draw(self, context):
        scn = context.scene
        layout = self.layout
        row = layout.row(align=True)
        row.prop(scn, "icon_filter", text='')
        row = layout.row(align=True)
        i = 0
        for icon in icons:
            if scn.icon_filter.upper() not in icon.upper():
                continue
            if i > 4:
                row = layout.row(align=True)
                i = 0
            i = i + 1
            row.label(text=icon, icon=icon)

def register():
    bpy.utils.register_class(YAID_PT_display_icons)
    bpy.types.Scene.icon_filter= StringProperty(
        name="Icon Filter",
        subtype='FILE_NAME',
        default="",
        description='Filter icons on that string')

def unregister():
    bpy.utils.unregister_class(YAID_PT_display_icons)

if __name__ == "__main__":
    register()
