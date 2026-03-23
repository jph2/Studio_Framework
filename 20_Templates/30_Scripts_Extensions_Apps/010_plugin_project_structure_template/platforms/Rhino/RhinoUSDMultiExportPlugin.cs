// TEMPLATE FILE - DO NOT SHIP AS-IS
// Replace placeholders before production use.
using System;
using System.Runtime.InteropServices;
using Rhino.PlugIns;

namespace RhinoUSDMultiExport
{
    [Guid("[REPLACE_ME:PLUGIN_GUID]")]
    public class RhinoUSDMultiExportPlugin : PlugIn
    {
        public RhinoUSDMultiExportPlugin()
        {
            Instance = this;
        }

        public static RhinoUSDMultiExportPlugin Instance { get; private set; }
    }
}
