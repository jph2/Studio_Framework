"""
⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS

Example operator scaffold (platform overlay).
"""

import bpy

from ..utils.logging_utils import get_logger

_LOG = get_logger(__name__)


class TEMPLATE_OT_example(bpy.types.Operator):
    bl_idname = "template.example"
    bl_label = "Template Example"
    bl_description = "Example operator (template)"

    def execute(self, context):  # noqa: ARG002
        _LOG.info("Template operator executed")
        self.report({"INFO"}, "Template operator executed")
        return {"FINISHED"}


_CLASSES = (TEMPLATE_OT_example,)


def register_ops():
    for cls in _CLASSES:
        bpy.utils.register_class(cls)


def unregister_ops():
    for cls in reversed(_CLASSES):
        bpy.utils.unregister_class(cls)

