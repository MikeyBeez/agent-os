# Agent OS

**A Canonical Naming and Discovery System for AI Agents**

The Agent Operating System provides the fundamental infrastructure that distributed AI systems need: canonical naming, discovery, process management, and communication protocols — eliminating the chaos of magic strings and implicit dependencies.

## The Problem

Every agent framework today suffers from the same fundamental issue:

```python
# Current Reality: Magic Strings Everywhere
agent.run("search_web", "query")      # Will this work?
agent.invoke("web_search", "query")   # Or is it this?
agent.execute("searchWeb", "query")   # Or maybe this?
agent.use_tool("webSearch", "query")  # Who knows?
```

We're trying to build agent societies without the equivalent of DNS, process tables, or system calls.

## The Solution: Agent OS

Agent OS provides a true operating system foundation for AI agents with:

- **Canonical Naming System** - No more magic strings, registered discoverable entities
- **Registry & Discovery** - Find agents, tools, and protocols like DNS
- **Process Management** - Track running agents like a process table
- **Message Bus** - Reliable inter-agent communication
- **Validation & Linting** - Catch errors before runtime
- **Editor Integration** - Autocomplete and validation in your IDE

## Installation

```bash
pip install agent-os
```

## Quick Start

### Register a Tool

```python
from agent_os.registry import register

@register.tool("web_search")
class WebSearchTool:
    """Search the web for current information"""
    canonical_name = "{{tool:web_search}}"
    version = "1.2.0"
    
    def execute(self, query: str) -> List[SearchResult]:
        # Implementation
        pass
```

### Use Registered Names

```python
from agent_os.registry import resolve

# NO MORE MAGIC STRINGS
# Instead: registered, discoverable entities
results = resolve.tool("web_search").execute("AI advancements")
analysis = resolve.protocol("data_analysis").send(
    to=resolve.agent("analysis_bot"),
    data=results
)
```

### Discover Available Capabilities

```python
from agent_os import registry

# What tools are available?
available_tools = await registry.discover("tool", 
    tags=["research", "current_data"]
)

# What agents can help with analysis?
analysis_agents = await process_manager.find_agents_by_capability(
    "data_analysis"
)
```

## Core Architecture

```
~/.agent_os/
├── registry/              # The canonical naming authority
│   ├── agents/           # {{agent:research_bot}}
│   ├── tools/            # {{tool:web_search}}
│   ├── protocols/        # {{protocol:data_analysis}}
│   ├── types/            # {{type:research_result}}
│   └── resources/        # {{resource:knowledge_base}}
├── runtime/              # Running system state
│   ├── processes/        # Active agents
│   ├── connections/      # Active communication channels
│   └── resources/        # Allocated resources
└── cache/                # Discovered capabilities
    ├── tool_cache/
    └── protocol_cache/
```

## Features

### 1. Canonical Naming

```python
# Register once, use everywhere
@register.tool("web_search")
class WebSearchTool:
    canonical_name = "{{tool:web_search}}"
    version = "1.2.0"
    
# Use with confidence
tool = resolve.tool("web_search")
```

### 2. Registry & Discovery

```bash
# CLI commands
agent-os registry list tools
agent-os registry describe {{tool:web_search}}
agent-os check my_agent.py
```

### 3. Process Management

```python
from agent_os.runtime import process_manager

# Start an agent
process = await process_manager.start_agent("research_bot")

# Find agents by capability
analyzers = await process_manager.find_agent_by_capability("data_analysis")
```

### 4. Message Bus

```python
from agent_os.runtime import message_bus

# Send typed, validated messages
receipt = await message_bus.send_message(
    from_agent="research_bot",
    to_agent="analysis_bot",
    protocol="data_analysis",
    data=results
)
```

### 5. Validation & Linting

```python
# agent_os/linter catches errors
# ❌ ERROR: Use canonical name format
agent.use_tool("web_search", query)  

# ✅ CORRECT
agent.use_tool("{{tool:web_search}}", query)
```

### 6. Editor Integration

```vim
" Autocomplete canonical names
" Type {{tool: and get suggestions
" Syntax highlighting for entity references
```

## CLI Usage

```bash
# List available tools
agent-os registry list tools
# Output:
# {{tool:web_search}}      Search the web (v1.2.0)
# {{tool:code_analysis}}   Analyze code (v1.0.0)
# {{tool:file_operations}} File operations (v2.1.0)

# Describe a tool
agent-os registry describe {{tool:web_search}}
# Output:
# Name: {{tool:web_search}}
# Version: 1.2.0
# Description: Search the web for current information
# Dependencies: network_access, html_parser
# Provided by: company/agent_tools

# Check agent dependencies
agent-os check research_agent.py
# Output:
# ✅ {{tool:web_search}} (v1.2.0)
# ✅ {{tool:data_analysis}} (v1.1.0)
# ❌ {{tool:premium_search}} (license required)

# Run with validation
agent-os run --validate research_agent.py
# Output:
# Validating agent definitions...
# ✅ All tools registered
# ✅ All protocols available
# ✅ All types defined
# Starting agent system...
```

## The Philosophical Shift

Agent OS represents a fundamental rethinking of how we build AI systems:

| From | To |
|------|-----|
| Fragile Scripts | Robust Systems |
| Magic Strings | Canonical Names |
| Ad-hoc Communication | Structured Protocols |
| Implicit Dependencies | Explicit Contracts |
| Manual Coordination | Automatic Discovery |

## The Payoff

```python
# BEFORE: Brittle, magical, hard to maintain
def do_research():
    agent1.invoke("webSearch", query)       # Will this work?
    agent2.call("analyzeData", result1)     # Who knows!

# AFTER: Explicit, discoverable, reliable
def do_research():
    results = resolve.tool("web_search").execute(query)
    analysis = resolve.protocol("data_analysis").send(
        to=resolve.agent("analysis_specialist"),
        data=results
    )
    # Type-checked, registry-validated, runtime-guaranteed
```

## Development

```bash
# Clone repository
git clone https://github.com/yourusername/agent-os.git
cd agent-os

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 agent_os/

# Build documentation
cd docs && make html
```

## Project Status

**Current Version**: 0.1.0 (Alpha)

**Implemented**:
- Core registry architecture
- Basic naming system
- CLI scaffolding

**In Progress**:
- Process management system
- Message bus implementation
- Linting rules
- Editor plugins

**Planned**:
- Resource management
- Dynamic capability discovery
- Protocol negotiation
- Full editor integration (VSCode, Vim, Emacs)

## Documentation

Full documentation available at: [Documentation URL]

- [Architecture Overview](docs/architecture.md)
- [Registry System](docs/registry.md)
- [Process Management](docs/processes.md)
- [Message Bus](docs/messaging.md)
- [Linting & Validation](docs/linting.md)
- [Editor Integration](docs/editors.md)

## Contributing

Contributions welcome! This project aims to establish the fundamental infrastructure for AI agent systems.

**Areas needing help**:
- Process management implementation
- Message bus reliability
- Linter rule development
- Editor plugin development
- Documentation
- Testing

Please open an issue or PR!

## Vision

Read the full vision: [The Agent Operating System: A Vision for Canonical AI Agent Development](https://medium.com/@mbonsign/the-agent-operating-system-a-vision-for-canonical-ai-agent-development-79e8c2391f74)

We are building the foundations of AI society. Let's build them with the same rigor we applied to operating systems, networking protocols, and distributed systems. The Agent OS isn't a luxury — it's a necessity for the next generation of AI systems.

**Let's build the /etc for the mind.**

## License

MIT License - see LICENSE file for details.

## Contact

- **Author**: [Your Name]
- **Email**: [your.email@example.com]
- **Medium**: [@mbonsign](https://medium.com/@mbonsign)
- **GitHub**: [yourusername](https://github.com/yourusername)

---

*The choice is simple: continue with the current chaos of magic strings and implicit dependencies, or build a proper foundation with canonical naming and explicit contracts. The future of reliable AI systems depends on this choice.*
