"""
Example usage of LuminaAI v2.0
Demonstrates various features and capabilities
"""

import json
from luminaai_v2 import (
    create_lumina_ai,
    create_assistant,
    LuminaAICore,
    ModelType
)
from utils import (
    Cache,
    PerformanceMonitor,
    TokenCounter,
    hash_prompt,
    load_config
)


def example_basic_usage():
    """Basic usage example"""
    print("\n" + "=" * 60)
    print("Example 1: Basic LuminaAI Usage")
    print("=" * 60)
    
    # Create LuminaAI instance
    lumina = create_lumina_ai()
    
    # Process a simple prompt
    result = lumina.process("Explain quantum computing in simple terms")
    
    print(f"\nPrompt: {result['prompt']}")
    print(f"Output: {result['output']}")
    print(f"Status: {result['status']}")


def example_custom_config():
    """Custom configuration example"""
    print("\n" + "=" * 60)
    print("Example 2: Custom Configuration")
    print("=" * 60)
    
    # Create custom config
    custom_config = {
        "max_tokens": 2048,
        "temperature": 0.5,
        "top_p": 0.95,
        "enable_caching": True,
        "optimization_level": "high_performance"
    }
    
    # Initialize with custom config
    lumina = create_lumina_ai(config=custom_config)
    
    print("\nCustom Configuration:")
    print(json.dumps(lumina.config, indent=2))
    
    # Process with custom config
    result = lumina.process("Generate a creative story")
    print(f"\nResult: {result['output']}")


def example_model_registration():
    """Model registration example"""
    print("\n" + "=" * 60)
    print("Example 3: Model Registration")
    print("=" * 60)
    
    lumina = create_lumina_ai()
    
    # Register different model types
    lumina.register_model(
        ModelType.LANGUAGE,
        "gpt-advanced",
        {"version": "latest", "specialization": "general"}
    )
    
    lumina.register_model(
        ModelType.CODE,
        "codegen-pro",
        {"version": "1.0", "specialization": "code_generation"}
    )
    
    lumina.register_model(
        ModelType.REASONING,
        "logic-engine",
        {"version": "2.0", "specialization": "logical_reasoning"}
    )
    
    # Display capabilities
    capabilities = lumina.get_capabilities()
    print("\nRegistered Models:")
    for model in capabilities['models']:
        print(f"  - {model}")


def example_batch_processing():
    """Batch processing example"""
    print("\n" + "=" * 60)
    print("Example 4: Batch Processing")
    print("=" * 60)
    
    lumina = create_lumina_ai()
    
    # Multiple prompts
    prompts = [
        "What is artificial intelligence?",
        "Explain machine learning",
        "What is deep learning?",
        "How does neural network work?"
    ]
    
    # Batch process
    results = lumina.batch_process(prompts)
    
    print(f"\nProcessed {len(results)} prompts:")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['prompt']}")
        print(f"   Output: {result['output']}")


def example_assistant_chat():
    """Assistant chat example"""
    print("\n" + "=" * 60)
    print("Example 5: LuminaAI Assistant")
    print("=" * 60)
    
    # Create assistant
    assistant = create_assistant()
    
    # Multi-turn conversation
    messages = [
        "Hello! What can you help me with?",
        "Tell me about LuminaAI v2.0",
        "What are its key features?"
    ]
    
    print("\nConversation:")
    for msg in messages:
        print(f"\nUser: {msg}")
        response = assistant.chat(msg)
        print(f"Assistant: {response}")


def example_with_utilities():
    """Example using utilities"""
    print("\n" + "=" * 60)
    print("Example 6: Using Utilities")
    print("=" * 60)
    
    lumina = create_lumina_ai()
    
    # Setup cache
    cache = Cache(max_size=100)
    
    # Setup performance monitor
    monitor = PerformanceMonitor()
    
    # Process with caching
    prompt = "Explain the future of AI"
    prompt_hash = hash_prompt(prompt)
    
    print(f"\nPrompt: {prompt}")
    print(f"Prompt hash: {prompt_hash}")
    
    # Check cache
    cached_result = cache.get(prompt_hash)
    
    if cached_result:
        print("Using cached result")
        result = cached_result
    else:
        print("Processing new request")
        import time
        start = time.time()
        result = lumina.process(prompt)
        duration = time.time() - start
        
        # Cache result
        cache.set(prompt_hash, result)
        
        # Record metrics
        monitor.record_request(True, duration)
    
    print(f"Output: {result['output']}")
    
    # Display metrics
    print("\nPerformance Metrics:")
    print(json.dumps(monitor.get_metrics(), indent=2))
    
    # Token counting
    token_count = TokenCounter.count(prompt)
    print(f"\nEstimated tokens: {token_count}")
    print(f"Estimated cost: ${TokenCounter.estimate_cost(token_count):.6f}")


def example_session_export():
    """Session export example"""
    print("\n" + "=" * 60)
    print("Example 7: Session Export")
    print("=" * 60)
    
    lumina = create_lumina_ai()
    
    # Register some models
    lumina.register_model(ModelType.LANGUAGE, "test-model-1")
    lumina.register_model(ModelType.CODE, "test-model-2")
    
    # Process some data
    lumina.process("Test prompt 1")
    lumina.process("Test prompt 2")
    
    # Export session
    export_path = "/tmp/lumina_session.json"
    lumina.export_session(export_path)
    
    print(f"\nSession exported to: {export_path}")
    
    # Read and display
    with open(export_path, 'r') as f:
        session_data = json.load(f)
    
    print("\nExported Session Data:")
    print(json.dumps(session_data, indent=2))


def example_config_management():
    """Configuration management example"""
    print("\n" + "=" * 60)
    print("Example 8: Configuration Management")
    print("=" * 60)
    
    # Load config from file
    try:
        config = load_config("config.json")
        print("\nLoaded configuration from config.json:")
        if "models" in config:
            print("\nAvailable model configurations:")
            for model_name, model_config in config["models"].items():
                print(f"\n{model_name}:")
                print(json.dumps(model_config, indent=2))
    except Exception as e:
        print(f"Could not load config: {e}")


def run_all_examples():
    """Run all examples"""
    print("\n" + "=" * 80)
    print(" " * 20 + "LuminaAI v2.0 Examples")
    print("=" * 80)
    
    examples = [
        example_basic_usage,
        example_custom_config,
        example_model_registration,
        example_batch_processing,
        example_assistant_chat,
        example_with_utilities,
        example_session_export,
        example_config_management
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\nError in {example.__name__}: {e}")
    
    print("\n" + "=" * 80)
    print(" " * 20 + "All Examples Completed!")
    print("=" * 80)


if __name__ == "__main__":
    run_all_examples()
