# Example MCP Server Code Snippets

## Basic MCP Server (Python)

```python
import asyncio
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

# Initialize MCP server
server = FastMCP("Example MCP Server")

@server.resource("users/{user_id}")
async def get_user(user_id: str) -> str:
    """Get user information by ID"""
    # Simulate database lookup
    users = {
        "1": {"name": "Alice", "email": "alice@example.com"},
        "2": {"name": "Bob", "email": "bob@example.com"}
    }
    user = users.get(user_id, {})
    return f"User: {user.get('name', 'Unknown')} ({user.get('email', 'No email')})"

@server.tool("calculate")
async def calculate(expression: str) -> Dict[str, Any]:
    """Calculate mathematical expressions"""
    try:
        result = eval(expression)  # Note: Use safely in production
        return {
            "expression": expression,
            "result": result,
            "success": True
        }
    except Exception as e:
        return {
            "expression": expression,
            "error": str(e),
            "success": False
        }

@server.prompt("greeting")
async def greeting_prompt(name: str = "User") -> str:
    """Generate a personalized greeting"""
    return f"Hello {name}! How can I help you today?"

if __name__ == "__main__":
    server.run()
```

## MCP Server with Database Integration

```python
import sqlite3
from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any

server = FastMCP("Database MCP Server")

# Initialize database
def init_db():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

@server.tool("query_products")
async def query_products(category: str = None) -> List[Dict[str, Any]]:
    """Query products from database"""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    
    if category:
        cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    else:
        cursor.execute("SELECT * FROM products")
    
    products = []
    for row in cursor.fetchall():
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "category": row[3]
        })
    
    conn.close()
    return products

@server.tool("add_product")
async def add_product(name: str, price: float, category: str) -> Dict[str, Any]:
    """Add a new product to database"""
    try:
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
            (name, price, category)
        )
        conn.commit()
        product_id = cursor.lastrowid
        conn.close()
        
        return {
            "success": True,
            "id": product_id,
            "message": f"Product '{name}' added successfully"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    init_db()
    server.run()
```

## MCP Client Example

```python
from mcp.client import create_client, StdioClientTransport
import asyncio

async def main():
    # Connect to MCP server
    transport = StdioClientTransport("python", ["server.py"])
    
    async with create_client(transport) as client:
        # List available resources
        resources = await client.list_resources()
        print("Available resources:", resources)
        
        # Call a tool
        result = await client.call_tool("calculate", {"expression": "2 + 2"})
        print("Calculation result:", result)
        
        # Get a resource
        user_data = await client.read_resource("users/1")
        print("User data:", user_data)

if __name__ == "__main__":
    asyncio.run(main())
```

## Configuration Examples

### server_config.json
```json
{
  "name": "My MCP Server",
  "version": "1.0.0",
  "description": "Example MCP server with multiple capabilities",
  "transport": {
    "type": "stdio"
  },
  "capabilities": {
    "resources": true,
    "tools": true,
    "prompts": true
  },
  "security": {
    "require_auth": false,
    "allowed_origins": ["*"]
  }
}
```

### Client Configuration
```json
{
  "servers": {
    "example-server": {
      "command": "python",
      "args": ["server.py"],
      "env": {
        "DATABASE_URL": "sqlite:///example.db"
      }
    }
  }
}
```
