# Architecture RFC

## Core Decisions
1. **Hybrid Execution Model**: Combines actor model for agent isolation with dataflow for task orchestration
2. **Sharding Strategy**: Consistent hashing based on entity IDs for state distribution
3. **Consensus Mechanism**: Raft implementation for cluster coordination
4. **Backpressure Protocol**: Window-based flow control between scheduling tiers

## Design Rationale
Each decision addresses specific tradeoffs between scalability and consistency in agent workloads...