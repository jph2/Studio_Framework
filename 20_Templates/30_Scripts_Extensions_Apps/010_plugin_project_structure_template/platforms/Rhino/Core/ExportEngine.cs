// TEMPLATE FILE - DO NOT SHIP AS-IS
using Rhino;

namespace RhinoUSDMultiExport.Core
{
    public class ExportEngine
    {
        private readonly RhinoDoc _doc;

        public ExportEngine(RhinoDoc doc)
        {
            _doc = doc;
        }

        public bool ExportAll()
        {
            // Placeholder implementation for scaffolding.
            RhinoApp.WriteLine("TODO: implement export logic for " + _doc.Name);
            return true;
        }
    }
}
