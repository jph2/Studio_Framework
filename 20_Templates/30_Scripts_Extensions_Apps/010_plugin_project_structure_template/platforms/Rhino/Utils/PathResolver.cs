// TEMPLATE FILE - DO NOT SHIP AS-IS
using System.IO;

namespace RhinoUSDMultiExport.Utils
{
    public static class PathResolver
    {
        public static string EnsureDirectory(string path)
        {
            Directory.CreateDirectory(path);
            return path;
        }
    }
}
