from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("CalculatorServer")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two integers together.

    Args:
        a: The first integer.
        b: The second integer.
    """
    return a + b


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
