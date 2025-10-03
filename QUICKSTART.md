# LuminaAI v2.0 Quick Start Guide

Get up and running with LuminaAI v2.0 in minutes!

## Installation

### Option 1: Direct Usage

```bash
# Clone the repository
git clone https://github.com/goody81/treaai.git
cd treaai

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Package Installation

```bash
# Install as a Python package
pip install -e .
```

## 5-Minute Tutorial

### 1. Basic Hello World

```python
from luminaai_v2 import create_lumina_ai

# Initialize LuminaAI
lumina = create_lumina_ai()

# Process your first prompt
result = lumina.process("Hello, LuminaAI!")
print(result['output'])
```

**Output:**
```
LuminaAI v2.0 processed: Hello, LuminaAI!
```

### 2. Using the Assistant

```python
from luminaai_v2 import create_assistant

# Create an assistant
assistant = create_assistant()

# Have a conversation
response = assistant.chat("What is LuminaAI?")
print(response)

# Continue the conversation (with context)
response = assistant.chat("What can it do?")
print(response)
```

### 3. Custom Configuration

```python
from luminaai_v2 import create_lumina_ai

# Create custom configuration
config = {
    "max_tokens": 2048,
    "temperature": 0.5,
    "enable_caching": True
}

# Initialize with custom config
lumina = create_lumina_ai(config=config)

# Process a prompt
result = lumina.process("Generate a creative story")
print(result['output'])
```

### 4. Batch Processing

```python
from luminaai_v2 import create_lumina_ai

lumina = create_lumina_ai()

# Process multiple prompts at once
prompts = [
    "What is AI?",
    "Explain machine learning",
    "What is deep learning?"
]

results = lumina.batch_process(prompts)

for i, result in enumerate(results, 1):
    print(f"{i}. {result['prompt']}")
    print(f"   {result['output']}\n")
```

### 5. Working with Models

```python
from luminaai_v2 import create_lumina_ai, ModelType

lumina = create_lumina_ai()

# Register a custom model
lumina.register_model(
    ModelType.CODE,
    "python-expert",
    {"specialization": "python"}
)

# Use the model
result = lumina.process(
    "Write a Python function to sort a list",
    model_name="python-expert"
)
print(result['output'])
```

### 6. Performance Monitoring

```python
from luminaai_v2 import create_lumina_ai
from utils import PerformanceMonitor
import time

lumina = create_lumina_ai()
monitor = PerformanceMonitor()

# Process and measure
start = time.time()
result = lumina.process("Test prompt")
duration = time.time() - start

# Record metrics
monitor.record_request(True, duration)

# View metrics
metrics = monitor.get_metrics()
print(f"Total requests: {metrics['total_requests']}")
print(f"Average time: {metrics['avg_time']:.4f}s")
```

### 7. Caching for Performance

```python
from luminaai_v2 import create_lumina_ai
from utils import Cache, hash_prompt

lumina = create_lumina_ai()
cache = Cache(max_size=1000)

def get_response(prompt):
    # Check cache first
    prompt_hash = hash_prompt(prompt)
    cached = cache.get(prompt_hash)
    
    if cached:
        print("Using cached result")
        return cached
    
    # Process and cache
    print("Processing new request")
    result = lumina.process(prompt)
    cache.set(prompt_hash, result)
    return result

# First call - processes
response1 = get_response("What is quantum computing?")

# Second call - uses cache
response2 = get_response("What is quantum computing?")
```

### 8. Configuration Management

```python
from luminaai_v2 import create_lumina_ai
from utils import load_config, save_config

# Load from file
config = load_config("config.json")
lumina = create_lumina_ai(config=config)

# Modify configuration
new_config = {
    "temperature": 0.8,
    "max_tokens": 8192
}
lumina.update_config(new_config)

# Save configuration
save_config(lumina.config, "my_config.json")
```

### 9. Get System Information

```python
from luminaai_v2 import create_lumina_ai

lumina = create_lumina_ai()

# Get capabilities
capabilities = lumina.get_capabilities()

print(f"Version: {capabilities['version']}")
print(f"Session ID: {capabilities['session_id']}")
print(f"\nCapabilities:")
for cap in capabilities['capabilities']:
    print(f"  - {cap}")
```

### 10. Export Session Data

```python
from luminaai_v2 import create_lumina_ai

lumina = create_lumina_ai()

# Do some work
lumina.process("Task 1")
lumina.process("Task 2")
lumina.register_model(ModelType.LANGUAGE, "test-model")

# Export session
lumina.export_session("my_session.json")
print("Session exported!")
```

## Running Examples

The repository includes comprehensive examples:

```bash
# Run all examples
python examples.py

# Run the main module demo
python luminaai_v2.py

# Test utilities
python utils.py
```

## Common Use Cases

### Use Case 1: Code Generation Assistant

```python
from luminaai_v2 import create_assistant

assistant = create_assistant({
    "temperature": 0.3,  # Lower for more precise code
    "max_tokens": 4096
})

# Generate code
response = assistant.chat("""
Write a Python function that:
- Takes a list of numbers
- Returns the sum of even numbers
- Handles empty lists
""")
print(response)
```

### Use Case 2: Data Analysis

```python
from luminaai_v2 import create_lumina_ai

lumina = create_lumina_ai()

data = """
Sales data for Q1:
January: $50,000
February: $65,000
March: $70,000
"""

result = lumina.process(f"Analyze this sales data and provide insights:\n{data}")
print(result['output'])
```

### Use Case 3: Content Generation

```python
from luminaai_v2 import create_lumina_ai

lumina = create_lumina_ai({
    "temperature": 0.9,  # Higher for more creativity
    "max_tokens": 2048
})

topics = ["AI", "Future", "Technology"]
contents = lumina.batch_process([
    f"Write a creative paragraph about {topic}"
    for topic in topics
])

for topic, content in zip(topics, contents):
    print(f"\n{topic}:")
    print(content['output'])
```

## Next Steps

1. **Read the full documentation**: Check out `README.md` for comprehensive information
2. **Explore the API**: See `API.md` for detailed API reference
3. **Run examples**: Execute `examples.py` to see all features in action
4. **Customize configuration**: Edit `config.json` for your needs
5. **Build your application**: Start integrating LuminaAI into your projects!

## Troubleshooting

### Import Error

```python
# Make sure you're in the right directory
import sys
sys.path.append('/path/to/treaai')

from luminaai_v2 import create_lumina_ai
```

### Configuration Issues

```python
from utils import validate_config

config = {...}
if validate_config(config):
    print("Config is valid")
else:
    print("Config has issues")
```

### Check Installation

```bash
# Verify Python version
python --version  # Should be 3.7+

# Test imports
python -c "from luminaai_v2 import create_lumina_ai; print('OK')"
```

## Support

- **Documentation**: See `README.md` and `API.md`
- **Examples**: Run `python examples.py`
- **Issues**: https://github.com/goody81/treaai/issues

## Tips for Success

1. **Start Simple**: Begin with basic examples and gradually add complexity
2. **Use Caching**: Enable caching for frequently used prompts
3. **Monitor Performance**: Use `PerformanceMonitor` to track metrics
4. **Adjust Temperature**: Lower (0.3) for precise, higher (0.9) for creative
5. **Batch When Possible**: Use `batch_process()` for multiple requests
6. **Save Sessions**: Export important sessions with `export_session()`
7. **Customize Config**: Adjust configuration for your specific needs

---

**Congratulations!** You're now ready to use LuminaAI v2.0! 🚀

For more information, see the full documentation in `README.md`.
