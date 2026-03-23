"""
⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS

Minimal UI panel scaffold (platform overlay).
"""

import bpy


class TEMPLATE_PT_main_panel(bpy.types.Panel):
    bl_label = "[REPLACE_ME:PANEL_LABEL]"
    bl_idname = "TEMPLATE_PT_main_panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"

    def draw(self, context):  # noqa: ARG002
        layout = self.layout
        layout.label(text="Template panel")
        layout.operator("template.example", text="Run Example")


_CLASSES = (TEMPLATE_PT_main_panel,)


def register_ui():
    for cls in _CLASSES:
        bpy.utils.register_class(cls)


def unregister_ui():
    for cls in reversed(_CLASSES):
        bpy.utils.unregister_class(cls)

