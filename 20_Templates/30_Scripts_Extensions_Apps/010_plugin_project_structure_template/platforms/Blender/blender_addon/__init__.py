"""
⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS

Blender add-on entry point (platform overlay).
Copy into your repo at: blender_addon/__init__.py
Replace all [REPLACE_ME] placeholders.
"""

bl_info = {
    "name": "[REPLACE_ME:ADDON_DISPLAY_NAME]",
    "author": "[REPLACE_ME:AUTHOR]",
    "version": ([REPLACE_ME:MAJOR], [REPLACE_ME:MINOR], [REPLACE_ME:PATCH]),
    "blender": ([REPLACE_ME:BLENDER_MAJOR], [REPLACE_ME:BLENDER_MINOR], 0),
    "location": "[REPLACE_ME:UI_LOCATION]",
    "description": "[REPLACE_ME:DESCRIPTION]",
    "category": "[REPLACE_ME:CATEGORY]",
}

from .utils.logging_utils import get_logger
from .ui.panel_main import register_ui, unregister_ui
from .operators.op_example import register_ops, unregister_ops

_LOG = get_logger(__name__)


def register():
    _LOG.info("Registering add-on: %s", bl_info.get("name"))
    register_ops()
    register_ui()


def unregister():
    _LOG.info("Unregistering add-on: %s", bl_info.get("name"))
    unregister_ui()
    unregister_ops()

