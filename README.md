# MCP Q&A Chatbot

A comprehensive Q&A chatbot that specializes in answering questions about the Model Context Protocol (MCP). This chatbot helps developers understand MCP concepts, implementation, best practices, and troubleshooting.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI GPT-3.5-turbo for intelligent answers
- 📚 **Comprehensive Knowledge Base**: Covers MCP concepts, implementation patterns, and common issues
- 🔍 **Semantic Search**: Finds relevant information using sentence embeddings
- 💬 **Interactive UI**: Clean and user-friendly Streamlit interface
- 🎯 **Suggested Questions**: Pre-built questions to help users get started
- 📱 **Responsive Design**: Works well on different screen sizes

## What the Chatbot Covers

### Core MCP Concepts
- Model Context Protocol overview and architecture
- Client-server communication patterns
- Transport layers (stdio, HTTP, WebSocket)
- Protocol implementation details

### MCP Capabilities
- Resources: Static and dynamic data access
- Tools: Function calling and action execution
- Prompts: Reusable prompt templates
- Sampling: LLM completion requests

### Implementation Guidance
- Step-by-step development guide
- Best practices and design patterns
- Security considerations
- Performance optimization

### Troubleshooting
- Common issues and solutions
- Debugging techniques
- Connection problems
- Protocol errors

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "D:\Desktop\Masai\W4D1\Q&A-Chatbot-About-MCP-Servers"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and go to `http://localhost:8501`

## Usage

### Getting Started
1. Open the application in your web browser
2. Use the suggested questions to explore MCP topics
3. Type your own questions in the chat input
4. Get detailed, contextual answers about MCP

### Example Questions
- "What is the Model Context Protocol?"
- "How do I create my first MCP server?"
- "What are the security considerations for MCP?"
- "How do I implement tools in an MCP server?"
- "What's the difference between resources and tools?"

### Features Overview
- **Chat Interface**: Main conversation area with message history
- **Suggested Questions**: Quick-start questions on the right sidebar
- **Knowledge Base**: Comprehensive MCP information automatically referenced
- **Semantic Search**: Finds relevant context for each question
- **Clear Chat**: Reset conversation history

## Project Structure

```
Q&A-Chatbot-About-MCP-Servers/
│
├── app.py                 # Main Streamlit application
├── mcp_chatbot.py        # Chatbot logic and knowledge base handler
├── knowledge_base.json   # Comprehensive MCP knowledge base
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .env                 # Your actual environment variables (create this)
├── Procfile              # Render deployment configuration
├── runtime.txt           # Python version for deployment
├── .streamlit/           # Streamlit configuration for deployment
│   └── config.toml
├── DEPLOYMENT.md         # Detailed deployment guide
└── README.md           # This file
```

## Deployment

### Deploy to Render (Recommended)

This application is ready for deployment on Render. See [`DEPLOYMENT.md`](DEPLOYMENT.md) for detailed instructions.

**Quick Deploy Steps:**
1. Push your code to GitHub
2. Connect your GitHub repo to Render
3. Set environment variables (especially `OPENAI_API_KEY`)
4. Deploy!

**Live Demo**: Once deployed, your app will be available at a URL like `https://your-app-name.onrender.com`

### Local Development
For local development, follow the installation instructions above.

## Technical Details

### Architecture
- **Frontend**: Streamlit web interface
- **Backend**: OpenAI GPT-3.5-turbo API
- **Knowledge Base**: JSON-based with keyword search
- **Deployment**: Ready for Render cloud hosting
- **Search**: Intelligent keyword matching for context retrieval

### Key Components

1. **MCPKnowledgeBase Class**
   - Loads and manages MCP knowledge
   - Performs intelligent keyword search
   - Finds relevant context for questions

2. **MCPChatbot Class**
   - Handles OpenAI API interactions
   - Formats context and generates responses
   - Manages conversation history

3. **Streamlit Interface**
   - User-friendly chat interface
   - Suggested questions sidebar
   - Configuration status display

### Knowledge Base Topics
- MCP Overview and Architecture
- Capabilities (Resources, Tools, Prompts, Sampling)
- Implementation Patterns
- Security Best Practices
- Common Use Cases
- Troubleshooting Guide
- Development Guide
- Protocol Details
- Ecosystem and Tools

## Configuration

### Environment Variables
```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=1000
TEMPERATURE=0.7
```

### Customization
- **Knowledge Base**: Edit `knowledge_base.json` to add more MCP information
- **UI Styling**: Modify CSS in `app.py` for custom appearance
- **Model Settings**: Adjust temperature, max_tokens in `.env` file
- **Suggested Questions**: Update the list in `mcp_chatbot.py`

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your OpenAI API key is correctly set in `.env`
   - Check that the key has sufficient credits

2. **Module Import Error**
   - Install all requirements: `pip install -r requirements.txt`
   - Ensure you're in the correct virtual environment

3. **Streamlit Not Starting**
   - Check if port 8501 is available
   - Try running with different port: `streamlit run app.py --server.port 8502`

4. **Knowledge Base Not Loading**
   - Ensure `knowledge_base.json` exists in the project directory
   - Check JSON syntax if you've modified the file

## Contributing

Feel free to enhance the chatbot by:
- Adding more MCP knowledge to the knowledge base
- Improving the UI/UX design
- Adding new features like conversation export
- Optimizing search and response quality

## License

This project is for educational purposes as part of the Masai curriculum.

## Acknowledgments

- Model Context Protocol documentation and community
- OpenAI for the GPT-3.5-turbo API
- Streamlit for the web framework
- Sentence Transformers for semantic search capabilities
