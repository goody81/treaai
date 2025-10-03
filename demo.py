#!/usr/bin/env python3
"""
LuminaAI v2.0 Demo
Interactive demonstration of LuminaAI capabilities
"""

import json
import time
from luminaai_v2 import create_lumina_ai, create_assistant, ModelType
from utils import Cache, PerformanceMonitor, TokenCounter, hash_prompt


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def print_section(title):
    """Print a section divider"""
    print("\n" + "-" * 70)
    print(f"  {title}")
    print("-" * 70 + "\n")


def demo_introduction():
    """Show introduction"""
    print_header("🌟 Welcome to LuminaAI v2.0 🌟")
    print("LuminaAI v2.0 is an advanced AI system built with the treaai framework.")
    print("This demo will showcase its powerful capabilities.\n")
    input("Press Enter to begin the demo...")


def demo_initialization():
    """Demonstrate initialization"""
    print_section("1. Initialization")
    print("Creating LuminaAI instance...")
    
    lumina = create_lumina_ai()
    
    print("✓ LuminaAI v2.0 initialized successfully!")
    print(f"  Session ID: {lumina.session_id}")
    print(f"  Version: {lumina.version}")
    
    return lumina


def demo_capabilities(lumina):
    """Show system capabilities"""
    print_section("2. System Capabilities")
    
    capabilities = lumina.get_capabilities()
    
    print("Available Capabilities:")
    for cap in capabilities['capabilities']:
        print(f"  ✓ {cap.replace('_', ' ').title()}")
    
    print("\nConfiguration:")
    print(f"  • Max Tokens: {capabilities['config']['max_tokens']}")
    print(f"  • Temperature: {capabilities['config']['temperature']}")
    print(f"  • Caching: {'Enabled' if capabilities['config']['enable_caching'] else 'Disabled'}")
    print(f"  • Safety Filters: {'Enabled' if capabilities['config']['safety_filters'] else 'Disabled'}")


def demo_basic_processing(lumina):
    """Demonstrate basic processing"""
    print_section("3. Basic AI Processing")
    
    prompts = [
        "What is artificial intelligence?",
        "Explain the concept of machine learning",
        "How does deep learning work?"
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n{i}. Prompt: \"{prompt}\"")
        result = lumina.process(prompt)
        print(f"   Response: {result['output']}")
        print(f"   Status: {result['status']}")


def demo_model_registration(lumina):
    """Demonstrate model registration"""
    print_section("4. Model Registration")
    
    models = [
        (ModelType.LANGUAGE, "gpt-lumina", {"specialization": "general"}),
        (ModelType.CODE, "codegen-lumina", {"specialization": "code"}),
        (ModelType.REASONING, "logic-lumina", {"specialization": "reasoning"})
    ]
    
    print("Registering AI models:")
    for model_type, name, config in models:
        lumina.register_model(model_type, name, config)
        print(f"  ✓ {name} ({model_type.value})")
    
    capabilities = lumina.get_capabilities()
    print(f"\nTotal registered models: {len(capabilities['models'])}")


def demo_batch_processing(lumina):
    """Demonstrate batch processing"""
    print_section("5. Batch Processing")
    
    prompts = [
        "Define neural networks",
        "What is NLP?",
        "Explain computer vision",
        "What is reinforcement learning?"
    ]
    
    print(f"Processing {len(prompts)} prompts in batch...\n")
    
    start_time = time.time()
    results = lumina.batch_process(prompts)
    duration = time.time() - start_time
    
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['prompt'][:50]}...")
        print(f"   → {result['output'][:80]}...")
    
    print(f"\n✓ Batch completed in {duration:.3f} seconds")
    print(f"  Average: {duration/len(prompts):.3f}s per prompt")


def demo_assistant(lumina):
    """Demonstrate assistant functionality"""
    print_section("6. LuminaAI Assistant")
    
    print("Creating conversational assistant...")
    assistant = create_assistant()
    
    conversation = [
        "Hello! What is LuminaAI?",
        "What makes it special?",
        "What can it help me with?"
    ]
    
    print("\nConversation Demo:\n")
    for msg in conversation:
        print(f"👤 User: {msg}")
        response = assistant.chat(msg)
        print(f"🤖 Assistant: {response}\n")
        time.sleep(0.5)


def demo_performance_monitoring():
    """Demonstrate performance monitoring"""
    print_section("7. Performance Monitoring")
    
    print("Setting up performance monitor...")
    monitor = PerformanceMonitor()
    lumina = create_lumina_ai()
    
    print("\nRunning performance test (10 requests)...")
    
    for i in range(10):
        start = time.time()
        lumina.process(f"Test prompt {i+1}")
        duration = time.time() - start
        monitor.record_request(True, duration)
    
    metrics = monitor.get_metrics()
    
    print("\nPerformance Metrics:")
    print(f"  • Total Requests: {metrics['total_requests']}")
    print(f"  • Successful: {metrics['successful_requests']}")
    print(f"  • Failed: {metrics['failed_requests']}")
    print(f"  • Average Time: {metrics['avg_time']:.4f}s")
    print(f"  • Total Time: {metrics['total_time']:.4f}s")


def demo_caching():
    """Demonstrate caching"""
    print_section("8. Intelligent Caching")
    
    cache = Cache(max_size=100)
    lumina = create_lumina_ai()
    
    prompt = "What is quantum computing?"
    prompt_hash = hash_prompt(prompt)
    
    print(f"Prompt: \"{prompt}\"")
    print(f"Hash: {prompt_hash}\n")
    
    # First request
    print("First request (no cache):")
    start = time.time()
    result = lumina.process(prompt)
    duration1 = time.time() - start
    cache.set(prompt_hash, result)
    print(f"  Time: {duration1:.4f}s")
    print(f"  Result: {result['output'][:60]}...")
    
    # Second request (from cache)
    print("\nSecond request (from cache):")
    start = time.time()
    cached_result = cache.get(prompt_hash)
    duration2 = time.time() - start
    print(f"  Time: {duration2:.4f}s")
    print(f"  Result: {cached_result['output'][:60]}...")
    print(f"\n✓ Speedup: {duration1/duration2:.1f}x faster with caching!")


def demo_token_counting():
    """Demonstrate token counting"""
    print_section("9. Token Usage Estimation")
    
    texts = [
        "Hello, world!",
        "This is a longer sentence with more words to count.",
        "LuminaAI v2.0 is an advanced AI system with powerful capabilities."
    ]
    
    print("Estimating token usage:\n")
    
    total_tokens = 0
    for text in texts:
        tokens = TokenCounter.count(text)
        cost = TokenCounter.estimate_cost(tokens)
        total_tokens += tokens
        
        print(f"Text: \"{text[:50]}...\"")
        print(f"  Tokens: {tokens}")
        print(f"  Est. Cost: ${cost:.6f}\n")
    
    total_cost = TokenCounter.estimate_cost(total_tokens)
    print(f"Total Tokens: {total_tokens}")
    print(f"Total Est. Cost: ${total_cost:.6f}")


def demo_session_export(lumina):
    """Demonstrate session export"""
    print_section("10. Session Management")
    
    print("Processing some tasks...")
    lumina.process("Task 1: Analyze data")
    lumina.process("Task 2: Generate report")
    
    export_path = "/tmp/lumina_demo_session.json"
    print(f"\nExporting session to: {export_path}")
    lumina.export_session(export_path)
    
    print("✓ Session exported successfully!")
    
    with open(export_path, 'r') as f:
        session_data = json.load(f)
    
    print("\nSession Summary:")
    print(f"  • Version: {session_data['version']}")
    print(f"  • Session ID: {session_data['session_id']}")
    print(f"  • Models: {len(session_data['models'])}")
    print(f"  • Timestamp: {session_data['timestamp']}")


def demo_conclusion():
    """Show conclusion"""
    print_header("🎉 Demo Complete! 🎉")
    
    print("LuminaAI v2.0 Features Demonstrated:")
    print("  ✓ System initialization and configuration")
    print("  ✓ Multi-model AI processing")
    print("  ✓ Batch processing capabilities")
    print("  ✓ Conversational assistant")
    print("  ✓ Performance monitoring")
    print("  ✓ Intelligent caching")
    print("  ✓ Token usage estimation")
    print("  ✓ Session management")
    
    print("\n" + "=" * 70)
    print("Thank you for trying LuminaAI v2.0!")
    print("Built with ❤️ using the treaai framework")
    print("=" * 70 + "\n")


def run_demo():
    """Run the complete demo"""
    try:
        demo_introduction()
        
        lumina = demo_initialization()
        demo_capabilities(lumina)
        demo_basic_processing(lumina)
        demo_model_registration(lumina)
        demo_batch_processing(lumina)
        demo_assistant(lumina)
        demo_performance_monitoring()
        demo_caching()
        demo_token_counting()
        demo_session_export(lumina)
        
        demo_conclusion()
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n\nError during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_demo()
