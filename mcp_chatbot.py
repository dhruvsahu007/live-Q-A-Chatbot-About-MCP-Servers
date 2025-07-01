import json
import os
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import re
import numpy as np

# Load environment variables
load_dotenv()

class MCPKnowledgeBase:
    """Knowledge base for MCP-related information"""
    
    def __init__(self, knowledge_file: str = "knowledge_base.json"):
        self.knowledge_file = knowledge_file
        self.knowledge_data = self._load_knowledge()
    
    def _load_knowledge(self) -> Dict[str, Any]:
        """Load knowledge base from JSON file"""
        try:
            with open(self.knowledge_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            st.error(f"Knowledge base file {self.knowledge_file} not found!")
            return {}
    
    def search_relevant_content(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Search for relevant content based on query using keyword matching"""
        if not self.knowledge_data:
            return []
        
        query_lower = query.lower()
        query_words = set(re.findall(r'\w+', query_lower))
        
        scored_items = []
        
        for key, item in self.knowledge_data.items():
            # Combine all text content for searching
            search_text = f"{item.get('title', '')} {item.get('content', '')}"
            
            # Add structured content
            for field in ['key_points', 'components', 'capabilities', 'patterns', 
                         'practices', 'use_cases', 'issues', 'steps', 'details', 'tools']:
                if field in item:
                    if isinstance(item[field], list):
                        search_text += " " + " ".join(str(x) for x in item[field])
                    else:
                        search_text += " " + str(item[field])
            
            search_text_lower = search_text.lower()
            search_words = set(re.findall(r'\w+', search_text_lower))
            
            # Calculate relevance score
            # Exact phrase match gets highest score
            if query_lower in search_text_lower:
                score = 10.0
            else:
                # Word overlap score
                common_words = query_words.intersection(search_words)
                if len(query_words) > 0:
                    score = len(common_words) / len(query_words)
                else:
                    score = 0
            
            if score > 0:
                result_item = item.copy()
                result_item['similarity_score'] = score
                result_item['key'] = key
                scored_items.append(result_item)
        
        # Sort by score and return top_k
        scored_items.sort(key=lambda x: x['similarity_score'], reverse=True)
        return scored_items[:top_k]

class MCPChatbot:
    """MCP Q&A Chatbot using OpenAI API"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "1000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.knowledge_base = MCPKnowledgeBase()
        
        # System prompt for MCP expertise
        self.system_prompt = """You are an expert on the Model Context Protocol (MCP). You help developers understand MCP concepts, implementation, best practices, and troubleshooting. 

Your responses should be:
- Clear and technically accurate
- Include practical examples when relevant
- Reference specific MCP concepts and terminology
- Provide actionable guidance for implementation
- Be helpful for both beginners and experienced developers

When answering questions, use the provided context from the knowledge base to ensure accuracy and completeness."""
    
    def get_response(self, user_question: str, conversation_history: List[Dict[str, str]] = None) -> str:
        """Generate response using OpenAI API with MCP knowledge"""
        
        # Search for relevant content in knowledge base
        relevant_content = self.knowledge_base.search_relevant_content(user_question, top_k=3)
        
        # Create context from relevant content
        context = self._format_context(relevant_content)
        
        # Prepare messages
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history[-6:])  # Keep last 6 messages for context
        
        # Add context and current question
        context_message = f"Context from MCP knowledge base:\n{context}\n\nUser question: {user_question}"
        messages.append({"role": "user", "content": context_message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def _format_context(self, relevant_content: List[Dict[str, Any]]) -> str:
        """Format relevant content as context for the AI"""
        if not relevant_content:
            return "No specific context found in knowledge base."
        
        context_parts = []
        for item in relevant_content:
            context_part = f"**{item.get('title', 'Unknown Topic')}**\n"
            context_part += f"{item.get('content', '')}\n"
            
            # Add structured information
            for field in ['key_points', 'components', 'capabilities', 'patterns', 
                         'practices', 'use_cases', 'issues', 'steps', 'details', 'tools']:
                if field in item and item[field]:
                    context_part += f"\n{field.replace('_', ' ').title()}:\n"
                    if isinstance(item[field], list):
                        for point in item[field]:
                            context_part += f"- {point}\n"
                    else:
                        context_part += f"{item[field]}\n"
            
            context_parts.append(context_part)
        
        return "\n---\n".join(context_parts)
    
    def get_suggested_questions(self) -> List[str]:
        """Get a list of suggested questions for users"""
        return [
            "What is the Model Context Protocol (MCP)?",
            "How do I create my first MCP server?",
            "What are the different types of MCP capabilities?",
            "How does MCP handle security and permissions?",
            "What are common use cases for MCP servers?",
            "How do I troubleshoot MCP connection issues?",
            "What's the difference between MCP resources and tools?",
            "How do I implement authentication in MCP servers?",
            "What are best practices for MCP server development?",
            "How do I test my MCP server implementation?"
        ]
