---
arys_schema_version: '1.2'
id: 667664c0-5fdc-4d95-ac34-e22e17d8d8ff
title: Templates
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:28Z'
last_modified: '2026-02-18T05:33:28Z'
---

# Templates

**Version**: 1.0.0 | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Scripts_Extensions_Apps_AUTO

**Tag block:**
#best_practices #automation #framework_integration #openusd #usd_core #omniverse #validation #quality_assurance #conversion #workflow_automation #extension_development

This directory contains reusable templates and foundations for USD/Omniverse development scripts.

## Available Templates

### Enhanced Script Template (`TemplateScript_V01.py`)
**Purpose**: Compliant foundation for USD/Omniverse Python development scripts.

**Features**:
- **Configuration Rules Compliant**: Meets all script configuration requirements
- **Unified Configuration System**: Integrates with General_Scripts_Extensions_Apps configuration framework
- **Standardized Logging**: Consistent logging patterns across all tools
- **USD Environment Validation**: Automatic validation of USD dependencies
- **Modular Operation Structure**: Easy to add new operations and functionality
- **Error Handling**: Robust error handling with detailed reporting
- **Execution Tracking**: Comprehensive execution statistics and timing
- **Automatic Timestamps**: Built-in timestamp management

## Quick Start

### 1. **Basic Usage**
```python
from tools.templates.TemplateScript_V01 import EnhancedScriptTemplate

# Create template instance
template = EnhancedScriptTemplate()

# Execute script
result = template.execute_script()
print(f"Success: {result['success']}")
```

### 2. **With Custom Configuration**
```python
from tools.config.base_config import BaseConfig
from tools.templates.TemplateScript_V01 import EnhancedScriptTemplate

# Create custom configuration
config = BaseConfig()
config.LOG_LEVEL = "high"
config.DRY_RUN = True

# Create template with configuration
template = EnhancedScriptTemplate(config)

# Execute
result = template.execute_script()
```

### 3. **Extending the Template**
```python
class MyCustomScript(EnhancedScriptTemplate):
    def __init__(self):
        super().__init__()
        # Custom initialization
    
    def _execute_operations(self) -> Dict[str, Any]:
        """Override to implement custom operations."""
        self.log_info("Starting custom operation...")
        
        result = {
            "operation": "Custom Operation",
            "success": True,
            "items_processed": 0,
            "execution_time": "0.0s"
        }
        
        try:
            # Your custom logic here
            self.log_info("Custom operation completed successfully")
            
        except Exception as e:
            self.log_error(f"Custom operation failed: {str(e)}")
            result["success"] = False
        
        return result

# Usage
script = MyCustomScript()
result = script.execute_script()
```

## Template Structure

### **Core Components**

#### 1. **Configuration Management**
- **Unified Configuration**: Integrates with `BaseConfig` system
- **Fallback Support**: Works even without unified configuration
- **Tool Metadata**: Automatic tool name, version, and category management

#### 2. **Logging System**
- **Multiple Levels**: None, Medium, High (Debug)
- **File and Console**: Simultaneous file and console logging
- **Timestamped**: All log entries include timestamps
- **Configurable**: Log level controlled by configuration

#### 3. **Operation Framework**
- **Modular Design**: Easy to add new operations by overriding `_execute_operations()`
- **Result Tracking**: Structured result objects for each operation
- **Error Handling**: Comprehensive error capture and reporting
- **Execution Statistics**: Automatic tracking of operations, errors, and warnings

#### 4. **USD Integration**
- **Environment Validation**: Automatic USD dependency checking
- **Best Practices**: Follows USD development standards
- **Error Handling**: Graceful handling of USD import failures

### **Template Methods**

#### **Core Methods**
- `__init__(config)`: Initialize template with configuration
- `execute_script()`: Main execution method (calls required logging functions)
- `_execute_operations()`: Override this method to implement custom operations

#### **Logging Methods**
- `log_info(message)`: Log information message
- `log_error(message)`: Log error message
- `log_warning(message)`: Log warning message
- `log_debug(message)`: Log debug message

#### **Utility Methods**
- `validate_environment()`: Validate environment readiness
- `_create_error_result(error_message)`: Create standardized error results
- `_log_execution_summary()`: Log execution summary and statistics

## Customization Guide

### **1. Adding New Operations**

Override the `_execute_operations()` method:

```python
def _execute_operations(self) -> Dict[str, Any]:
    """Execute the main operations - override in subclasses."""
    self.log_info("Starting my custom operations...")
    
    result = {
        'operation': 'My Custom Operations',
        'success': True,
        'items_processed': 0,
        'execution_time': '0.0s'
    }
    
    try:
        # Your operation logic here
        self.log_info("Operations completed successfully")
        
    except Exception as e:
        self.log_error(f"Operations failed: {str(e)}")
        result["success"] = False
    
    return result
```

### **2. Adding Custom Methods**

```python
def my_custom_method(self, parameter: str) -> str:
    """My custom method implementation."""
    self.log_info(f"Executing custom method with: {parameter}")
    
    try:
        # Your custom logic here
        result = f"Processed: {parameter}"
        self.log_info("Custom method completed successfully")
        return result
        
    except Exception as e:
        self.log_error(f"Custom method failed: {str(e)}")
        raise
```

### **3. Custom Configuration**

```python
def __init__(self, config: Optional[BaseConfig] = None):
    super().__init__(config)
    
    # Add custom configuration
    self.custom_setting = "my_value"
    self.custom_timeout = 30
```

## Configuration Options

### **Basic Configuration**
```python
# Logging levels
config.LOG_LEVEL = "none"      # No logging
config.LOG_LEVEL = "medium"    # Standard information
config.LOG_LEVEL = "high"      # Debug information

# Operation settings
config.DRY_RUN = True          # Test mode (no actual changes)
config.ROOT_DIRECTORY = "/path/to/root"
config.OUTPUT_DIR = "/path/to/output"
```

### **Template-Specific Settings**
```python
# Script metadata
SCRIPT_NAME = "My Custom Script"
SCRIPT_VERSION = "1.0.0"
SCRIPT_CATEGORY = "materials"

# Operation settings
ROOT_DIRECTORY = r"C:\path\to\usd\files"
FILE_PATTERN = "*.usd"
DRY_RUN = True
LOG_LEVEL = "medium"
```

## Best Practices

### **1. **Always Inherit from Template**
```python
class MyScript(EnhancedScriptTemplate):
    def __init__(self):
        super().__init__()
        # Custom initialization
```

### **2. **Use Structured Results**
```python
result = {
    "operation": "Operation Name",
    "success": True,
    "items_processed": 0,
    "execution_time": "0.0s"
}
```

### **3. **Proper Error Handling**
```python
try:
    # Your operation logic
    pass
except Exception as e:
    self.log_error(f"Operation failed: {str(e)}")
    return self._create_error_result(str(e))
```

### **4. **Use Logging Methods**
```python
self.log_info("Starting operation...")
self.log_debug("Processing item...")
self.log_warning("Potential issue...")
self.log_error("Operation failed...")
```

### **5. **Validate Environment**
```python
if not self.validate_environment():
    self.log_error("Environment validation failed")
    return self._create_error_result("Environment validation failed")
```

## Integration Examples

### **Material Tool Integration**
```python
from tools.config.material_config import MaterialConfig
from tools.templates.TemplateScript_V01 import EnhancedScriptTemplate

class MaterialScript(EnhancedScriptTemplate):
    def __init__(self):
        config = MaterialConfig()
        super().__init__(config)
    
    def _execute_operations(self) -> Dict[str, Any]:
        """Material-specific operations."""
        self.log_info("Starting material processing...")
        
        result = {
            'operation': 'Material Processing',
            'success': True,
            'items_processed': 0,
            'execution_time': '0.0s'
        }
        
        try:
            # Material processing logic here
            self.log_info("Material processing completed")
            
        except Exception as e:
            self.log_error(f"Material processing failed: {str(e)}")
            result["success"] = False
        
        return result
```

### **Variant Tool Integration**
```python
from tools.config.variant_config import VariantConfig
from tools.templates.TemplateScript_V01 import EnhancedScriptTemplate

class VariantScript(EnhancedScriptTemplate):
    def __init__(self):
        config = VariantConfig()
        super().__init__(config)
    
    def _execute_operations(self) -> Dict[str, Any]:
        """Variant-specific operations."""
        # Your variant processing logic here
        pass
```

## Compliance Features

### **Configuration Rules Compliance**
- ✅ **Required Sections**: CUSTOMIZE and DERIVED sections present
- ✅ **Timestamps**: Created and Last edited time in correct format
- ✅ **Version**: Semantic versioning (1.0.0)
- ✅ **Required Functions**: print_script_start() and print_script_end() called
- ✅ **Structure**: Proper shebang, docstring, and organization

### **Automatic Compliance**
- **Build Script Integration**: Works with automated build system
- **Timestamp Updates**: Automatic timestamp management
- **Version Control**: Semantic versioning support
- **Validation**: Built-in compliance checking

## Troubleshooting

### **Common Issues**

#### **1. USD Import Errors**
```
Warning: USD Python bindings not available
```
**Solution**: Install USD Python bindings or use fallback configuration.

#### **2. Configuration Import Errors**
```
Warning: Configuration system not available
```
**Solution**: Ensure proper import paths or use standalone mode.

#### **3. Logging Setup Failures**
```
Warning: Could not setup logging: [Error details]
```
**Solution**: Check output directory permissions and disk space.

### **Debug Mode**
Enable debug logging for detailed information:
```python
config.LOG_LEVEL = "high"
```

## Dependencies

- **Required**: Python 3.7+, standard library modules
- **Optional**: `pxr` (USD Python bindings)
- **Optional**: `tools.config.base_config` (Unified configuration system)

## License

This template is part of the General_Scripts_Extensions_Apps framework and is licensed under the MIT License.

## Contributing

When contributing new templates or enhancements:

1. **Follow the established pattern** in `TemplateScript_V01.py`
2. **Ensure compliance** with script configuration rules
3. **Use the unified configuration system** when possible
4. **Include comprehensive documentation** and examples
5. **Test with both USD and non-USD environments**
6. **Follow the error handling and logging patterns**

## Version History

- **v1.0.0**: Compliant template with unified configuration system
- **Previous versions**: Basic template with logging and user input

## Build System Integration

This template integrates with the automated build system:

- **Automatic Timestamps**: Updated via build script
- **Version Management**: Incremented automatically
- **Compliance Checking**: Validated against configuration rules
- **Template Customization**: Used to create new compliant scripts

### **Using the Build System**
```bash
# Create new script from template
python tools/utilities/build_scripts.py create "My New Tool" materials

# Update all scripts
python tools/utilities/build_scripts.py build

# Windows batch file
build_scripts.bat create "My New Tool" materials
```
