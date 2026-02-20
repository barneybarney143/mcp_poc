# MCP Calculator Server - VSCode Setup Guide

This project contains a simple Model Context Protocol (MCP) server that provides an `add_numbers` tool.

## Prerequisites
- Python 3.10+
- A compatible VSCode extension (e.g., [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline) or [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev))

## Quick Setup

### 1. Initialize Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure VSCode Extension
This project includes a local `mcp_config.json` that is configured to use the local `venv`. 

If your VSCode extension (like Roo Code or Cline) supports workspace-level MCP settings, it will automatically detect the server. Otherwise, you can point your global settings to the local `venv` path:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "/ABSOLUTE/PATH/TO/mcp_poc/venv/bin/python3",
      "args": ["/ABSOLUTE/PATH/TO/mcp_poc/mcp_server.py"]
    }
  }
}
```

## Repository-level Configuration
We have included a template configuration file at `mcp_config.template.json`. You can copy this and adjust the paths for your local machine.

## How to Test
Run the included test script to ensure the server is working correctly:
```bash
python3 test_server.py
```
