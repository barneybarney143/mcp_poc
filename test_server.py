import subprocess
import json


def test_add():
    # Construct the initialize request
    init_request = {
        "jsonrpc": "2.0",
        "method": "initialize",
        "id": 1,
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0.0"},
        },
    }

    # Construct the tool call request
    call_request = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 2,
        "params": {"name": "add_numbers", "arguments": {"a": 10, "b": 20}},
    }

    # Run the server and pipe the inputs
    process = subprocess.Popen(
        ["python3", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Send requests separated by newlines (standard for stdio MCP)
    input_data = json.dumps(init_request) + "\n" + json.dumps(call_request) + "\n"
    stdout, stderr = process.communicate(input=input_data)

    print("STDOUT output:")
    for line in stdout.splitlines():
        try:
            msg = json.loads(line)
            if "result" in msg:
                print(f"Server response: {json.dumps(msg, indent=2)}")
        except:
            continue


if __name__ == "__main__":
    test_add()
