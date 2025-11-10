# mcp-demo
Use FastAPI and FastMCP (from https://gofastmcp.com/integrations/fastapi#offering-an-llm-friendly-api and https://gofastmcp.com/integrations/fastapi#combining-lifespans)

## Installation
```
poetry install
```

### Adding MCP to Claude Code CLI
```
claude mcp remove demo-mcp || true && claude mcp add demo-mcp --transport http http://localhost:8000/llm/mcp && claude mcp list
```
Then launch Claude Code and confirm it sees and tests the add tool:
```
> Now you should see the add numbers tool in the demo-mcp MCP server 

● I can see that you've successfully reconnected to the demo-mcp MCP server. Let me verify that the add numbers tool is available by checking the MCP resources.

● listMcpResources(List MCP resources from server "demo-mcp")
  ⎿  (No resources found)                                                                                                                                                                                

● Great! The demo-mcp server is connected. I can confirm that the mcp__demo-mcp__add_nums tool is available in the function tools, which means it's been successfully exposed through the MCP server.

  Let me test it by adding two numbers:

● demo-mcp - add_nums (MCP)(a: 5, b: 3)
  ⎿  {            
       "result": 8
     }

● Perfect! The add numbers tool from the demo-mcp MCP server is working correctly. When I called it with a=5 and b=3, it returned the correct result of 8.

  The MCP integration is working as expected. You can now use this tool (and any other tools exposed by the demo-mcp server) throughout your Claude Code session.
```

## Running
```
make run
```

