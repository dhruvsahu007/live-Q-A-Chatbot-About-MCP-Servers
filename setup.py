#!/usr/bin/env python3
"""
Setup and test script for MCP Q&A Chatbot
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def check_env_file():
    """Check if .env file exists and has API key"""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        print("📝 Creating .env file from template...")
        
        # Copy from example
        example_file = Path(".env.example")
        if example_file.exists():
            with open(example_file, 'r') as f:
                content = f.read()
            with open(env_file, 'w') as f:
                f.write(content)
            print("✅ .env file created. Please add your OpenAI API key.")
        return False
    
    # Check if API key is set
    with open(env_file, 'r') as f:
        content = f.read()
        if "your_openai_api_key_here" in content:
            print("❌ Please set your OpenAI API key in .env file")
            return False
    
    print("✅ .env file configured")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], check=True, capture_output=True)
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    required_modules = [
        "streamlit",
        "openai",
        "sentence_transformers",
        "sklearn",
        "numpy",
        "dotenv"
    ]
    
    failed_imports = []
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError:
            print(f"  ❌ {module}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"❌ Failed to import: {', '.join(failed_imports)}")
        return False
    
    print("✅ All modules imported successfully")
    return True

def test_knowledge_base():
    """Test if knowledge base loads correctly"""
    print("📚 Testing knowledge base...")
    try:
        import json
        with open("knowledge_base.json", 'r') as f:
            data = json.load(f)
        
        if len(data) > 0:
            print(f"✅ Knowledge base loaded with {len(data)} topics")
            return True
        else:
            print("❌ Knowledge base is empty")
            return False
    except Exception as e:
        print(f"❌ Failed to load knowledge base: {e}")
        return False

def run_tests():
    """Run all setup tests"""
    print("🚀 MCP Q&A Chatbot Setup & Test")
    print("=" * 40)
    
    tests = [
        ("Python Version", check_python_version),
        ("Environment File", check_env_file),
        ("Requirements", install_requirements),
        ("Module Imports", test_imports),
        ("Knowledge Base", test_knowledge_base)
    ]
    
    all_passed = True
    for test_name, test_func in tests:
        print(f"\n🔧 {test_name}:")
        if not test_func():
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 All tests passed! Ready to run the chatbot.")
        print("💡 Run: streamlit run app.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
    
    return all_passed

def main():
    """Main function"""
    if "--test" in sys.argv:
        run_tests()
    else:
        print("MCP Q&A Chatbot Setup")
        print("Available commands:")
        print("  python setup.py --test    Run setup tests")
        print("  streamlit run app.py      Start the chatbot")

if __name__ == "__main__":
    main()
