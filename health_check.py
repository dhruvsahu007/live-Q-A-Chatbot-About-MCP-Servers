import os
from mcp_chatbot import MCPKnowledgeBase

def health_check():
    """Simple health check for the application"""
    try:
        # Check if knowledge base loads
        kb = MCPKnowledgeBase()
        if not kb.knowledge_data:
            return False, "Knowledge base failed to load"
        
        # Check if environment variables are set
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "your_openai_api_key_here":
            return False, "OpenAI API key not configured"
        
        return True, "All systems operational"
    
    except Exception as e:
        return False, f"Health check failed: {str(e)}"

if __name__ == "__main__":
    success, message = health_check()
    print(f"Health Check: {'PASS' if success else 'FAIL'} - {message}")
    exit(0 if success else 1)
