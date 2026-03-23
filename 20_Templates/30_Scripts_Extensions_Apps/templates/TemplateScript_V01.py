#!/usr/bin/env python3

"""
Enhanced Script Template v1.0.0
Template tool for USD/Omniverse development

ENVIRONMENT: HYBRID
TAGS: templates, script_template, development_tools, hybrid, beginner, python_standard, safe_execution, log_output, best_practices

PURPOSE: Provides a standardized template for creating new USD/Omniverse scripts
INPUT: None (template for creating new scripts)
OUTPUT: New scripts with proper structure and best practices
USE CASE: When you need to create a new script following best practices

This template helps you:
1. Set up proper script structure
2. Use the unified configuration system
3. Handle errors and logging correctly
4. Follow USD development best practices
5. Create well-documented code

Think of it like a "script starter kit" that:
- Gives you the right foundation
- Sets up all the necessary parts
- Shows you best practices
- Makes it easy to get started
- Helps you write good code

Part of the General_Scripts_Extensions_Apps unified tool framework.
© 2025 - MIT License
"""

import os
import sys
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# USD imports (with error handling)
try:
    from pxr import Usd, UsdGeom, UsdShade, Sdf, Gf
    USD_AVAILABLE = True
except ImportError:
    USD_AVAILABLE = False
    print("Warning: USD Python bindings not available")

# Local imports
try:
    from ..config.base_config import BaseConfig
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    print("Warning: Configuration system not available")

# ============================================================================
# SCRIPT METADATA
# ============================================================================
# Created time: January 15, 2025 02:30 PM
# Last edited time: January 15, 2025 02:30 PM
# Script category: template
# Version: 1.0.0

# ============================================================================
# CUSTOMIZE THESE SETTINGS
# ============================================================================

# Basic configuration
SCRIPT_NAME = "Enhanced Script Template"
SCRIPT_VERSION = "1.0.0"
SCRIPT_CATEGORY = "template"

# Operation settings
ROOT_DIRECTORY = r"C:\path\to\usd\files"
FILE_PATTERN = "*.usd"
DRY_RUN = True  # Set to False for actual execution
LOG_LEVEL = "medium"  # none, medium, high

# ============================================================================
# DERIVED SETTINGS (DO NOT MODIFY)
# ============================================================================

# Output and logging
OUTPUT_DIR = os.path.join(os.getcwd(), "output")
LOG_DIR = os.path.join(OUTPUT_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, f"{SCRIPT_NAME.lower().replace(' ', '_')}.log")

# Validation
VALID_LOG_LEVELS = ["none", "medium", "high"]
VALID_CATEGORIES = ["materials", "variants", "debugging", "analysis", "utilities", "templates"]

# ============================================================================
# ENHANCED SCRIPT TEMPLATE CLASS
# ============================================================================

class EnhancedScriptTemplate:
    """
    Enhanced script template for creating well-structured USD/Omniverse scripts
    
    This class provides a foundation for building new scripts. Think of it
    like a "script starter kit" that gives you:
    1. Configuration management (like settings control)
    2. Proper logging (like keeping track of what happens)
    3. Error handling (like dealing with problems safely)
    4. Best practices (like doing things the right way)
    
    The template includes:
    - Configuration system integration
    - Standardized logging setup
    - Error handling patterns
    - Performance tracking
    - Status reporting
    
    It helps you by:
    - Setting up the basic structure
    - Handling common tasks
    - Following best practices
    - Making logging easy
    - Tracking execution
    
    This is particularly useful when:
    - Starting a new script
    - Learning best practices
    - Need proper error handling
    - Want good logging setup
    
    Example:
        # Create a new script
        class MyScript(EnhancedScriptTemplate):
            def _execute_operations(self):
                # Your code here
                return {'success': True}
        
        script = MyScript()
        result = script.execute_script()
    
    Note:
        This template follows all best practices:
        - Uses the unified configuration system
        - Implements proper logging
        - Handles errors correctly
        - Tracks performance
        - Reports status clearly
    """
    
    def __init__(self, config: Optional[BaseConfig] = None):
        """
        Initialize the enhanced script template
        
        This function sets up the script with everything it needs.
        Think of it like preparing your workspace before starting:
        - Setting up the script name and version
        - Configuring how detailed the logging should be
        - Preparing the output directories
        - Setting up error tracking
        
        Args:
            config (BaseConfig, optional): Configuration settings for the script.
                                         If not provided, uses default settings
                                         from the script.
        
        Example:
            # Create script with default settings
            script = EnhancedScriptTemplate()
            
            # Or create one with custom settings
            config = BaseConfig()
            config.LOG_LEVEL = "high"
            script = EnhancedScriptTemplate(config)
        
        Note:
            The initialization process:
            - Sets up script metadata
            - Configures logging system
            - Prepares execution tracking
            - Creates output directories
        """
        self.script_name = SCRIPT_NAME
        self.script_version = SCRIPT_VERSION
        self.script_category = SCRIPT_CATEGORY
        
        # Configuration setup
        if config and CONFIG_AVAILABLE:
            self.config = config
        else:
            self.config = self._create_fallback_config()
        
        # Setup logging
        self._setup_logging()
        
        # Execution tracking
        self.start_time = None
        self.end_time = None
        self.execution_stats = {
            'operations_completed': 0,
            'errors_encountered': 0,
            'warnings_generated': 0
        }
    
    def _create_fallback_config(self) -> Any:
        """Create a fallback configuration if BaseConfig is not available."""
        class FallbackConfig:
            def __init__(self):
                self.ROOT_DIRECTORY = ROOT_DIRECTORY
                self.FILE_PATTERN = FILE_PATTERN
                self.DRY_RUN = DRY_RUN
                self.LOG_LEVEL = LOG_LEVEL
                self.OUTPUT_DIR = OUTPUT_DIR
            
            def print_script_start(self):
                print(f"Starting {SCRIPT_NAME} v{SCRIPT_VERSION}")
                print(f"Configuration: {self.__dict__}")
            
            def print_script_end(self):
                print(f"Completed {SCRIPT_NAME} v{SCRIPT_VERSION}")
        
        return FallbackConfig()
    
    def _setup_logging(self):
        """Setup logging system."""
        # Create output directories
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        os.makedirs(LOG_DIR, exist_ok=True)
        
        # Configure logging
        if self.config.LOG_LEVEL == "none":
            logging.basicConfig(level=logging.CRITICAL)
        elif self.config.LOG_LEVEL == "medium":
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(LOG_FILE),
                    logging.StreamHandler(sys.stdout)
                ]
            )
        else:  # high
        logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(LOG_FILE),
                    logging.StreamHandler(sys.stdout)
                ]
            )
        
        self.logger = logging.getLogger(self.script_name)
    
    def log_info(self, message: str):
        """Log informational message."""
        self.logger.info(message)
        if self.config.LOG_LEVEL != "none":
            print(f"INFO: {message}")
    
    def log_warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)
        if self.config.LOG_LEVEL != "none":
            print(f"WARNING: {message}")
    
    def log_error(self, message: str):
        """Log error message."""
        self.logger.error(message)
        if self.config.LOG_LEVEL != "none":
            print(f"ERROR: {message}")
    
    def log_debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)
        if self.config.LOG_LEVEL == "high":
            print(f"DEBUG: {message}")
    
    def validate_environment(self) -> bool:
        """Validate that the environment is ready for execution."""
        validation_passed = True
        
        # Check USD availability
        if not USD_AVAILABLE:
            self.log_warning("USD Python bindings not available - some features may not work")
            validation_passed = False
        
        # Check configuration
        if not CONFIG_AVAILABLE:
            self.log_warning("Configuration system not available - using fallback config")
            validation_passed = False
        
        # Validate settings
        if self.config.LOG_LEVEL not in VALID_LOG_LEVELS:
            self.log_error(f"Invalid LOG_LEVEL: {self.config.LOG_LEVEL}")
            validation_passed = False
        
        if self.script_category not in VALID_CATEGORIES:
            self.log_warning(f"Unknown script category: {self.script_category}")
        
        # Check paths
        if not os.path.exists(self.config.ROOT_DIRECTORY):
            self.log_warning(f"ROOT_DIRECTORY does not exist: {self.config.ROOT_DIRECTORY}")
        
        return validation_passed
    
    def execute_script(self) -> Dict[str, Any]:
        """
        Main execution method that runs the script safely
        
        This is the main function that coordinates script execution.
        Think of it like a project manager that:
        1. Makes sure everything is ready
        2. Runs the operations safely
        3. Tracks what happens
        4. Reports the results
        
    Returns:
            Dict[str, Any]: A report containing:
                - operation: What was done
                - success: Whether it worked
                - message/error: Result or error message
                - items_processed: How many items were handled
                - execution_time: How long it took
        
        Example:
            # Run the script
            script = MyScript()
            result = script.execute_script()
            
            if result["success"]:
                print(f"Processed {result['items_processed']} items")
            else:
                print(f"Error: {result['error']}")
        
        Note:
            This process is safe and organized:
            1. Validates environment first
            2. Tracks execution time
            3. Handles errors properly
            4. Reports results clearly
            5. Logs everything important
        """
        self.start_time = datetime.now()
        
        # REQUIRED: Log script start
        if hasattr(self.config, 'print_script_start'):
            self.config.print_script_start()
        else:
            self.log_info(f"Starting {self.script_name} v{self.script_version}")
        
        # Validate environment
        if not self.validate_environment():
            self.log_error("Environment validation failed")
            return self._create_error_result("Environment validation failed")
        
        try:
            # Execute main operations
            result = self._execute_operations()
            
            # Update execution stats
            self.execution_stats['operations_completed'] += 1
            
            return result
            
        except Exception as e:
            self.log_error(f"Script execution failed: {str(e)}")
            self.execution_stats['errors_encountered'] += 1
            return self._create_error_result(str(e))
        
        finally:
            self.end_time = datetime.now()
            self._log_execution_summary()
    
    def _execute_operations(self) -> Dict[str, Any]:
        """
        Execute the main script operations (override in subclasses)
        
        This is where you put your script's main work. Think of it
        like the "worker" function that actually does the job:
        1. Gets the work that needs to be done
        2. Does the work carefully
        3. Keeps track of progress
        4. Returns the results
        
        Returns:
            Dict[str, Any]: A report containing:
                - operation: What was done
                - success: Whether it worked
                - message: What happened
                - items_processed: How many items handled
                - execution_time: How long it took
        
        Example:
            def _execute_operations(self):
                # Do your work here
                items = self.find_items_to_process()
                for item in items:
                    self.process_item(item)
                
                return {
                    'operation': 'Process Items',
                    'success': True,
                    'message': 'All items processed',
                    'items_processed': len(items),
                    'execution_time': '1.5s'
                }
        
        Note:
            This is a template - you should override this in your script:
            1. Replace this with your actual work
            2. Keep track of what you process
            3. Handle errors properly
            4. Return results in the same format
        """
        # This is a template - subclasses should implement their operations
        self.log_info("Template script - no operations implemented")
        
        return {
            'operation': 'Template Execution',
            'success': True,
            'message': 'Template script executed successfully',
            'items_processed': 0,
            'execution_time': '0.0s'
        }
    
    def _create_error_result(self, error_message: str) -> Dict[str, Any]:
        """Create a standardized error result."""
        return {
            'operation': self.script_name,
            'success': False,
            'error': error_message,
            'items_processed': 0,
            'execution_time': '0.0s'
        }
    
    def _log_execution_summary(self):
        """Log execution summary and statistics."""
        if self.start_time and self.end_time:
            execution_time = (self.end_time - self.start_time).total_seconds()
            
            self.log_info("=" * 50)
            self.log_info("EXECUTION SUMMARY")
            self.log_info("=" * 50)
            self.log_info(f"Script: {self.script_name} v{self.script_version}")
            self.log_info(f"Category: {self.script_category}")
            self.log_info(f"Start time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            self.log_info(f"End time: {self.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            self.log_info(f"Execution time: {execution_time:.2f} seconds")
            self.log_info(f"Operations completed: {self.execution_stats['operations_completed']}")
            self.log_info(f"Errors encountered: {self.execution_stats['errors_encountered']}")
            self.log_info(f"Warnings generated: {self.execution_stats['warnings_generated']}")
            self.log_info("=" * 50)
        
        # REQUIRED: Log script end
        if hasattr(self.config, 'print_script_end'):
            self.config.print_script_end()
        else:
            self.log_info(f"Completed {self.script_name} v{self.script_version}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function for standalone execution."""
    print(f"Running {SCRIPT_NAME} v{SCRIPT_VERSION}")
    print(f"Category: {SCRIPT_CATEGORY}")
    print(f"Dry run mode: {DRY_RUN}")
    print(f"Log level: {LOG_LEVEL}")
    print("-" * 50)
    
    # Create and execute script
    script = EnhancedScriptTemplate()
    result = script.execute_script()
    
    # Display result
    print("\n" + "=" * 50)
    print("EXECUTION RESULT")
    print("=" * 50)
    for key, value in result.items():
        print(f"{key}: {value}")
    
    return result

if __name__ == "__main__":
    main()