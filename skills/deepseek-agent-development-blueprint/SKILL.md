---
name: deepseek-agent-development-blueprint
description: DeepSeek Agent Development Blueprint
---

# DeepSeek Agent Development Blueprint

This skill defines the autonomous behavior, system prompt, and capabilities for the agent **DeepSeek Agent Development Blueprint**.

## Source Location
Originally discovered in Rick's Downloads at: `/Users/kalivibecoding/Downloads/credit system may26/deepseek26/DeepSeek Agent Development Blueprint.md`

## 🧠 Master Agent Prompt & Capabilities

# **Architecture and Engineering Blueprint for Ultra-Intelligent Autonomous DeepSeek-V4 Agentic Systems**

## **Architectural Foundations and Scalable Memory Primitives**

The development of high-performing autonomous systems requires a fundamental alignment between high-level orchestration layers and the underlying low-level language model architecture.1 Historically, executing agentic tasks over long horizons has been hindered by exponential hardware scaling costs, GPU memory limits, and compounding context degradation.1 The DeepSeek-V4 model family, consisting of DeepSeek-V4-Pro and DeepSeek-V4-Flash, introduces architectural modifications specifically engineered to resolve these bottlenecks, providing a scalable foundation for highly complex agentic operations.1  
DeepSeek-V4-Pro represents a flagship Mixture-of-Experts (MoE) configuration deploying 1.6 trillion total parameters, of which only 49 billion are active per token.3 This establishes a 30:1 compression ratio between total and active parameters, minimizing active computational overhead.3 Its lightweight sibling, DeepSeek-V4-Flash, operates with 284 billion total parameters, activating 13 billion per token.3 Both models support a native 1,000,000-token context window, utilizing a novel attention framework to overcome the memory bottlenecks of long-context retrieval.3  
Rather than relying on standard dense attention, DeepSeek-V4 utilizes a Hybrid Attention Architecture that alternates between Compressed Sparse Attention (CSA) and a newly developed Heavily Compressed Attention (HCA) mechanism.1 In DeepSeek-V4-Pro’s 61-layer transformer stack, layers 0 and 1 implement HCA, layers 2 through 60 alternate between CSA and HCA, and the final Multi-Token Prediction (MTP) block executes sliding-window attention.1 This alternating distribution prevents capacity degradation by matching layer-specific execution patterns with optimized compression schemes.1  
At a context depth of one million tokens, the combination of CSA and HCA allows DeepSeek-V4-Pro to operate with only 27% of the single-token inference floating-point operations (FLOPs) and 10% of the KV cache memory required by its predecessor, DeepSeek-V3.2.1 The DeepSeek-V4-Flash model optimizes these parameters further, requiring only 10% of the active FLOPs and 7% of the KV cache memory.1 When compared to standard Grouped Query Attention (GQA) with 8 heads stored in ![][image1]\-bit floating-point format (BF16), the DeepSeek-V4 attention scheme compresses the absolute KV cache memory footprint to approximately 2%, effectively resolving the memory wall that historically caused long-horizon agent trajectories to halt mid-execution due to out-of-memory errors.1

\+-----------------------------------------------------------------------------+  
|                         DEEPSEEK-V4 HYBRID ATTENTION                        |  
\+-----------------------------------------------------------------------------+  
| Layer 0 \- 1   : Heavily Compressed Attention (HCA)                          |  
| Layers 2 \- 60 : Alternating CSA & HCA Layers                                |  
| Layer 61 (MTP): Sliding-Window Attention Only                               |  
\+-----------------------------------------------------------------------------+  
|                          ENGRAM CONDITIONAL MEMORY                          |  
\+-----------------------------------------------------------------------------+  
| DRAM Hash-Lookup (Syntax, Rules, Entities) \-\> O(1) Static Retrieval         |  
| GPU HBM Active Compute (Attention & Dynamic Inference)                      |  
\+-----------------------------------------------------------------------------+

Signal propagation and stability across these deep transformer layers are maintained by Manifold-Constrained Hyper-Connections (mHC), a mathematical framework that reinforces conventional residual pathways while preserving model expressivity.2 The models are pre-trained on more than 32 trillion diverse tokens using the Muon optimizer to accelerate convergence.2 Post-training utilizes a two-stage pipeline: first, the independent cultivation of domain-specific experts through Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) via Group Relative Policy Optimization (GRPO), followed by a unified model consolidation phase via on-policy distillation.2  
A core architectural breakthrough of the DeepSeek-V4 family is the integration of Engram Conditional Memory via Scalable Lookup.6 This represents a secondary, static axis of sparsity operating alongside the dynamic routing of MoE experts.8 Engram isolates static patterns, such as syntactic structures, entity names, and API function signatures, and offloads them to a hash-based lookup table stored entirely in system DRAM.3 This allows ![][image2] pattern retrieval without executing these static structures through active GPU attention layers.3  
Empirical scaling analyses establish a U-shaped scaling relationship between MoE allocation and Engram memory parameters.8 The optimal performance split is achieved by allocating 75% of compute capacity to active GPU HBM reasoning and offloading 25% to static DRAM lookup systems.6 This architecture preserves active GPU transformer layers for complex multi-step reasoning while allowing agents to reference deep, static codebases and documentation libraries directly from cheap, local system memory.6

## **Empirical Performance Analysis and Agent Economics**

Evaluating autonomous systems requires a rigorous analysis of both model capability and operational unit economics.1 While proprietary closed-source systems maintain narrow margins in highly specialized evaluations, the open-weight paradigm represented by DeepSeek-V4 offers a dramatic cost-to-performance advantage.3

### **Master Frontier Model Comparison**

To characterize the capabilities of DeepSeek-V4, the following table evaluates the Pro and Flash variants against leading open-weight and proprietary models across core performance benchmarks and API pricing tiers.3

| Model Variant | Developer | Architectural Footprint | Context Length | MMLU-Pro Score | GPQA Diamond | SWE-bench Verified | SWE-bench Pro | LiveCodeBench | Codeforces Rating | Input Price ($/MTok) | Output Price ($/MTok) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **GPT-5.5 Pro** | OpenAI | Undisclosed | 256K | \- | \- | \- | \- | \- | \- | $30.00 | $180.00 |
| **GPT-5.5** | OpenAI | Undisclosed | 256K | 92.4% | \- | 88.7% | 58.6% | \- | \- | $5.00 | $30.00 |
| **Claude Opus 4.7** | Anthropic | Undisclosed | 1M | \- | 94.2% | 87.6% | 64.3% | \- | \- | $5.00 | $25.00 |
| **Gemini 3.1 Pro** | Google | Undisclosed | 1M | \- | 94.3% | 80.6% | \- | 91.7% | 3052 | $2.00 | $12.00 |
| **DeepSeek V4-Pro** | DeepSeek | 1.6T MoE (49B active) | 1M | 87.5% | 90.1% | 80.6% | 55.4% | 93.5% | 3206 | $1.74 | $3.48 |
| **DeepSeek V4-Flash** | DeepSeek | 284B MoE (13B active) | 1M | 86.2% | \- | \- | 52.6% | 91.6% | \- | $0.14 | $0.28 |
| **Llama 4 Maverick** | Meta | 400B MoE (17B active) | 1M | 91.8% | \- | \- | \- | \- | \- | $0.15 | $0.60 |
| **Grok 4** | xAI | Undisclosed | 2M | \- | \- | \- | \- | \- | \- | $3.00 | $15.00 |

3  
DeepSeek-V4-Pro demonstrates competitive performance in developer and coding-centric environments.4 On the LiveCodeBench programming evaluation, DeepSeek-V4-Pro scores 93.5%, outperforming Gemini 3.1 Pro's 91.7%.3 In competitive programming, DeepSeek-V4-Pro reaches a Codeforces Elo rating of 3206, establishing a strong open-weight record that surpasses proprietary systems such as GPT-5.4 (which rated at 3168\) and Gemini 3.1 Pro (which rated at 3052).3  
On SWE-bench Verified—a benchmark that directly correlates with an agent's ability to resolve real-world software issues—DeepSeek-V4-Pro matches Gemini 3.1 Pro at 80.6% resolved.3 While Claude Opus 4.7 maintains a performance advantage on SWE-bench Verified (87.6%) and GPQA Diamond (94.2%), its operational deployment costs are substantially higher.3

### **Performance Retention of the Flash Variant**

A key feature of the DeepSeek-V4 architecture is the performance retention profile of DeepSeek-V4-Flash.3 Despite operating on less than a third of the active parameter budget (13B versus 49B), DeepSeek-V4-Flash retains the vast majority of the Pro model's performance 3:

* **MMLU-Pro**: DeepSeek-V4-Flash scores 86.2% versus the Pro model's 87.5%, representing a **98.5% performance retention rate**.3  
* **LiveCodeBench**: DeepSeek-V4-Flash achieves 91.6% against the Pro model's 93.5%, a **98.0% retention rate**.3  
* **SWE-bench Pro**: DeepSeek-V4-Flash resolves 52.6% of tasks compared to the Pro model's 55.4%, a **95.0% retention rate**.3

This high retention rate makes DeepSeek-V4-Flash a highly practical, cost-effective target for high-throughput, latency-sensitive agent deployments.3  
To further validate V4-Pro's utility in real-world agent environments, the model was subjected to specialized agent-oriented benchmarks.4 The evaluations confirm that the model's architectural optimizations directly improve planning and execution capabilities 4:

* **Terminal Bench 2.0**: Scores 67.9% in maximum thinking mode, validating the agent's ability to handle complex bash prompts and operating system interventions.4  
* **MCPAtlas Public**: Scores 73.6% in maximum thinking mode, which represents a leading open-source score for tool discovery and execution.4  
* **BrowseComp**: Scores 83.4% in maximum thinking mode, demonstrating stable navigation and data extraction over multi-turn web browsing sessions.4  
* **Toolathlon**: Scores 51.8% in maximum thinking mode, establishing its ability to dynamically select, configure, and execute a sequence of API tools.4

### **DeepSeek-V4 Deep Pricing Structure**

To maximize operational efficiency, DeepSeek implements a multi-tiered pricing model for the V4 API, incorporating off-peak schedules and cache hit discounts.3

| Model Tier | Input Price ($/MTok) | Output Price ($/MTok) | Cached Input Price ($/MTok) | Off-Peak Input ($/MTok) | Off-Peak Output ($/MTok) | Off-Peak Cached ($/MTok) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **DeepSeek-V4-Pro** | $1.74 | $3.48 | $0.17 | $0.87 | $1.74 | $0.09 |
| **DeepSeek-V4-Flash** | $0.14 | $0.28 | $0.014 | $0.07 | $0.14 | $0.007 |

3  
The off-peak pricing windows (active from 16:30 to 00:30 GMT) cut execution costs in half.3 The 90% discount applied to cached inputs is particularly critical for long-horizon agent systems.3 In multi-turn workflows where the entire conversation history, static codebases, and system rules are continually re-evaluated, caching ensures that subsequent steps only incur the cost of new tokens, minimizing the compounding cost of long context windows.1

## **Mathematical Underpinnings of Self-Evolution: GRPO and Policy Alignment**

A primary challenge in deploying autonomous agents is the development of robust, multi-step problem-solving capabilities without relying on massive, human-labeled instruction datasets.10 DeepSeek addresses this through Group Relative Policy Optimization (GRPO), a reinforcement learning framework that incentivizes logical progression and self-correction directly within the model's weights.10  
Traditional reinforcement learning frameworks, such as Proximal Policy Optimization (PPO), rely on a dual-model architecture comprising a policy model (actor) and a value model (critic).10 The critic model estimates the value function to establish a baseline for advantage calculations, a process that can double the active GPU memory requirement during training.10 GRPO eliminates the critic network entirely.12 Instead of estimating absolute state values, GRPO samples a group of candidate outputs for any given query and calculates relative advantages within that group.10 This critic-free framework reduces overall training memory and computational overhead by up to 50%.12

\+---------------------------------------------------------------------------------+  
|                       GRPO POLICY ADVANTAGE COMPUTATION                         |  
\+---------------------------------------------------------------------------------+  
| Query (q) \--\> Generate Group \[o\_1, o\_2,..., o\_G\] via Policy \\pi\_\\theta         |  
|                                                                                 |  
|                  \+-----------------------------------------+                    |  
|                  |  Evaluate Rewards \[r\_1, r\_2,..., r\_G\]  |                    |  
|                  \+-----------------------------------------+                    |  
|                                       |                                         |  
|                                       v                                         |  
|                 Calculate Advantage: A\_i \= (r\_i \- mean) / std                   |  
|                                       |                                         |  
|                                       v                                         |  
|                      Update Policy Weights \\pi\_\\theta                           |  
\+---------------------------------------------------------------------------------+

Let ![][image3] be the input query. The policy model ![][image4] generates a group of ![][image5] outputs:  
![][image6]  
Each candidate output ![][image7] is evaluated by a reward function, yielding a scalar reward ![][image8].10 The advantage ![][image9] for each candidate is computed as:  
![][image10]  
The policy is then updated using the advantage score, driving the model to generate the highest-rated candidate in future iterations.10 This comparative optimization allows the model to explore multiple solution pathways and self-correct when intermediate steps fail.11  
To prevent the model's policy from degrading during early, unstable reinforcement learning stages, a cold-start fine-tuning phase is applied using curated, structured deliberation data.11 In contrast to DeepSeek-R1-Zero, which encountered readability issues and language mixing (e.g., generating English analytical steps under a Chinese prompt), the cold-start data formats output sequences as:  
![][image11]  
This format structure forces a separation between intermediate, analytical thought processes and the final user-facing summary, improving overall readability.13  
To enforce logical rigor, two types of reward models are deployed during the GRPO training loop:

1. **Rule-Based Verification**: For mathematical tasks and software engineering, rule-based reward scripts verify correctness directly.10 Mathematical proofs are checked by parsing the final answer wrapped in LaTeX ![][image12] notation.14 Coding implementations are compiled and executed in sandboxed test-runners, with rewards assigned based on unit test pass rates.10  
2. **Language Consistency Penalties**: To resolve language mixing during multi-turn deliberations, a linguistic penalty reward is calculated based on the proportion of target-language tokens in the deliberation stream.11 Adding this penalty slightly reduces peak mathematical performance but ensures readable, linguistically aligned outputs.13

## **API Configuration and Deliberation State Control**

To support different speed, cost, and complexity requirements, the DeepSeek-V4 API exposes three deliberation modes that control the depth of the internal thought trace.4

### **Deliberation Tiers and Latency Profiles**

* **Non-think Mode**: Disables internal deliberation chains entirely, returning direct outputs.4 This mode is optimized for low-latency, deterministic tasks like JSON format conversion, key-value extraction, and one-sentence summarization.4  
* **Think High Mode**: Activates the deliberation engine to construct a step-by-step verification trace within \<think\>...\</think\> blocks prior to emitting the final answer.15 This mode provides a balance of cost and logic for tasks like interactive code debugging, local script generation, and immediate planning.15  
* **Think Max Mode**: Configures the deliberation engine for deep analysis, directing the model to explore multiple logical pathways and run self-verification steps before committing to an output.2 It requires a minimum context window of 384,000 tokens and is optimized for complex refactors, mathematical proofs, and long-horizon agent trajectories.1

### **API Payload Specifications**

API requests are configured using a nested thinking object inside the extra\_body parameter and a top-level reasoning\_effort string.15

#### **Non-think Mode Payload**

To disable the deliberation engine, the reasoning\_effort parameter is omitted from the request body entirely to prevent validation errors, and thinking.type is explicitly set to "disabled".4

JSON  
{  
  "model": "deepseek-v4-flash",  
  "messages":,  
  "extra\_body": {  
    "thinking": {  
      "type": "disabled"  
    }  
  }  
}

#### **Think High Mode Payload**

To enable the standard deliberation chain, thinking.type is set to "enabled" and reasoning\_effort is set to "high".15

JSON  
{  
  "model": "deepseek-v4-pro",  
  "messages":,  
  "reasoning\_effort": "high",  
  "extra\_body": {  
    "thinking": {  
      "type": "enabled"  
    }  
  }  
}

#### **Think Max Mode Payload**

To enable maximum deliberation depth, reasoning\_effort is set to "max".15

JSON  
{  
  "model": "deepseek-v4-pro",  
  "messages": \[  
    {  
      "role": "user",  
      "content": "Analyze this codebase and identify race conditions under heavy concurrent load."  
    }  
  \],  
  "reasoning\_effort": "max",  
  "extra\_body": {  
    "thinking": {  
      "type": "enabled"  
    }  
  }  
}

### **Critical Client Integration Protocols**

To prevent API failures (such as HTTP 400 Bad Request) when deploying DeepSeek-V4 within autonomous agent loops, three integration properties must be configured in the client-side API configuration layer 16:

* **supportsToolChoice: false**: The DeepSeek-V4 thinking modes reject the explicit tool\_choice parameter.16 The client must allow the model to select tools implicitly from the system prompt or provided tool array.16  
* **requiresReasoningContentForToolCalls: true**: When reconstructing conversational histories that span multiple turns, the client must preserve the exact \<think\> token content emitted by the model.16 Omitting the thinking logs between tool execution turns breaks context verification and causes API validation failures.16  
* **requiresAssistantContentForToolCalls: true**: Assistant messages that contain tool calls must not have null or empty content fields.16 A placeholder string or the original thought trace must be supplied within the text body.16

Furthermore, the DeepSeek-V4 API introduces **Interleaved Thinking Across Tool Calls**.1 Unlike traditional conversational LLMs that flush their internal deliberation states at user message boundaries, DeepSeek-V4 retains the accumulated thinking history across multiple rounds of tool execution.1 This allows the agent to maintain a single, coherent analytical path across dozens of sequential tool calls and environment feedback loops.1

### **Terminal Coding Agent Configurations**

For terminal-based developer agents (such as Oh My Pi or Deep Code), custom integration configurations are necessary to ensure stable execution.16

#### **Custom models.yml for Oh My Pi (v14.5+)**

YAML  
providers:  
  deepseek:  
    baseUrl: "https://api.deepseek.com"  
    api: "openai-completions"  
    apiKey:...\[source\](https://api-docs.deepseek.com/quick\_start/agent\_integrations/oh\_my\_pi)

16

#### **Custom settings.json for Deep Code CLI**

JSON  
{  
  "env": {  
    "MODEL": "deepseek-v4-pro",  
    "BASE\_URL": "https://api.api.deepseek.com",  
    "API\_KEY": "sk-your-key-here",  
    "thinkingEnabled": true,  
    "reasoningEffort": "max",  
    "webSearchTool": true  
  }  
}

17

## **Native Tool-Calling Schemas, Parsers, and the DSec Sandbox**

DeepSeek-V4 introduces a native, XML-based tool-calling format wrapped in the |DSML| special token, replacing standard JSON-in-string tool-calling formats.1 This design reduces structural syntax errors and string escaping failures that commonly occur when models attempt to nest JSON structures within text fields.1 The model wraps tools using \<｜DSML｜tool\_calls\> blocks, a transition from the \<｜DSML｜function\_calls\> markers used in DeepSeek-V3.2.18

### **XML-Based Tool-Call Example**

XML  
\<｜DSML｜tool\_calls\>  
\<invoke name\="execute\_terminal"\>  
\<parameter name\="command" string\="true"\>grep \-rn "TODO: race condition"./src\</parameter\>  
\</invoke\>  
\</｜DSML｜tool\_calls\>

1  
The schema uses the string="true" attribute to pass raw text arguments directly without escaping, while passing structured objects as JSON with string="false".1 This prevents common parsing errors associated with boolean, numeric, and nested object fields.1

### **Fault-Tolerant Python Parser Implementation**

When deploying DeepSeek-V4 through custom local endpoints, serving backends may occasionally leak raw DSML markers directly into the text stream instead of normalizing them into structured API fields.19 The following production-grade Python class implements a fault-tolerant parser capable of handling both Unicode fullwidth delimiters and ASCII pipe boundaries, extracting the arguments into clean structured schemas.19

Python  
import re  
import json  
import xml.etree.ElementTree as ET  
from typing import List, Dict, Any, Optional

class DeepSeekV4ToolParser:  
    """  
    Production parser designed to parse DeepSeek-V4 DSML/XML tool calls.  
    Handles both Unicode fullwidth and standard ASCII delimiters.  
    """  
    def \_\_init\_\_(self):  
        \# Regex to capture content inside Unicode or ASCII DSML tool call tags  
        self.dsml\_pattern \= re.compile(  
            r"(?:\<｜DSML｜tool\_calls\>|\<\\|DSML\\|tool\_calls\>)(.\*?)(?:\<｜DSML｜\>|\<\\|DSML\\|\>|.\*|$)",   
            re.DOTALL  
        )

    def parse(self, raw\_content: str) \-\> List\]:  
        tool\_calls \=  
        if not raw\_content:  
            return tool\_calls

        \# Check for presence of DSML tags  
        match \= self.dsml\_pattern.search(raw\_content)  
        if not match:  
            \# Fallback check for raw XML invoke blocks without the parent DSML container  
            xml\_content \= raw\_content  
        else:  
            xml\_content \= match.group(1).strip()

        \# Wrap in temporary root element to handle multiple sibling invoke tags  
        wrapped\_xml \= f"\<root\>{xml\_content}\</root\>"  
          
        try:  
            root \= ET.fromstring(wrapped\_xml)  
            for invoke in root.findall("invoke"):  
                name \= invoke.get("name")  
                if not name:  
                    continue  
                  
                parameters \= {}  
                for param in invoke.findall("parameter"):  
                    p\_name \= param.get("name")  
                    is\_string \= param.get("string", "true").lower() \== "true"  
                    p\_text \= param.text.strip() if param.text else ""  
                      
                    if p\_name:  
                        if is\_string:  
                            parameters\[p\_name\] \= p\_text  
                        else:  
                            try:  
                                parameters\[p\_name\] \= json.loads(p\_text)  
                            except json.JSONDecodeError:  
                                parameters\[p\_name\] \= p\_text  \# Fallback to raw string  
                  
                tool\_calls.append({  
                    "id": f"call\_{hash(name \+ json.dumps(parameters)) % 10\*\*8}",  
                    "type": "function",  
                    "function": {  
                        "name": name,  
                        "arguments": json.dumps(parameters)  
                    }  
                })  
        except ET.ParseError:  
            \# Fallback regex-based parser in case of incomplete or malformed XML streaming  
            tool\_calls \= self.\_regex\_fallback\_parse(xml\_content)  
              
        return tool\_calls

    def \_regex\_fallback\_parse(self, xml\_content: str) \-\> List\]:  
        calls \=  
        invoke\_blocks \= re.findall(r'\<invoke name="(\[^"\]+)"\\s\*\>(.\*?)\</invoke\>', xml\_content, re.DOTALL)  
        for name, param\_block in invoke\_blocks:  
            parameters \= {}  
            params \= re.findall(r'\<parameter name="(\[^"\]+)"(?: string="(\[^"\]+)")?\\s\*\>(.\*?)\</parameter\>', param\_block, re.DOTALL)  
            for p\_name, is\_str, p\_val in params:  
                is\_string \= is\_str.lower()\!= "false" if is\_str else True  
                clean\_val \= p\_val.strip()  
                if is\_string:  
                    parameters\[p\_name\] \= clean\_val  
                else:  
                    try:  
                        parameters\[p\_name\] \= json.loads(clean\_val)  
                    except json.JSONDecodeError:  
                        parameters\[p\_name\] \= clean\_val  
            calls.append({  
                "id": f"call\_regex\_{hash(name \+ json.dumps(parameters)) % 10\*\*8}",  
                "type": "function",  
                "function": {  
                    "name": name,  
                    "arguments": json.dumps(parameters)  
                }  
            })  
        return calls

### **DeepSeek Elastic Compute (DSec) Sandbox**

For executing untrusted or autonomous code steps, the agent relies on the DeepSeek Elastic Compute (DSec) framework.1 Written in Rust, DSec exposes a unified Python SDK that manages execution sandboxes across four distinct virtualization tiers: simple function calling, isolated container runtimes, microVMs (powered by Firecracker), and full QEMU virtual machine substrates.1

\+-----------------------------------------------------------------------------+  
|                     DSEC VIRTUALIZATION & STORAGE STACK                     |  
\+-----------------------------------------------------------------------------+  
| Python SDK Layer \-\> Unified Interface for Containers & VM Substrates        |  
|                                                                             |  
|                   \+---------------------------------------+                 |  
|                   | Layered 3FS Storage System            |                 |  
|                   | \- Dynamic chunk-streaming of images   |                 |  
|                   \+---------------------------------------+                 |  
|                                       |                                     |  
|                                       v                                     |  
|                 MicroVM (Firecracker) / Full VM (QEMU)                      |  
|                                       |                                     |  
|                                       v                                     |  
|                 Preemption-Safe Trajectory Replay Logs                      |  
\+-----------------------------------------------------------------------------+

DSec addresses three core system challenges for autonomous agent execution:

* **Layered 3FS Storage System**: Standard agent rollouts are delayed by container cold starts.1 DSec integrates with DeepSeek's high-performance 3FS file system, loading microVM and container images instantly using dynamic chunk streaming.1  
* **Preemption-Safe Trajectory Replay**: In highly distributed clusters, node preemptions can interrupt agent runs.1 DSec records every environment mutation and tool-execution state, enabling the agent loop to resume from failure states without re-running expensive or irreversible tool actions.1  
* **Unified Abstraction API**: The agent training harness targets a single API, allowing the system to scale from simple mock functions up to complex sandboxed environments with full operating system access.1

## **Local Deployment, Serving Optimization, and Kernel-Level Acceleration**

Deploying DeepSeek-V4 models locally requires maximizing hardware capabilities through dedicated, low-level libraries and inference engines.22

### **Low-Level Library Infrastructure**

The official DeepSeek GitHub organization hosts specialized repositories that bypass standard PyTorch abstractions to execute high-performance kernels directly on GPU and network hardware 21:

* **DeepEP (v2)**: An efficient expert-parallel communication library designed for NVLink and NVSHMEM environments.21 DeepEP v2 supports high-speed expert dispatch, token routing, and context-parallel operations.24 It is optimized for both FP8 and FP4 precision, allowing overlapping communication and computation during the forward pass.24  
* **DeepGEMM**: A library of clean and efficient FP8 GEMM kernels with fine-grained scaling.21 DeepGEMM implements tile-wise and block-wise quantization methods to reduce the memory bandwidth bottleneck of large MoE models on NVIDIA Hopper GPUs.26 It optimizes execution by compiling custom scaling kernels directly into CUDA workloads, bypassing traditional PyTorch-to-CUDA orchestration overhead.27  
* **FlashMLA**: High-performance kernels specifically optimized for Multi-Head Latent Attention (MLA), accelerating decoding speeds under high concurrency.21  
* **TileKernels**: A collection of GPU kernels written in TileLang, providing highly fused, memory-efficient operations.21  
* **DualPipe**: A bidirectional pipeline parallelism algorithm that optimizes computation-communication overlap during the training and serving of massive MoE models.21  
* **3FS**: A high-performance distributed file system designed to handle the high IOPS and data throughput requirements of massive AI workloads.1

### **SGLang Support and Core Roadmap**

For local serving, SGLang (v0.4+) provides significant throughput advantages over vLLM due to its custom integration of DeepSeek-V4's architectural features 22:

* **RadixAttention**: SGLang automatically manages the KV cache as a dynamic tree structure.28 For multi-agent workflows where multiple agents share common system prompts, API schemas, and code histories, RadixAttention identifies the overlapping prefixes, storing them once and serving them instantly from the cache.28 This reduces Time-to-First-Token (TTFT) by up to 29% under concurrent loads.28  
* **Expert-Parallel Load Balancing (EPLB)**: Fixes optimal GPU mapping for MoE routing layers, preventing hot-spotting on specific cards under skewed prompt weights.24  
* **Marlin & CUTLASS Implementations**: Day-0 PRs implement a W4A16 quantized Marlin backend and CUTLASS SM90 MXFP4 MoE kernels, enabling high-speed local inference under compressed precision weights.24

### **Explicit Local Serving Execution Commands**

#### **Serving DeepSeek-V4-Flash on a Single H100 GPU (SGLang)**

For developers deploying the Flash model on a single 80GB card, use the following SGLang command to launch an OpenAI-compatible endpoint 29:

Bash  
python3 \-m sglang.launch\_server \\  
    \--model-path deepseek-ai/DeepSeek-V4-Flash \\  
    \--tp-size 1 \\  
    \--context-length 131072 \\  
    \--mem-fraction-static 0.90 \\  
    \--enable-torch-compile \\  
    \--served-model-name deepseek-v4-flash \\  
    \--trust-remote-code \\  
    \--port 30000

29

* \--tp-size 1: Sets tensor parallelism to 1, utilizing a single GPU.29  
* \--context-length 131072: Caps the active context window to 128K to optimize VRAM allocation.29  
* \--mem-fraction-static 0.90: Allocates 90% of available VRAM to static model weights and the KV cache.29  
* \--enable-torch-compile: Compiles the execution graph, increasing overall throughput by 10% to 20% on Hopper architectures.29

#### **Serving DeepSeek-V4-Flash on Multi-GPU Clusters (vLLM)**

For higher concurrency workloads, use vLLM to split the Flash model across two GPUs 30:

Bash  
python3 \-m vllm.entrypoints.openai.api\_server \\  
    \--model deepseek-ai/DeepSeek-V4-Flash \\  
    \--tensor-parallel-size 2 \\  
    \--max-model-len 1048576 \\  
    \--dtype auto \\  
    \--enable-prefix-caching \\  
    \--port 8000

30

* \--tensor-parallel-size 2: Splits attention and linear layers across two H100 GPUs.23  
* \--max-model-len 1048576: Activates the full 1-million-token context window.30  
* \--enable-prefix-caching: Enables automatic prefix caching to accelerate multi-turn conversation steps.30

#### **Serving DeepSeek-V4-Pro on an 8x H100 SXM Node (vLLM)**

For enterprise-grade deployments of the 1.6T Pro model, split the model across an 8-GPU node using tensor and expert parallelism 23:

Bash  
vllm serve deepseek-ai/DeepSeek-V4-Pro \\  
    \--tensor-parallel-size 4 \\  
    \--enable-expert-parallel \\  
    \--dtype fp8 \\  
    \--max-model-len 524288 \\  
    \--gpu-memory-utilization 0.95 \\  
    \--host 0.0.0.0 \\  
    \--port 8000

23

* \--tensor-parallel-size 4: Distributes the dense attention layers across 4-GPU sub-groups.23  
* \--enable-expert-parallel: Activates expert parallelism, distributing the 256 MoE experts across all 8 GPUs.10  
* \--gpu-memory-utilization 0.95: Optimizes VRAM allocation by reserving 95% of active memory.23

## **Multi-Agent Orchestration Patterns and State Synchronization**

When building multi-agent systems, selecting the right orchestration framework is critical for performance and reliability.31

### **Multi-Agent Framework Evaluation**

The following table compares the structural patterns, capabilities, and reliability characteristics of the five primary agent frameworks deployed in enterprise environments.31

| Framework | Orchestration Pattern | Long-Term State Management | MCP Integration Maturity | Key Operational Strength | Main Reliability Blocker |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **LangChain / LangGraph** | Graph-Based State Machines | Central Persistence & Time-Travel Hooks | Highly Mature (Native Client) | Fine-grained control over execution steps and retries | High implementation complexity and custom code overhead |
| **LlamaIndex** | RAG-First Data Pipelines | Vector / Graph Database Indexing Layers | Mature (Retriever Abstractions) | Structured document intelligence and contextual retrieval | Weak native multi-agent collaboration primitives |
| **CrewAI** | Role-Playing Collaborative Teams | Shared In-Memory State & Task Passing | Practical & Explicit | Natural modeling of business tasks and human teams | Weak dynamic branching and complex retry logic |
| **AutoGen (AG2)** | Conversation-First Message Flow | Event-Driven Message Brokers | Extensible Runtime Modules | Isolated write-execute-debug code iteration loops | Poor policy enforcement and structural sequence tracking |
| **BeeAI** | Hybrid Python / TypeScript Runtimes | Distributed Memory & Remote State Pools | Native Support | Consistent execution across Granites and Llama 3 models | Smaller open-source community ecosystem |

31

### **The Multi-Agent Memory Silo Problem**

A primary engineering challenge in multi-agent systems is the **Multi-Agent Memory Silo Problem**.31 Within role-playing frameworks like CrewAI, agents share a short-term, task-level memory pool.31 However, once tasks are divided across separate groups, these memory boundaries become siloed.31  
For example, if a "procurement agent team" and a "finance agent team" both reason about an overlapping concept like a "cost center," their internal representations can drift during long-context execution.31 This semantic drift leads to conflicting output schemas, tool execution failures, and execution loops.31 Resolving this requires a global, shared context layer managed outside the individual agent frameworks.31

\+-----------------------------------------------------------------------------+  
|                HYBRID STATE GRAPH & ORCHESTRATION ARCHITECTURE              |  
\+-----------------------------------------------------------------------------+  
|                                                                             |  
|                       LANGGRAPH (Top-Level Controller)                      |  
|                  Tracks Global State, Branching Logic & Human Audits        |  
|                                       |                                     |  
|         \+-----------------------------+-----------------------------+       |  
|         |                                                           |       |  
|         v                                                           v       |  
|   CREWAI (Workflow Nodes)                               AutoGen (Code Nodes) |  
|   Coordinates Role-Based Multi-Step                     Manages Write-Run-  |  
|   Research, Verification & Writing                      Debug Execution Loops |  
|                                                                             |  
\+-----------------------------------------------------------------------------+

### **The Hybrid Orchestration Solution**

To resolve the memory silo problem while maximizing agent performance, modern enterprise architectures deploy a hybrid, multi-framework orchestration stack 34:

1. **LangGraph** acts as the top-level orchestrator, managing global state persistence, cross-agent routing policies, error recovery, and human-in-the-loop validation checkpoints.31  
2. **CrewAI** is embedded within specific LangGraph nodes to coordinate structured, role-based sub-tasks (e.g., executing a sequential research-write-review pipeline).34  
3. **AutoGen** is instantiated within isolated execution nodes to manage autonomous code-generation, shell compilation, and runtime debugging cycles.34

Standardized communication across these distinct frameworks is maintained using the Model Context Protocol (MCP), ensuring consistent tool schemas, data definitions, and resource states across the entire system.31

## **Synthesis and Strategic Recommendations**

The combination of DeepSeek-V4's architectural modifications, the GRPO reinforcement learning framework, and advanced orchestration patterns provides a powerful template for building ultra-intelligent, autonomous agent systems.1 Based on the technical specifications and performance evaluations detailed in this report, developers should implement the following strategic recommendations 6:

### **Dynamic Inference Model Routing**

To optimize both cost and latency, implement a dynamic routing policy at the gateway layer 4:

* Use **DeepSeek-V4-Flash in Non-think Mode** for routine tasks like JSON format parsing, schema extraction, and immediate key-value lookups.4  
* Use **DeepSeek-V4-Flash in Think High Mode** for standard multi-step tasks, tool orchestration, and initial code generation, leveraging the Flash variant's 98% performance retention.3  
* Escalate to **DeepSeek-V4-Pro in Think Max Mode** only for complex logic tasks like multi-file codebase refactoring, security vulnerability analysis, and hard algorithmic mathematical modeling.4

### **Active Prefix Caching Design**

To maximize prefix caching hits and minimize token costs, restructure agent prompts to place static components at the beginning of payloads 28:

* Consolidate system instructions, role identities, task guidelines, and tool definitions into a single prefix block, ensuring this block remains identical across all turns of a conversation.28  
* Append dynamic parameters (such as temporary outputs, user messages, and runtime environment feedback) strictly at the end of the prompt payload.28  
* This structure allows serving engines to retrieve the cached attention states of static components instantly, avoiding costly re-computation on subsequent turns.28

### **Low-Level Memory Offloading**

When deploying locally under constrained VRAM environments, leverage DeepSeek-V4’s Engram architecture.6 Ensure that static syntax patterns, system rules, and API definitions are offloaded to system DRAM, reserving high-speed GPU HBM strictly for active context processing and dynamic MoE expert routing.6

### **Strict Sandboxed Isolation**

Never execute agentic tool calls directly on host infrastructure or within production clusters.32 Implement a multi-tiered security model for DSec:

* Configure **Function Calling** and mock layers for local development and early-stage testing.1  
* Implement **Docker Containers** for verified third-party API integration layers.1  
* Enforce isolated **Firecracker MicroVMs** with read-only root filesystems and constrained memory limits for executing unverified code, terminal commands, or shell scripts generated by the agent.1 Ensure that all network traffic is routed through secure outbound proxies and audit trails are persisted for compliance verification.32

#### **Works cited**

1. DeepSeek-V4: a million-token context that agents can actually use \- Hugging Face, accessed May 25, 2026, [https://huggingface.co/blog/deepseekv4](https://huggingface.co/blog/deepseekv4)  
2. deepseek-ai/DeepSeek-V4-Pro \- Hugging Face, accessed May 25, 2026, [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)  
3. DeepSeek V4 Preview: The Complete 2026 Guide ... \- O-mega.ai, accessed May 25, 2026, [https://o-mega.ai/articles/deepseek-v4-preview-the-complete-2026-guide](https://o-mega.ai/articles/deepseek-v4-preview-the-complete-2026-guide)  
4. DeepSeek V4 AI Model Details: Full Specs & Capabilities (2026) \- Framia Pro, accessed May 25, 2026, [https://framia.pro/page/en-US/news/deepseek-v4-ai-model-details](https://framia.pro/page/en-US/news/deepseek-v4-ai-model-details)  
5. DeepSeek V4 Pro for Local Vulnerability Discovery, What Actually Works \- Penligent, accessed May 25, 2026, [https://www.penligent.ai/hackinglabs/es/deepseek-v4-pro-for-local-vulnerability-discovery-what-actually-works/](https://www.penligent.ai/hackinglabs/es/deepseek-v4-pro-for-local-vulnerability-discovery-what-actually-works/)  
6. DeepSeek V4 Targets Coding Dominance with Mid-February Launch \- Introl, accessed May 25, 2026, [https://introl.com/blog/deepseek-v4-february-2026-coding-model-release](https://introl.com/blog/deepseek-v4-february-2026-coding-model-release)  
7. deepseek-ai / deepseek-v4-pro \- NVIDIA API Documentation, accessed May 25, 2026, [https://docs.api.nvidia.com/nim/reference/deepseek-ai-deepseek-v4-pro](https://docs.api.nvidia.com/nim/reference/deepseek-ai-deepseek-v4-pro)  
8. GitHub \- deepseek-ai/Engram: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models : r/LocalLLaMA \- Reddit, accessed May 25, 2026, [https://www.reddit.com/r/LocalLLaMA/comments/1qb034t/github\_deepseekaiengram\_conditional\_memory\_via/](https://www.reddit.com/r/LocalLLaMA/comments/1qb034t/github_deepseekaiengram_conditional_memory_via/)  
9. DeepSeek V4 Preview Release, accessed May 25, 2026, [https://api-docs.deepseek.com/news/news260424](https://api-docs.deepseek.com/news/news260424)  
10. DeepSeek R1 and R1-Zero Explained \- The Hundred-Page Language Models Book, accessed May 25, 2026, [https://thelmbook.com/articles/\#\!./DeepSeek-R1.md](https://thelmbook.com/articles/#!./DeepSeek-R1.md)  
11. Understanding DeepSeek R1—A Reinforcement Learning-Driven Reasoning Model, accessed May 25, 2026, [https://kili-technology.com/blog/understanding-deepseek-r1](https://kili-technology.com/blog/understanding-deepseek-r1)  
12. DeepSeek R1: Efficient Reinforcement Learning with GRPO \- DataOps Labs, accessed May 25, 2026, [https://blog.dataopslabs.com/deepseek-r1-efficient-reinforcement-learning-with-grpo](https://blog.dataopslabs.com/deepseek-r1-efficient-reinforcement-learning-with-grpo)  
13. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning, accessed May 25, 2026, [https://arxiv.org/html/2501.12948v1](https://arxiv.org/html/2501.12948v1)  
14. Detailed explanation of DeepSeek-R1 method: pure reinforcement learning and self-evolving behavior | by Xupeng Wang | Medium, accessed May 25, 2026, [https://medium.com/@marvelous\_catawba\_otter\_200/detailed-explanation-of-deepseek-r1-method-pure-reinforcement-learning-and-self-evolving-behavior-dced3a31e53a](https://medium.com/@marvelous_catawba_otter_200/detailed-explanation-of-deepseek-r1-method-pure-reinforcement-learning-and-self-evolving-behavior-dced3a31e53a)  
15. DeepSeek V4 API Tutorial: Building a Thinking Mode Arena ..., accessed May 25, 2026, [https://www.datacamp.com/tutorial/deepseek-v4-api-tutorial](https://www.datacamp.com/tutorial/deepseek-v4-api-tutorial)  
16. Using DeepSeek with Oh My Pi, accessed May 25, 2026, [https://api-docs.deepseek.com/quick\_start/agent\_integrations/oh\_my\_pi](https://api-docs.deepseek.com/quick_start/agent_integrations/oh_my_pi)  
17. Integrate with Deep Code \- DeepSeek API Docs, accessed May 25, 2026, [https://api-docs.deepseek.com/quick\_start/agent\_integrations/deepcode](https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode)  
18. deepseekv4\_tool\_parser \- vLLM, accessed May 25, 2026, [https://docs.vllm.ai/en/latest/api/vllm/tool\_parsers/deepseekv4\_tool\_parser/](https://docs.vllm.ai/en/latest/api/vllm/tool_parsers/deepseekv4_tool_parser/)  
19. \[Bug\]: Tool calls not parsed correctly with DeepSeek-V4 · Issue \#15453 · NousResearch/hermes-agent \- GitHub, accessed May 25, 2026, [https://github.com/NousResearch/hermes-agent/issues/15453](https://github.com/NousResearch/hermes-agent/issues/15453)  
20. DeepSeek V4 Pro / V4 Flash on NVIDIA NIM: streaming tool calls do not continue in Claude Code / Anthropic-compatible agent workflow, accessed May 25, 2026, [https://forums.developer.nvidia.com/t/deepseek-v4-pro-v4-flash-on-nvidia-nim-streaming-tool-calls-do-not-continue-in-claude-code-anthropic-compatible-agent-workflow/368085](https://forums.developer.nvidia.com/t/deepseek-v4-pro-v4-flash-on-nvidia-nim-streaming-tool-calls-do-not-continue-in-claude-code-anthropic-compatible-agent-workflow/368085)  
21. DeepSeek \- GitHub, accessed May 25, 2026, [https://github.com/deepseek-ai](https://github.com/deepseek-ai)  
22. LLM Serving: Ollama vs vLLM vs TGI | Guides \- Clore.ai, accessed May 25, 2026, [https://docs.clore.ai/guides/comparisons/llm-serving-comparison](https://docs.clore.ai/guides/comparisons/llm-serving-comparison)  
23. Deploy DeepSeek V4 on GPU Cloud: MoE Inference with vLLM and Expert Parallelism, accessed May 25, 2026, [https://www.spheron.network/blog/deploy-deepseek-v4-gpu-cloud/](https://www.spheron.network/blog/deploy-deepseek-v4-gpu-cloud/)  
24. DeepSeek V4 Roadmap \#23602 \- sgl-project/sglang \- GitHub, accessed May 25, 2026, [https://github.com/sgl-project/sglang/issues/23602](https://github.com/sgl-project/sglang/issues/23602)  
25. deepseek-ai/DeepSeek-V3 \- GitHub, accessed May 25, 2026, [https://github.com/deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)  
26. 1 Introduction \- arXiv, accessed May 25, 2026, [https://arxiv.org/html/2511.02302v1](https://arxiv.org/html/2511.02302v1)  
27. Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures \- arXiv, accessed May 25, 2026, [https://arxiv.org/html/2505.09343v1](https://arxiv.org/html/2505.09343v1)  
28. SGLang vs vLLM: Complete LLM Inference Engine Comparison 2026 | Local AI Master, accessed May 25, 2026, [https://localaimaster.com/blog/sglang-vs-vllm-comparison](https://localaimaster.com/blog/sglang-vs-vllm-comparison)  
29. DeepSeek V4 (1.6T MoE, Multimodal) | Guides \- Clore.ai, accessed May 25, 2026, [https://docs.clore.ai/guides/language-models/deepseek-v4](https://docs.clore.ai/guides/language-models/deepseek-v4)  
30. How to Run DeepSeek V4 Locally ? \- Apidog, accessed May 25, 2026, [https://apidog.com/blog/how-to-run-deepseek-v4-locally/](https://apidog.com/blog/how-to-run-deepseek-v4-locally/)  
31. AI Agent Frameworks Compared: LangChain, CrewAI, and More \- Atlan, accessed May 25, 2026, [https://atlan.com/know/ai-agents-frameworks-compared/](https://atlan.com/know/ai-agents-frameworks-compared/)  
32. AI Agent Frameworks Comparison 2026: LangChain vs CrewAI vs AutoGen \- Cordum, accessed May 25, 2026, [https://cordum.io/blog/ai-agent-frameworks-comparison](https://cordum.io/blog/ai-agent-frameworks-comparison)  
33. Comparing AI agent frameworks: CrewAI, LangGraph, and BeeAI \- IBM Developer, accessed May 25, 2026, [https://developer.ibm.com/articles/awb-comparing-ai-agent-frameworks-crewai-langgraph-and-beeai/](https://developer.ibm.com/articles/awb-comparing-ai-agent-frameworks-crewai-langgraph-and-beeai/)  
34. CrewAI vs AutoGen vs LangGraph: Which Multi-Agent Framework in 2026?, accessed May 25, 2026, [https://dev.to/agdex\_ai/crewai-vs-autogen-vs-langgraph-which-multi-agent-framework-in-2026-51m6](https://dev.to/agdex_ai/crewai-vs-autogen-vs-langgraph-which-multi-agent-framework-in-2026-51m6)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAA5UlEQVR4XmNgGAX0ACJA/B9dEA3oAvEHBoi6eDQ5OLBhgCh4B8S/oWxsgIkBIncLymcH4r9A/AKuAgnIAbEvlA1SgMvQIiD+CcTSUL4nA0QtLvVwgM9QkLgFmlg+A8ISnACXoT4MqOJhQMyMxMcLcBm6nAEifh2Ie6BiJ4F4EQMRhuMy9DIDRNwcTRwk9g1NDAPgMnQ9A3ZxiiJqJgN2cYoMtWbALk6RoSAAEmfDIoZVPScQdwHxAQaEIpB324FYFqGMIRCIfwBxAJR/CIgvAjE3XAWZAJQ1k4B4EwNmShgFo4AWAADz6UM+NWOhyQAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAZCAYAAACo79dmAAACFklEQVR4Xu2WvUsdQRTFrx9BwSJgY/4CmxSiRVCiaEA0KZQIsQqkExFC8gfETkTsxCBqoRAiJEVsRAIiWAUFsUiVFCoWQr7IV2Ohhck9zizvvvNm387ysHs/OLBz5s7O3dk7uyNSpUpZalQdpt2qGlM1Gi/EgGqCzQgu2cjDJ9WIqlm1r/rndWGDAvxhI5IZ1UM2s3gnLqkWcYN/er9O9dr3QV3et2yoHpGHN3RbNS/p4xLQX8tmGnuq9+ISw4piMPNDwiv8yvvMLXFvCEmjv7O4u4gHqmM2QzyW4slw/cS0E4alsLoWtHfIY7KSBXzfIGeqD/66XtwgrAbTLunJTpHHxCaLN5tKk0QEefrExdrdO+TbN40XIiZZlNkkm5aXUrpSacyJi10w3qrE1RrGldtgYFu1yablXOKTRblwbaKNSbLAHHfZJJZVh2xaQjWYBuIGyTsQ98nLAmO72SRmVb/ZtBxJXLJLqlM2lXXVLpsBMEcPm8SauB9SKuPibnTCHYb7UvptTZhWfWMzAOboZZPAQ+PnUpakFLZUd4zf7/2PxmPaxMXYs0QIxNxjk8BXBV+XTH5JIelEz4si0kHsWzaVG6q/4lb+i+qr6ru4jRoiphyvaFA9E1c3i+JWLBZMEqrnvEQnWwlPpfKJcNh5weZ1Map6w2YOKn3Y3KyIOxLmBXUcOotcKzgEfWYzA2xCHE+rVMniP6qYfwSn1SCOAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAbCAYAAABFuB6DAAAAp0lEQVR4XmNgGAUDBpiAuBaI7wLxLiAuB+I2IJ6IrAgEeoD4PxDzQfkgNgiHw1UAgR1UsAtJ7CRUDAWABK5gEcOqcBoWMawKZZD4rFCx9UhiYICuE+RTkJgpmjjDdSCeBMT8QNzHAFG0G0UFFAgxQCS/MUCsA7HrUFTgACCFXOiC6ECfAdPNGIATiGcyQBSC3MuOKg0BikBcDMR5QJwLxJUMWHw9LAAAxC8mFkjhBosAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAABBElEQVR4XmNgGAWjYHABFiBOAuJUIM4A4kwkDOJrIpQSB24D8X88+AJCKWHwE4itgJgdiBcCMRsQcwFxLpQNcj06YEIXgAEZBoSkHwPENSCQBsTKUDY6mAXE4kD8BIjr0ORQwFcgPgZln2DA7jJRIF4MZS9nQDgAKwBJtkDZbxkgmtEByBA7KPsoAx4DnYD4CwMkzEAApNAHIQ0GeVBxGACxfyDxUcBfIM5B4l8C4odIfBD4BcT/GCBhCMIgA2ejqEAC6E4vAeL7DAgXgwBIDSgVgIAGED9mwBPb7mh8UBLiQBMDGVgMZVcAcSWSHFkAZGAUlA3yOsXAkgGSYx6hS4yCkQQAPFI174dGsrYAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAbCAYAAAB1NA+iAAAA1UlEQVR4XmNgGAX4QDEQ/4fiv1BaDyo3DYiZoWwMIMMAUXwUXQIIDgPxDwaIPFZwjAEimY4ugQROA/F3dEEQADkJ5mR8YDEQ70cXBAGY5kB0CTRQB8T26IIGDBDNWegSWIA4ugAILGWAGCCELkEsgEUT2QBf4F1mQMjD8BEUFUgS2EAMEBcyINRsBmIbFBVAcJMBtwEwAJI/hy4IA3wMEAVx6BJQIM0AkfdFl0AG2QwQRaCkGgYVswbicgbiXAgGuxkQfr0BpT8CMSsQFyGpGwWjgLoAAPd9OIif4LmnAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAwCAYAAACsRiaAAAADgUlEQVR4Xu3cT6gucxgH8PFfshIWNleUPyEbhaQUCYUIWdDdCgtZUcrmppCEUEjZsJDssLwLyYINsvJv4c9CCEnk3/N0Zpzffc7Muec6c8476vOpbzO/Z2bed+Y9p+ZpZt636wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFi4a2qB7tpaWLFTamEGp9YCALBMf9cC/1rSZ3NWLcxkSccIAExwwp72bS2syE7/jW6tBQBgWXa6Gfg/+7IWVuDwyL21ODP/AwCwcGMn66w9EvkkcnRZthW5/fWRP+qCFTki8kPktm78eKd8VgszOLdb24eaKc/WwjZkA3pz5JnIi0093z/rAMACfRi5utRq81DHB9Ou/1Hkt2a8Ku0+3RR5oBmnq/rp2QdUu+7kbvOm7bnIU5FfIieUZV+V8eCcfnppP90zLOgdU8bflXG6oha2IJvvPJ5Ub/XmMc7ZGAIAM8lvQdZm7OLIz804m4dcJ9d9r6lPuT/yZjPObX/t1hqbYbzbfoxc2Iz3R+7r579u6ndFjm3Gg98jt9dib2iA0gWRB/v5pyPnNcuqvf00r/y1hoax/Zzy/Vt5xfNQP8cruwO3qdu/H3m91ACAhTg98nEzfjLyUDPOqy55azRd19SnfNCtNQeDbAzyJ0OGBuHlZtluqc3JMD4u8mi7YMSdkRtqcRP3dGuvf7CH+Id9uCxy/Ei93ee8CrpdL3SbN2zfRx4vNQBgQdqTdz7g3t7Ka59Bqw1bXpGqJ/5sAF/p5/MZqUuaZal9vVe7jdunqdpjpZa3WveX2pHdxu2fj5zZz/8Ueamfr+uN+aIWZvJXP82rZe829bw1mU1zu293RI5qxv/FSd36a74V+aZZlnJZrgMALNRY45LNWb1dVxu2Kdk0jT1jVZ+VS2/UwgzqfqcTI+eXWnvc75TxoL1lulOG/c0fxj2sn9/bTwfZ3M7hxshr3cbfdBsaSABgocYalTFjDdvdtTAhr96c1q0/cD94u4zn8HktTPi0mT8jcnkzHuStwt2W32at/qyFbah/74u69UYRAFioPIGPXRHbiu3cRssrcauWDeQttdjLb3HW5man7amFRn4xYLsejuyLPNHU8hYsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKH7B6fxjnKFco+dAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAaCAYAAAC+aNwHAAAAw0lEQVR4XmNgGAWjADtQB+JtQLwAiJlRpQiDI0D8H4hnA/E5IN4NxPwoKvCAf0CchyYGMgyECYJ9DNgVohuQAcTfkPhwAFI0F12QAdMAISCWReLDAUhRIrogA6YBOAFIES+aWB9UPBbKXwPEh4BYEq4CCfwB4mYkvigDRLMglK8PxExQMWR1cMAIxG+A+B0Q/wDiXajSYAAy9Cy6IDLgAOIgILZCl4ACUBTnowuSAmCBmYYiSgIApdKLQOyJLjEKBhoAAPn6JxjegOmAAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAbCAYAAACjkdXHAAAAvUlEQVR4XmNgGAWjgEiwF4iXAfE9IJYB4k9APBmIPyArwgVAijmA+D8QfwFiVSCeBcR/gZgFSR0GkABiTyB2Y4BoBtkIAiD2H5giQmAPA8QFzOgSUMANxL8YIC7EAF+BeBu6IBoAeQcrADnTAl0QCbCiC8AAEwNEMy4AioUiBhxq0hlwSECBLBB/ZIAYggGqgfgGuiAaABneiC5IDBAH4uNQtjGyBDGgngES0rboEsQAJSA+BMSn0CVGAb0AAKKKIJMDuTgxAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAbCAYAAACTHcTmAAABCUlEQVR4XmNgGAUDBUyB+D+6IKUAZCBVDe0E4mMMVDRUFYh/AnETAxUNBRkUDMQhUDbFoASItaFsEA0yVA4hTR74iMSWYIAYaoIkRjIwA+IkNDGQoQloYjDAgi6ADYAMWA/Eq4B4JRCvgYr1IiuCgi1A/AddEB3wAfEbIH6AhkGGLoGqQQYCQCyPLogMtID4N7ogFIAMvYguSAwAaQxEF4QCkNxfNLEcqHg7mjgYLGZAZMVLDKgBrwDES5HkpwFxFRC7QeVxpopvQPweiL8zQLzPiCSXBsRfgPgDEH+GyoPYICAIxFehbKqBk0AsBcRs6BKUAJDXQbF/CF2CEnCAAZIiAtDER8GIBQCouz2PbRK0kQAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABHCAYAAAC6YRv5AAAFUklEQVR4Xu3dW6htUxgH8IE4cr8k1ySXB9dcQkoREknhhTp44cGDUyckJeVFLkmJ5AHlVuKBpBBJFLlTlLvTOXXUSUJuyW0Maw7G/vZca6+z9zrrbHv/fvVvjvHNueaaa73srzX3nDMlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADa9i3Ou7MavtisAANh4Z8TCApVmbe9mvroZAwAwD3/FwgJNen8AAMveqAbrpjRYvy5nTZe1Oeu7epuqHZ/TBQCABRjVsBXXp7m3+Thn527cbnt2znbNHACAeZirGSvKNm/HYvBnt9wqDbZ/Kf3XxAEAME+7p0FztWtc0aNst1csAgAsR5fk7JMGDdLROb/NXL3Z7JLG+zVuEu5PM99vWu8LADCW27tlbVL2qyuyz5tx64gR6bPjkMylnOacRvN0Vc4DOcfGFZ2TYwEAYNr2zXkyFheJVbGwiUyjMQQAmLdy1eWWsZj6awu1Iue4WBzio1gY4cVYCA7M+TkWG30N2405K2MRAGBz6GtWJv2Ip4Nyfmrmfe/Zmmv9MbEwhlH7fDMWOt/FAgDAYlGam/LYp0mJzdKoRujInC1iMVjTjF9oxqPEYxjHfF4DAPxPXRALi1w5fThX0zSuy3JOjMUhynseFYuNc9OgiarHdk3OCf+tHmljm6/jc56NRQBgaTo0bXyzsJS81ox3y/km562mVpUGqXxP46T1fbcsV55u6EkVXzdK3/sAAEtYaViW8x//8rioK5r57814Esb5bn/J+bZbAgDM8Hi3HKepWMrKKcwLcw6PKxagPHe0XMlargAFAJi3+r9b4zZsl+ZcNyIAAEzQH804Nmzln+Un6SxZtAEAFqmdwjw2bAAAbGbrw7xt2F4OcwAApuiunF/TzNOhd6dBg/ZGzvY5p3TzxWrbnG1C7fy0uI952r5I/Ve7ugoVAJaQcm+2ze28NGjCbg31h8P8zqRZG6bvexn1FAcA4H/k/VjYhPqaiio2bK834+rBNHofy1nf93JPLAAAtLbulgd3yz1Tf1NRxYatb9vHUn+d4d9LOQ0OADDLT814XTOOTUU7jw1bfcxT6/k08zUHdMtai/ufS3ksVXnNuzlP5Jw2c/XUHdAt5/N5hm07rA4ALHPl0Uvl6tQjQr1tHq7NubeZx4btpWZclF+Kvgy1W3L2z3m6m9cHsZcnDpSHxo+jHtOKbnlmzis5P3bzaRr2eYqLc67sxq829eryNPgsh4W6hg0AGOr0nB9yfmtqtXnYIeeDnJvDutua+XvNuCrbnBpqn6aZjU01bqMSt6vzQ3IualdMSd/nKce0dzNf3Yyrss2jsZhmfz4AgH+0TULf+NQ0uF1He+uJsu6OZv5nM66eTLMbkDivYv3DMC9KE/RULHbKKdLW2jAv+k7bromFNPjV7L5YTP37jMddPBsLPfpeV7S3dQEA+Fe5/1v5Za00ETs29U+6WnVSN/+4W5Yc3a3ra0AeSbPrcV7F+jNp9j/gx9uGVC/n7BFqn4d58U4sZM/FQrZ7zg2xmPr3GY+7nKKtF24U5areDc28iq8rSlNc7lsHALBJfB0LaeNu69G3Xfk/r3HU/2c7p6ld3YwnZdx9XtWMz87ZrplXfZ83NqgAABP3UJiPe+Pccqq1XPjQnnJd2YxHqb/0xfcZdup0Icbd5zVpcDzlQoydw7oqHm/xVSwAAExa+SWp3s+tWpX6m5Pl6rPU/314NBUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAh/A5jALRKIxqOKAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,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>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAaCAYAAACD+r1hAAAAJ0lEQVR4XmNgGAUjB6SRiBn+A3EMkRikFkIQCUY1EANGtgZSMGkAAH2nLjtZ4/WrAAAAAElFTkSuQmCC>
