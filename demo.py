"""
Demo script to showcase MCP Q&A Chatbot capabilities
"""

import os
import json
from mcp_chatbot import MCPChatbot, MCPKnowledgeBase

def demo_knowledge_base():
    """Demonstrate knowledge base search capabilities"""
    print("=" * 60)
    print("📚 KNOWLEDGE BASE DEMO")
    print("=" * 60)
    
    kb = MCPKnowledgeBase()
    
    # Test queries
    test_queries = [
        "What is MCP?",
        "security best practices",
        "how to implement tools",
        "troubleshooting connection issues"
    ]
    
    for query in test_queries:
        print(f"\n🔍 Query: '{query}'")
        results = kb.search_relevant_content(query, top_k=2)
        
        for i, result in enumerate(results, 1):
            print(f"\n📄 Result {i} (Score: {result['similarity_score']:.3f}):")
            print(f"   Title: {result['title']}")
            print(f"   Content: {result['content'][:150]}...")

def demo_chatbot_responses():
    """Demonstrate chatbot response generation"""
    print("\n" + "=" * 60)
    print("🤖 CHATBOT DEMO")
    print("=" * 60)
    
    # Check if API key is configured
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("❌ OpenAI API key not configured. Skipping chatbot demo.")
        print("💡 Set your API key in .env file to test chatbot responses.")
        return
    
    try:
        chatbot = MCPChatbot()
        
        # Test questions
        test_questions = [
            "What is the Model Context Protocol?",
            "How do I create a basic MCP server?",
            "What are the main security considerations for MCP?",
            "Can you explain the difference between MCP resources and tools?"
        ]
        
        for question in test_questions:
            print(f"\n❓ Question: {question}")
            print("🤔 Generating response...")
            
            response = chatbot.get_response(question)
            print(f"🤖 Response: {response[:300]}...")
            print("-" * 40)
    
    except Exception as e:
        print(f"❌ Error testing chatbot: {e}")

def demo_suggested_questions():
    """Show suggested questions"""
    print("\n" + "=" * 60)
    print("💡 SUGGESTED QUESTIONS")
    print("=" * 60)
    
    try:
        # Create a dummy chatbot to get suggestions (doesn't need API key)
        os.environ["OPENAI_API_KEY"] = "dummy"  # Temporary for getting suggestions
        chatbot = MCPChatbot()
        
        suggestions = chatbot.get_suggested_questions()
        
        for i, question in enumerate(suggestions, 1):
            print(f"{i:2d}. {question}")
    
    except Exception as e:
        print(f"Error getting suggestions: {e}")

def show_project_structure():
    """Display project structure"""
    print("\n" + "=" * 60)
    print("📁 PROJECT STRUCTURE")
    print("=" * 60)
    
    files = [
        "app.py - Main Streamlit application",
        "mcp_chatbot.py - Chatbot logic and knowledge base",
        "knowledge_base.json - Comprehensive MCP knowledge",
        "requirements.txt - Python dependencies",
        ".env.example - Environment variables template",
        "README.md - Project documentation",
        "code_examples.md - MCP code snippets",
        "setup.py - Setup and testing script"
    ]
    
    for file_desc in files:
        file_name = file_desc.split(' - ')[0]
        description = file_desc.split(' - ')[1]
        
        if os.path.exists(file_name):
            status = "✅"
        else:
            status = "❌"
        
        print(f"{status} {file_desc}")

def show_usage_instructions():
    """Show how to use the chatbot"""
    print("\n" + "=" * 60)
    print("🚀 USAGE INSTRUCTIONS")
    print("=" * 60)
    
    instructions = [
        "1. Install dependencies: pip install -r requirements.txt",
        "2. Copy .env.example to .env",
        "3. Add your OpenAI API key to .env file",
        "4. Run setup test: python setup.py --test",
        "5. Start the application: streamlit run app.py",
        "6. Open browser to http://localhost:8501",
        "7. Start asking questions about MCP!"
    ]
    
    for instruction in instructions:
        print(f"   {instruction}")

def main():
    """Run the complete demonstration"""
    print("🎯 MCP Q&A CHATBOT DEMONSTRATION")
    print("Built for Masai School - W4D1 Assignment")
    
    # Show project overview
    show_project_structure()
    
    # Show usage instructions
    show_usage_instructions()
    
    # Demo knowledge base
    demo_knowledge_base()
    
    # Show suggested questions
    demo_suggested_questions()
    
    # Demo chatbot (if API key is available)
    demo_chatbot_responses()
    
    print("\n" + "=" * 60)
    print("✨ DEMO COMPLETE")
    print("=" * 60)
    print("💡 To start the interactive chatbot, run: streamlit run app.py")

if __name__ == "__main__":
    main()
