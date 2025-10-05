# LuminaAI v2.0 🚀

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/goody81/treaai)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-yellow.svg)](https://www.python.org/)

**LuminaAI v2.0** - Advanced AI System built with the treaai framework, taking AI capabilities to the next level.

## 🌟 Overview

LuminaAI v2.0 is a comprehensive, state-of-the-art AI system designed to provide powerful AI capabilities including:

- **Multi-Modal AI Processing** - Handle text, code, reasoning, and more
- **Advanced Configuration** - Highly customizable for your specific needs
- **Performance Optimized** - Built-in caching and performance monitoring
- **Safety First** - Comprehensive safety filters and content moderation
- **Batch Processing** - Efficiently process multiple requests
- **Conversation Memory** - Context-aware assistant with conversation history
- **Extensible Architecture** - Easy to extend with custom models and capabilities

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/goody81/treaai.git
cd treaai

# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

### Basic Usage

```python
from luminaai_v2 import create_lumina_ai

# Initialize LuminaAI
lumina = create_lumina_ai()

# Process a prompt
result = lumina.process("Explain quantum computing")
print(result['output'])

# Get capabilities
capabilities = lumina.get_capabilities()
print(capabilities)
```

### Using the Assistant

```python
from luminaai_v2 import create_assistant

# Create assistant
assistant = create_assistant()

# Chat with the assistant
response = assistant.chat("Hello! What can you do?")
print(response)

# Continue conversation
response = assistant.chat("Tell me about your features")
print(response)
```

## 📚 Features

### Core Capabilities

- **Text Generation**: Advanced language model processing
- **Code Generation**: Specialized code generation and analysis
- **Reasoning**: Logical reasoning and problem-solving
- **Batch Processing**: Process multiple prompts efficiently
- **Streaming**: Real-time streaming output support
- **Caching**: Intelligent caching for improved performance

### Model Types

LuminaAI v2.0 supports multiple model types:

- `LANGUAGE` - General language processing
- `VISION` - Visual understanding (coming soon)
- `MULTIMODAL` - Combined modalities
- `REASONING` - Logical reasoning and analysis
- `CODE` - Code generation and understanding

### Configuration

Customize LuminaAI with flexible configuration:

```python
custom_config = {
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9,
    "enable_streaming": True,
    "enable_caching": True,
    "safety_filters": True
}

lumina = create_lumina_ai(config=custom_config)
```

Load configuration from file:

```python
from utils import load_config

config = load_config("config.json")
lumina = create_lumina_ai(config=config)
```

## 🔧 Advanced Usage

### Register Custom Models

```python
from luminaai_v2 import create_lumina_ai, ModelType

lumina = create_lumina_ai()

# Register a custom model
lumina.register_model(
    ModelType.CODE,
    "my-code-model",
    {"version": "1.0", "specialization": "python"}
)
```

### Batch Processing

```python
prompts = [
    "What is AI?",
    "Explain machine learning",
    "What is deep learning?"
]

results = lumina.batch_process(prompts)
for result in results:
    print(f"Q: {result['prompt']}")
    print(f"A: {result['output']}\n")
```

### Performance Monitoring

```python
from utils import PerformanceMonitor

monitor = PerformanceMonitor()

# Your processing code
result = lumina.process("test prompt")

# Record metrics
monitor.record_request(True, 0.5)

# Get metrics
metrics = monitor.get_metrics()
print(f"Average time: {metrics['avg_time']:.2f}s")
```

### Caching

```python
from utils import Cache, hash_prompt

cache = Cache(max_size=1000)
prompt = "Your prompt here"
prompt_hash = hash_prompt(prompt)

# Check cache
cached = cache.get(prompt_hash)
if cached:
    result = cached
else:
    result = lumina.process(prompt)
    cache.set(prompt_hash, result)
```

## 📖 Examples

Run the examples to see LuminaAI v2.0 in action:

```bash
# Run all examples
python examples.py

# Or run the main module
python luminaai_v2.py
```

Example outputs demonstrate:
1. Basic usage
2. Custom configuration
3. Model registration
4. Batch processing
5. Assistant chat
6. Utility functions
7. Session export
8. Configuration management

## 🏗️ Architecture

```
LuminaAI v2.0
├── luminaai_v2.py      # Core AI engine
├── utils.py            # Utility functions
├── examples.py         # Usage examples
├── config.json         # Default configuration
├── setup.py            # Package setup
└── requirements.txt    # Dependencies
```

### Core Components

- **LuminaAICore**: Main AI processing engine
- **LuminaAIAssistant**: High-level assistant interface
- **Cache**: Intelligent caching system
- **PerformanceMonitor**: Performance tracking
- **TokenCounter**: Token usage estimation
- **RateLimiter**: API rate limiting

## 🔒 Safety & Privacy

LuminaAI v2.0 includes comprehensive safety features:

- **Content Filtering**: Automatic content moderation
- **Toxicity Detection**: Identify and filter toxic content
- **Bias Mitigation**: Reduce model biases
- **Privacy Protection**: User data protection
- **Safety Filters**: Configurable safety levels

## 🎯 Performance

Optimized for performance:

- **Intelligent Caching**: Reduce redundant processing
- **Batch Processing**: Efficient handling of multiple requests
- **Rate Limiting**: Prevent API overload
- **Performance Monitoring**: Track and optimize metrics
- **Configurable Optimization**: Balance speed vs. quality

## 📊 Monitoring & Metrics

Track your LuminaAI usage:

```python
# Get capabilities and status
capabilities = lumina.get_capabilities()

# Export session data
lumina.export_session("session_data.json")

# Monitor performance
from utils import PerformanceMonitor
monitor = PerformanceMonitor()
metrics = monitor.get_metrics()
```

## 🛠️ Development

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests (when available)
pytest tests/
```

### Code Quality

```bash
# Format code
black luminaai_v2.py utils.py examples.py

# Lint code
flake8 luminaai_v2.py utils.py examples.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Why LuminaAI v2.0?

LuminaAI v2.0 represents the next generation of AI systems:

- **Production Ready**: Built for real-world applications
- **Highly Configurable**: Adapt to your specific needs
- **Performance Optimized**: Fast and efficient
- **Safety First**: Comprehensive safety features
- **Easy to Use**: Simple API with powerful capabilities
- **Extensible**: Easy to add custom models and features
- **Well Documented**: Comprehensive documentation and examples

## 📞 Support

For issues, questions, or contributions, please visit:
- GitHub Issues: https://github.com/goody81/treaai/issues
- Repository: https://github.com/goody81/treaai

## 🔮 Roadmap

Future enhancements planned:

- [ ] Vision model integration
- [ ] Real-time streaming API
- [ ] Multi-language support
- [ ] Cloud deployment templates
- [ ] Advanced analytics dashboard
- [ ] Plugin system for extensions
- [ ] Model fine-tuning capabilities
- [ ] Enhanced conversation memory
- [ ] Web UI interface
- [ ] API endpoint server

---

**LuminaAI v2.0** - Powering the future of AI with treaai 🚀

Built with ❤️ by the treaai team
