"""
LuminaAI v2.0 Utilities
Helper functions and utilities for LuminaAI
"""

import hashlib
import time
from typing import Any, Dict, List, Optional, Callable
from functools import wraps
import json


class Cache:
    """Simple caching system for LuminaAI"""
    
    def __init__(self, max_size: int = 1000):
        """Initialize cache with max size"""
        self.max_size = max_size
        self.cache = {}
        self.access_times = {}
    
    def get(self, key: str) -> Optional[Any]:
        """Get item from cache"""
        if key in self.cache:
            self.access_times[key] = time.time()
            return self.cache[key]
        return None
    
    def set(self, key: str, value: Any) -> None:
        """Set item in cache"""
        if len(self.cache) >= self.max_size:
            self._evict_oldest()
        
        self.cache[key] = value
        self.access_times[key] = time.time()
    
    def _evict_oldest(self) -> None:
        """Evict oldest cache entry"""
        if not self.access_times:
            return
        
        oldest_key = min(self.access_times.items(), key=lambda x: x[1])[0]
        del self.cache[oldest_key]
        del self.access_times[oldest_key]
    
    def clear(self) -> None:
        """Clear all cache"""
        self.cache.clear()
        self.access_times.clear()


class PerformanceMonitor:
    """Monitor performance metrics for LuminaAI"""
    
    def __init__(self):
        """Initialize performance monitor"""
        self.metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_time": 0.0,
            "avg_time": 0.0
        }
    
    def record_request(self, success: bool, duration: float) -> None:
        """Record a request"""
        self.metrics["total_requests"] += 1
        
        if success:
            self.metrics["successful_requests"] += 1
        else:
            self.metrics["failed_requests"] += 1
        
        self.metrics["total_time"] += duration
        self.metrics["avg_time"] = (
            self.metrics["total_time"] / self.metrics["total_requests"]
        )
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics"""
        return self.metrics.copy()
    
    def reset(self) -> None:
        """Reset metrics"""
        self.metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_time": 0.0,
            "avg_time": 0.0
        }


def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        duration = end_time - start_time
        print(f"{func.__name__} took {duration:.4f} seconds")
        
        return result
    
    return wrapper


def hash_prompt(prompt: str) -> str:
    """
    Generate hash for a prompt (useful for caching)
    
    Args:
        prompt: Input prompt
        
    Returns:
        MD5 hash of the prompt
    """
    return hashlib.md5(prompt.encode()).hexdigest()


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate LuminaAI configuration
    
    Args:
        config: Configuration dictionary
        
    Returns:
        True if valid, False otherwise
    """
    required_keys = ["max_tokens", "temperature"]
    
    for key in required_keys:
        if key not in config:
            return False
    
    # Validate value ranges
    if not (0 <= config.get("temperature", 0) <= 2):
        return False
    
    if config.get("max_tokens", 0) <= 0:
        return False
    
    return True


def load_config(filepath: str) -> Dict[str, Any]:
    """
    Load configuration from JSON file
    
    Args:
        filepath: Path to config file
        
    Returns:
        Configuration dictionary
    """
    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}


def save_config(config: Dict[str, Any], filepath: str) -> bool:
    """
    Save configuration to JSON file
    
    Args:
        config: Configuration dictionary
        filepath: Path to save config
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False


def format_output(data: Any, format_type: str = "text") -> str:
    """
    Format output data
    
    Args:
        data: Data to format
        format_type: Output format (text, json, markdown)
        
    Returns:
        Formatted string
    """
    if format_type == "json":
        return json.dumps(data, indent=2)
    elif format_type == "markdown":
        if isinstance(data, dict):
            lines = ["```json"]
            lines.append(json.dumps(data, indent=2))
            lines.append("```")
            return "\n".join(lines)
    
    # Default text format
    return str(data)


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Split text into chunks with optional overlap
    
    Args:
        text: Input text
        chunk_size: Size of each chunk
        overlap: Overlap between chunks
        
    Returns:
        List of text chunks
    """
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    
    return chunks


def merge_configs(base_config: Dict[str, Any], 
                 override_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two configuration dictionaries
    
    Args:
        base_config: Base configuration
        override_config: Override configuration
        
    Returns:
        Merged configuration
    """
    merged = base_config.copy()
    merged.update(override_config)
    return merged


class TokenCounter:
    """Simple token counter for text"""
    
    @staticmethod
    def count(text: str) -> int:
        """
        Count approximate tokens in text
        
        Args:
            text: Input text
            
        Returns:
            Approximate token count
        """
        # Simple approximation: ~4 characters per token
        return len(text) // 4
    
    @staticmethod
    def estimate_cost(tokens: int, price_per_1k: float = 0.01) -> float:
        """
        Estimate cost for given tokens
        
        Args:
            tokens: Number of tokens
            price_per_1k: Price per 1000 tokens
            
        Returns:
            Estimated cost
        """
        return (tokens / 1000) * price_per_1k


class RateLimiter:
    """Rate limiter for API calls"""
    
    def __init__(self, max_calls: int, time_window: int = 60):
        """
        Initialize rate limiter
        
        Args:
            max_calls: Maximum calls allowed
            time_window: Time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
    
    def allow_request(self) -> bool:
        """
        Check if request is allowed
        
        Returns:
            True if allowed, False if rate limited
        """
        current_time = time.time()
        
        # Remove old calls outside time window
        self.calls = [t for t in self.calls if current_time - t < self.time_window]
        
        if len(self.calls) < self.max_calls:
            self.calls.append(current_time)
            return True
        
        return False
    
    def wait_time(self) -> float:
        """
        Calculate wait time until next request allowed
        
        Returns:
            Wait time in seconds
        """
        if not self.calls:
            return 0.0
        
        current_time = time.time()
        oldest_call = min(self.calls)
        
        wait = self.time_window - (current_time - oldest_call)
        return max(0, wait)


if __name__ == "__main__":
    # Test utilities
    print("Testing LuminaAI Utilities")
    print("=" * 60)
    
    # Test cache
    cache = Cache(max_size=3)
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    print(f"Cache get key1: {cache.get('key1')}")
    
    # Test performance monitor
    monitor = PerformanceMonitor()
    monitor.record_request(True, 0.5)
    monitor.record_request(True, 0.3)
    print(f"Performance metrics: {monitor.get_metrics()}")
    
    # Test hash
    test_prompt = "Hello, LuminaAI!"
    print(f"Prompt hash: {hash_prompt(test_prompt)}")
    
    # Test token counter
    token_count = TokenCounter.count("This is a test sentence.")
    print(f"Token count: {token_count}")
    
    print("\nUtilities test completed!")
