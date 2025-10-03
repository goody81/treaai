"""
LuminaAI v2.0 - Advanced AI System
Built with treaai framework

Main package for LuminaAI v2.0
"""

from luminaai_v2 import (
    LuminaAICore,
    LuminaAIAssistant,
    ModelType,
    create_lumina_ai,
    create_assistant
)

from utils import (
    Cache,
    PerformanceMonitor,
    TokenCounter,
    RateLimiter,
    hash_prompt,
    validate_config,
    load_config,
    save_config,
    format_output,
    chunk_text,
    merge_configs,
    timing_decorator
)

__version__ = "2.0.0"
__author__ = "treaai"
__all__ = [
    # Core classes
    "LuminaAICore",
    "LuminaAIAssistant",
    "ModelType",
    # Factory functions
    "create_lumina_ai",
    "create_assistant",
    # Utilities
    "Cache",
    "PerformanceMonitor",
    "TokenCounter",
    "RateLimiter",
    "hash_prompt",
    "validate_config",
    "load_config",
    "save_config",
    "format_output",
    "chunk_text",
    "merge_configs",
    "timing_decorator",
]
