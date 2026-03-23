---
arys_schema_version: '1.2'
id: 84dbe53d-bc5e-4e00-915d-2cd9be55337d
title: Project Templates
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T18:15:20Z'
last_modified: '2026-02-18T18:15:20Z'
---

# Project Templates

**Version**: 1.1.0 | **Date**: 18.02.2026 | **Time**: 21:25 | **GlobalID**: 20260218_2125_General_Scripts_Extensions_Apps_Templates

**Tag block:**
#best_practices #automation #framework_integration #openusd #usd_core #omniverse #export #workflow_automation #extension_development

This directory contains reusable templates and foundations for USD/Omniverse development projects.

## Available Templates

### 1. Plugin Project Structure Template (canonical, deterministic)

**Purpose**: Canonical, folder-based template for new plugin projects (Blender addons, Rhino plugins, etc.), designed to eliminate ambiguity and drift.

**Features**:
- **Validated Structure**: Tested across 3 repositories (C4D_USD_MultiExport, Blender_USD_MultiExport, Rhino_USD_MultiExport)
- **Consistent Documentation**: Numbered documentation files with clear separation of concerns
- **Non-Programmer Friendly**: Detailed build instructions that explain technical concepts
- **Professional Organization**: Clear folder structure and documentation hierarchy
- **Deterministic Bootstrap Script**: One command creates a new repo skeleton from templates
- **Common + Platform Overlays**: Avoids maintaining duplicated template trees

**Use When**: Creating a new plugin project (Blender addon, Rhino plugin, etc.)

**Canonical location**:
- `030_Proj_TEMPLATES/010_plugin_project_structure_template/`
  - `TEMPLATE_Plugin_Project_Common/`
  - `platforms/Blender/`
  - `platforms/Rhino/`

**Bootstrap script (deterministic)**:
- `040_Proj_TOOLS/utilities/bootstrap_plugin_project.py`

**Quickstart guide**:
- `010_Proj_GUIDES/G008_Plugin_Project_Bootstrap_GUIDE.md` - Step-by-step bootstrap instructions

**Reference doc (overview only)**:
- `030_Proj_TEMPLATES/010_plugin_project_structure_template/plugin_project_structure_template.md`

### 2. Enhanced Script Template (`templates/TemplateScript_V01.py`)

**Purpose**: Compliant foundation for USD/Omniverse Python development scripts.

**Features**:
- **Configuration Rules Compliant**: Meets all script configuration requirements
- **Unified Configuration System**: Integrates with General_Scripts_Extensions_Apps configuration framework
- **Standardized Logging**: Consistent logging patterns across all tools
- **USD Environment Validation**: Automatic validation of USD dependencies
- **Modular Operation Structure**: Easy to add new operations and functionality

**Use When**: Creating a new Python script for USD/Omniverse development.

**See**: [`templates/README.md`](templates/README.md) for detailed documentation.

### 3. Requirements Generation Template (`requirements_generation_template.md`)

**Purpose**: Comprehensive template for documenting project requirements based on research and discovery findings.

**Features**:
- **Research Synthesis**: Integrates discovery phase inputs and research findings
- **Structured Requirements**: Functional, non-functional, UI/UX, and integration requirements
- **Testability Assessment**: Built-in testability verification for each requirement
- **Traceability Matrix**: Links requirements to sources, test cases, and priorities
- **Validation Framework**: Completeness, consistency, and testability checks
- **Change Management**: Version control and change request process
- **Event Tracking**: Event ID system for requirements lifecycle management

**Key Sections**:
- Executive Summary
- Research Synthesis (Discovery & Research Phase Inputs)
- Requirements Categories:
  - Functional Requirements (REQ-001, REQ-002...)
  - Non-Functional Requirements (NFR-001, NFR-002...)
  - UI/UX Requirements (UX-001, UX-002...)
  - Integration Requirements (INT-001, INT-002...)
- Requirements Traceability Matrix
- Requirements Analysis (Completeness, Consistency, Testability)
- Validation & Approval Process
- Change Management

**Use When**: 
- Starting a new project after completing discovery/research phases
- Need to document requirements systematically
- Want to ensure testability and traceability
- Need stakeholder approval for requirements

**See**: [`requirements_generation_template.md`](requirements_generation_template.md) for complete template structure.

**Related Guide**: `010_Proj_GUIDES/G006_Requirements_Generation_GUIDE.md` for detailed guidance on requirements generation process.

### 4. Implementation Plan Template (`implementation_plan_template.md`)

**Purpose**: Comprehensive template for planning and tracking project implementation phases.

**Features**:
- **Phase-Based Planning**: Structured implementation phases with clear objectives
- **MVP Definition**: Clear MVP scope and acceptance criteria
- **Task Tracking**: Detailed tasks with time estimates and priorities
- **Quality Gates**: Defined checkpoints for each phase
- **Risk Management**: Risk assessment and mitigation strategies
- **Resource Planning**: Team, tools, and infrastructure requirements
- **Success Metrics**: Measurable project and quality metrics
- **Change Management**: Scope change criteria and change request process

**Key Sections**:
- Executive Summary
- Current System Analysis
- Requirements Summary
- MVP Definition
- Implementation Phases (with deliverables, tasks, quality gates)
- Timeline & Milestones
- Risk Assessment & Mitigation
- Resource Requirements
- Quality Assurance Plan
- Success Metrics
- Communication Plan
- Change Management
- Implementation Checklist

**Use When**:
- Requirements are finalized and approved
- Ready to plan implementation phases
- Need to track progress and manage risks
- Want structured quality gates and milestones

**See**: [`implementation_plan_template.md`](implementation_plan_template.md) for complete template structure.

**Related Guide**: `010_Proj_GUIDES/G007_Implementation_Planning_GUIDE.md` for detailed guidance on creating implementation plans.

---

## Quick Start

### Creating a New Plugin Project

1. **Bootstrap deterministically (recommended)**:

```bash
python 040_Proj_TOOLS/utilities/bootstrap_plugin_project.py --platform blender --dest "PATH_TO_NEW_REPO"
```

or

```bash
python 040_Proj_TOOLS/utilities/bootstrap_plugin_project.py --platform rhino --dest "PATH_TO_NEW_REPO"
```

2. **Replace placeholders**:
   - Search/replace all `[REPLACE_ME:...]` placeholders.

3. **Reference examples**:
   - `C4D_USD_MultiExport`
   - `Blender_USD_MultiExport`
   - `Rhino_USD_MultiExport`

### Creating Requirements Documentation

1. **Copy the requirements template**:
   ```bash
   cp 030_Proj_TEMPLATES/requirements_generation_template.md 02_Detailed_Requirements.md
   ```

2. **Fill in the template**:
   - Add project name and event ID
   - Synthesize research and discovery findings
   - Document functional requirements with acceptance criteria
   - Document non-functional requirements (performance, security, scalability, usability)
   - Add UI/UX requirements
   - Document integration requirements
   - Complete traceability matrix
   - Run completeness, consistency, and testability checks

3. **Validate and approve**:
   - Internal technical review
   - Stakeholder review
   - Approval sign-off
   - Version control

**See**: `010_Proj_GUIDES/G006_Requirements_Generation_GUIDE.md` for detailed guidance.

### Creating an Implementation Plan

1. **Copy the implementation plan template**:
   ```bash
   cp 030_Proj_TEMPLATES/implementation_plan_template.md 04_Implementation_Plan.md
   ```

2. **Fill in the template**:
   - Add project name and event ID
   - Summarize requirements (reference requirements document)
   - Define MVP scope and acceptance criteria
   - Break down into implementation phases
   - Add tasks with time estimates and priorities
   - Define quality gates for each phase
   - Assess risks and mitigation strategies
   - Plan resources and timeline
   - Define success metrics

3. **Track progress**:
   - Use implementation checklist
   - Monitor milestones
   - Update risk assessments
   - Manage change requests

**See**: `010_Proj_GUIDES/G007_Implementation_Planning_GUIDE.md` for detailed guidance.

### Creating a New Script

1. **Copy the script template**:
   ```bash
   cp templates/TemplateScript_V01.py my_new_script.py
   ```

2. **Customize the template**:
   - Update script metadata (name, version, category)
   - Implement `_execute_operations()` method
   - Add custom configuration if needed

3. **Follow best practices**:
   - Use structured results
   - Implement proper error handling
   - Use logging methods consistently
   - Validate environment before operations

---

## Template Guidelines

### When to Use Each Template

**Plugin Project Structure Template**:
- Creating a new plugin project (Blender addon, Rhino plugin, etc.)
- Need to establish consistent project structure
- Want to follow validated best practices

**Requirements Generation Template**:
- Completed discovery/research phases
- Ready to document requirements systematically
- Need stakeholder approval for requirements
- Want to ensure testability and traceability

**Implementation Plan Template**:
- Requirements are finalized and approved
- Ready to plan implementation phases
- Need to track progress and manage risks
- Want structured quality gates and milestones

**Script Template**:
- Creating a new Python script for USD/Omniverse development
- Need compliant foundation with logging and configuration
- Want standardized patterns and best practices

### Template Customization

All templates are designed to be customized:
- Modify structure to fit your specific needs
- Add project-specific sections
- Remove sections that don't apply
- Extend with additional documentation

### Best Practices

1. **Follow the Structure**: Use the template structure as a starting point
2. **Be Consistent**: Maintain consistency across similar projects
3. **Document Changes**: Note any deviations from the template
4. **Update Templates**: Contribute improvements back to templates

---

## Contributing

When contributing new templates or improvements:

1. **Follow the established pattern** in existing templates
2. **Include comprehensive documentation** and examples
3. **Test with real projects** before adding to templates
4. **Update this README** with new template information
5. **Provide usage examples** and quick start guides

---

## Template Workflow

### Complete Project Lifecycle

1. **Discovery/Research Phase** (outside templates)
   - Conduct research and discovery
   - Document findings

2. **Requirements Phase** → Use `requirements_generation_template.md`
   - Synthesize research findings
   - Document functional and non-functional requirements
   - Create traceability matrix
   - Get stakeholder approval

3. **Planning Phase** → Use `implementation_plan_template.md`
   - Define MVP scope
   - Break down into phases
   - Plan resources and timeline
   - Assess risks

4. **Project Setup** → Use the folder-based plugin template + bootstrap script
   - Create project structure
   - Set up documentation
   - Configure build scripts

5. **Development Phase** → Use `templates/TemplateScript_V01.py`
   - Implement features
   - Follow coding standards
   - Write tests

### Template Dependencies

```
Research/Discovery
    ↓
Requirements Template (02_Detailed_Requirements.md)
    ↓
Implementation Plan Template (04_Implementation_Plan.md)
    ↓
Plugin Project Structure Template (Project Setup: folder-based + bootstrap script)
    ↓
Script Template (Development)
```

## Related Resources

- **Examples**: See `070_Proj_EXAMPLES/` for example implementations
- **Guides**: 
  - `010_Proj_GUIDES/G006_Requirements_Generation_GUIDE.md` - Requirements generation process
  - `010_Proj_GUIDES/G007_Implementation_Planning_GUIDE.md` - Implementation planning process
  - `010_Proj_GUIDES/G008_Plugin_Project_Bootstrap_GUIDE.md` - Plugin project bootstrap (deterministic)
- **Best Practices**: See `090_Proj_BEST_PRACTICES/` for best practices
- **Real-World Examples**:
  - Plugin Projects: `C4D_USD_MultiExport`, `Blender_USD_MultiExport`, `Rhino_USD_MultiExport`

---

**Version**: 1.1.0  
**Last Updated**: 18.02.2026
