// TEMPLATE FILE - DO NOT SHIP AS-IS
using Rhino;
using Rhino.Commands;
using RhinoUSDMultiExport.Core;

namespace RhinoUSDMultiExport.Commands
{
    [CommandStyle(Style.ScriptRunner)]
    public class UsdMultiExportExportAll : Command
    {
        public override string EnglishName => "UsdMultiExportExportAll";

        protected override Result RunCommand(RhinoDoc doc, RunMode mode)
        {
            var engine = new ExportEngine(doc);
            var result = engine.ExportAll();

            RhinoApp.WriteLine(result ? "Export completed." : "Export failed.");
            return result ? Result.Success : Result.Failure;
        }
    }
}
