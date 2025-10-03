# LuminaAI v2.0 API Reference

## Table of Contents

1. [Core Classes](#core-classes)
2. [Model Types](#model-types)
3. [Configuration](#configuration)
4. [Utility Functions](#utility-functions)
5. [Examples](#examples)

## Core Classes

### LuminaAICore

Main AI processing engine for LuminaAI v2.0.

#### Constructor

```python
LuminaAICore(config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `config`: Optional configuration dictionary

**Example:**
```python
from luminaai_v2 import LuminaAICore

lumina = LuminaAICore({
    "max_tokens": 4096,
    "temperature": 0.7
})
```

#### Methods

##### `process(prompt: str, model_name: Optional[str] = None, **kwargs) -> Dict[str, Any]`

Process a prompt through LuminaAI.

**Parameters:**
- `prompt`: Input prompt to process
- `model_name`: Optional specific model to use
- `**kwargs`: Additional parameters

**Returns:**
- Dictionary containing processing results

**Example:**
```python
result = lumina.process("Explain quantum computing")
print(result['output'])
```

##### `batch_process(prompts: List[str], **kwargs) -> List[Dict[str, Any]]`

Process multiple prompts in batch.

**Parameters:**
- `prompts`: List of prompts to process
- `**kwargs`: Additional parameters

**Returns:**
- List of processing results

**Example:**
```python
prompts = ["What is AI?", "Explain ML"]
results = lumina.batch_process(prompts)
```

##### `register_model(model_type: ModelType, model_name: str, model_config: Optional[Dict] = None) -> None`

Register a new AI model.

**Parameters:**
- `model_type`: Type of the model (ModelType enum)
- `model_name`: Name identifier for the model
- `model_config`: Optional model configuration

**Example:**
```python
from luminaai_v2 import ModelType

lumina.register_model(
    ModelType.CODE,
    "codegen-v1",
    {"specialization": "python"}
)
```

##### `get_capabilities() -> Dict[str, Any]`

Get LuminaAI capabilities and status.

**Returns:**
- Dictionary of capabilities

**Example:**
```python
capabilities = lumina.get_capabilities()
print(capabilities['version'])
print(capabilities['models'])
```

##### `update_config(new_config: Dict[str, Any]) -> None`

Update LuminaAI configuration.

**Parameters:**
- `new_config`: New configuration parameters

**Example:**
```python
lumina.update_config({"temperature": 0.5})
```

##### `export_session(filepath: str) -> None`

Export current session data.

**Parameters:**
- `filepath`: Path to export session data

**Example:**
```python
lumina.export_session("session.json")
```

---

### LuminaAIAssistant

High-level assistant interface with conversation memory.

#### Constructor

```python
LuminaAIAssistant(config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `config`: Optional configuration dictionary

#### Methods

##### `chat(message: str, context: Optional[Dict[str, Any]] = None) -> str`

Chat with the assistant.

**Parameters:**
- `message`: User message
- `context`: Optional context information

**Returns:**
- Assistant response string

**Example:**
```python
from luminaai_v2 import create_assistant

assistant = create_assistant()
response = assistant.chat("Hello!")
print(response)
```

##### `reset_conversation() -> None`

Reset conversation history.

**Example:**
```python
assistant.reset_conversation()
```

---

## Model Types

### ModelType Enum

Available model types in LuminaAI:

```python
class ModelType(Enum):
    LANGUAGE = "language"      # General language processing
    VISION = "vision"          # Visual understanding
    MULTIMODAL = "multimodal"  # Combined modalities
    REASONING = "reasoning"    # Logical reasoning
    CODE = "code"              # Code generation
```

**Usage:**
```python
from luminaai_v2 import ModelType

model_type = ModelType.CODE
print(model_type.value)  # "code"
```

---

## Configuration

### Default Configuration

```python
{
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "enable_streaming": True,
    "enable_caching": True,
    "cache_size": 1000,
    "safety_filters": True,
    "optimization_level": "balanced"
}
```

### Configuration Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_tokens` | int | 4096 | Maximum tokens in response |
| `temperature` | float | 0.7 | Sampling temperature (0-2) |
| `top_p` | float | 0.9 | Nucleus sampling parameter |
| `top_k` | int | 50 | Top-k sampling parameter |
| `enable_streaming` | bool | True | Enable streaming output |
| `enable_caching` | bool | True | Enable response caching |
| `cache_size` | int | 1000 | Maximum cache entries |
| `safety_filters` | bool | True | Enable safety filters |
| `optimization_level` | str | "balanced" | Optimization level |

### Loading Configuration

```python
from utils import load_config

# Load from JSON file
config = load_config("config.json")
lumina = create_lumina_ai(config=config)
```

---

## Utility Functions

### Factory Functions

#### `create_lumina_ai(config: Optional[Dict] = None) -> LuminaAICore`

Create LuminaAI instance.

```python
lumina = create_lumina_ai()
```

#### `create_assistant(config: Optional[Dict] = None) -> LuminaAIAssistant`

Create LuminaAI Assistant.

```python
assistant = create_assistant()
```

### Cache

#### `Cache(max_size: int = 1000)`

Simple caching system.

**Methods:**
- `get(key: str) -> Optional[Any]`
- `set(key: str, value: Any) -> None`
- `clear() -> None`

**Example:**
```python
from utils import Cache

cache = Cache(max_size=100)
cache.set("key", "value")
result = cache.get("key")
```

### PerformanceMonitor

#### `PerformanceMonitor()`

Monitor performance metrics.

**Methods:**
- `record_request(success: bool, duration: float) -> None`
- `get_metrics() -> Dict[str, Any]`
- `reset() -> None`

**Example:**
```python
from utils import PerformanceMonitor

monitor = PerformanceMonitor()
monitor.record_request(True, 0.5)
metrics = monitor.get_metrics()
```

### TokenCounter

#### `TokenCounter.count(text: str) -> int`

Count approximate tokens in text.

**Example:**
```python
from utils import TokenCounter

tokens = TokenCounter.count("Hello, world!")
cost = TokenCounter.estimate_cost(tokens)
```

### Helper Functions

#### `hash_prompt(prompt: str) -> str`

Generate hash for a prompt.

```python
from utils import hash_prompt

prompt_hash = hash_prompt("Your prompt")
```

#### `validate_config(config: Dict[str, Any]) -> bool`

Validate configuration.

```python
from utils import validate_config

is_valid = validate_config(config)
```

#### `chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]`

Split text into chunks.

```python
from utils import chunk_text

chunks = chunk_text(long_text, chunk_size=500)
```

---

## Examples

### Basic Example

```python
from luminaai_v2 import create_lumina_ai

lumina = create_lumina_ai()
result = lumina.process("Hello, LuminaAI!")
print(result['output'])
```

### Advanced Example

```python
from luminaai_v2 import create_lumina_ai, ModelType
from utils import Cache, PerformanceMonitor, hash_prompt

# Setup
lumina = create_lumina_ai({
    "temperature": 0.5,
    "max_tokens": 2048
})
cache = Cache()
monitor = PerformanceMonitor()

# Register model
lumina.register_model(ModelType.CODE, "my-model")

# Process with caching
prompt = "Write Python code"
prompt_hash = hash_prompt(prompt)

cached = cache.get(prompt_hash)
if not cached:
    result = lumina.process(prompt)
    cache.set(prompt_hash, result)
    monitor.record_request(True, 0.3)
else:
    result = cached

print(result['output'])
```

### Assistant Example

```python
from luminaai_v2 import create_assistant

assistant = create_assistant()

# Multi-turn conversation
response1 = assistant.chat("What is LuminaAI?")
response2 = assistant.chat("What are its features?")

print(response1)
print(response2)

# Reset conversation
assistant.reset_conversation()
```

---

For more examples, see `examples.py` in the repository.
