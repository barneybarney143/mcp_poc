import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run_client():
    # Define server parameters - using the relative path to our venv python
    server_params = StdioServerParameters(
        command="./venv/bin/python3", args=["mcp_server.py"], env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            print("\n--- MCP Standalone Client ---")
            print("Connected to CalculatorServer.")
            print("Type 'exit' or 'quit' to stop.")

            while True:
                user_input = input("\nEnter calculation (e.g., 5 + 10) or 'exit': ")
                if user_input.lower() in ["exit", "quit"]:
                    break

                try:
                    # Simple parsing for demo purposes
                    if "+" in user_input:
                        parts = user_input.split("+")
                        a = int(parts[0].strip())
                        b = int(parts[1].strip())

                        # Call the tool
                        result = await session.call_tool(
                            "add_numbers", arguments={"a": a, "b": b}
                        )

                        # Process results
                        for content in result.content:
                            if content.type == "text":
                                print(f"Result: {content.text}")
                    else:
                        print("Please use the format: number + number")
                except ValueError:
                    print("Error: Please enter valid integers (e.g., 5 + 10)")
                except Exception as e:
                    print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(run_client())
    except KeyboardInterrupt:
        pass
