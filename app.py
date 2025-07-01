import streamlit as st
import os
from mcp_chatbot import MCPChatbot
import time

# Page configuration
st.set_page_config(
    page_title="MCP Expert Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple CSS for better visibility
st.markdown("""
<style>
    .main-title {
        color: #1e88e5;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .subtitle {
        color: #424242;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_chatbot():
    """Initialize the chatbot with error handling"""
    try:
        return MCPChatbot()
    except Exception as e:
        st.error(f"Failed to initialize chatbot: {str(e)}")
        st.error("Please check your OpenAI API key in the .env file")
        return None

def display_message(message, is_user=False):
    """Display a chat message with proper styling"""
    message_class = "user-message" if is_user else "bot-message"
    icon = "👤" if is_user else "🤖"
    role_name = "You" if is_user else "MCP Expert"
    
    # Escape HTML content and preserve line breaks
    safe_message = message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
    
    st.markdown(f"""
    <div class="chat-message {message_class}">
        <strong style="color: inherit;">{icon} {role_name}:</strong><br>
        <div style="margin-top: 0.5rem; color: inherit;">{safe_message}</div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-title">🤖 MCP Expert Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your AI assistant for Model Context Protocol questions</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📚 About MCP")
        st.markdown("""
        The **Model Context Protocol (MCP)** is an open standard that enables 
        secure connections between AI assistants and external data sources.
        
        **Key Features:**
        - 🔗 Connect AI to real-time data
        - 🔐 Secure and controlled access
        - 🛠️ Extensible architecture
        - 🌐 Multiple transport options
        """)
        
        st.header("🎯 What I can help with:")
        st.markdown("""
        - **Concepts**: Understanding MCP fundamentals
        - **Implementation**: Building MCP servers
        - **Best Practices**: Security and optimization
        - **Troubleshooting**: Common issues and solutions
        - **Examples**: Code snippets and patterns
        """)
        
        # API Key status
        st.header("⚙️ Configuration")
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and api_key != "your_openai_api_key_here" and len(api_key) > 20:
            st.success("✅ OpenAI API Key configured")
        else:
            st.error("❌ OpenAI API Key not configured")
            if os.path.exists(".env"):
                st.info("Please set your API key in the .env file")
            else:
                st.info("Set OPENAI_API_KEY as an environment variable")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = initialize_chatbot()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Chat Interface")
        
        # Display chat history
        chat_container = st.container()
        with chat_container:
            if not st.session_state.messages:
                st.info("👋 Welcome! Ask me anything about the Model Context Protocol (MCP).")
            
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
        
        # Chat input
        user_input = st.text_input(
            "💬 Ask me anything about MCP:",
            placeholder="e.g., How do I create an MCP server?",
            key="user_input"
        )
        
        col1_1, col1_2, col1_3 = st.columns([1, 1, 3])
        with col1_1:
            send_button = st.button("Send 📤", type="primary")
        with col1_2:
            clear_button = st.button("Clear 🗑️")
        
        # Handle suggested questions
        selected_question = None
    
    with col2:
        st.header("💡 Suggested Questions")
        
        if st.session_state.chatbot:
            suggested_questions = st.session_state.chatbot.get_suggested_questions()
            
            for i, question in enumerate(suggested_questions):
                if st.button(
                    question, 
                    key=f"suggestion_{i}",
                    help="Click to ask this question",
                    use_container_width=True
                ):
                    selected_question = question
    
    # Handle user input
    if (send_button and user_input) or selected_question:
        if st.session_state.chatbot is None:
            st.error("Chatbot not initialized. Please check your configuration.")
            return
        
        # Use selected question or user input
        current_question = selected_question if selected_question else user_input
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": current_question})
        
        # Show loading indicator
        with st.spinner("🤔 Thinking..."):
            # Get bot response
            conversation_history = [
                {"role": msg["role"], "content": msg["content"]} 
                for msg in st.session_state.messages[-10:]  # Last 10 messages
            ]
            
            bot_response = st.session_state.chatbot.get_response(
                current_question, 
                conversation_history[:-1]  # Exclude the current message
            )
        
        # Add bot response to history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Clear the input
        if selected_question:
            st.session_state.user_input = ""
        
        # Rerun to update the display
        st.rerun()
    
    # Clear chat history
    if clear_button:
        st.session_state.messages = []
        st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🚀 Built with Streamlit and OpenAI | 
        📖 <a href="https://modelcontextprotocol.io" target="_blank">Learn more about MCP</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
