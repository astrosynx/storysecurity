# 🚀 Astrosynx — Stress & Chaos Testing Suite

Production-oriented **chaos & stress testing toolkit** for **Story validator nodes**.  
Designed to safely simulate real-world failure conditions, measure recovery behavior, and improve operational resilience **before incidents happen**.

---

## 🧠 What Is This?

Astrosynx Stress & Chaos Testing Suite is a **scenario-driven framework** that allows validator operators to deliberately introduce controlled failures into their infrastructure and observe how systems behave under pressure.

The goal is **not to break the network**, but to answer critical operational questions:

- How fast does a node recover after failure?
- Does it rejoin peers correctly?
- Are monitoring and alerting systems reacting in time?
- Which configurations degrade silently under load?

---

## ✨ Key Features

✅ Scenario-based fault injection (YAML)  
🌐 Network degradation (latency, packet loss)  
🔁 Validator service restarts (systemd)  
🔥 CPU & IO stress testing (`stress-ng`)  
📡 gRPC-level Story observability  
📊 Recovery & MTTR measurement  
🛡️ Safe-by-default execution (`DRY_RUN`)  
🧩 Modular & extensible architecture  

---

## 🧱 High-Level Architecture

```mermaid
flowchart TD
    %% =====================
    %% Operator Input
    %% =====================
    subgraph Input["Operator & Configuration"]
        A1["Validator Operator"]
        A2["Scenario YAML<br/>(faults, timing, params)"]
    end

    %% =====================
    %% Control Layer
    %% =====================
    subgraph Control["Control & Orchestration"]
        B1["CLI Controller<br/>(chaosctl.py)"]
        B2["Safety Guardrails<br/>(DRY_RUN, mainnet-safe)"]
        B3["Chaos Engine<br/>(fault sequencing)"]
    end

    %% =====================
    %% Fault Injection
    %% =====================
    subgraph Faults["Fault Injection Layer"]
        C1["Network Faults<br/>(tc / netem)"]
        C2["Node Faults<br/>(systemd restart)"]
        C3["Resource Stress<br/>(stress-ng CPU / IO)"]
    end

    %% =====================
    %% Runtime Environment
    %% =====================
    subgraph Runtime["Validator Runtime"]
        D1["Story Validator Node"]
        D2["Host OS & Network Stack"]
    end

    %% =====================
    %% Observability
    %% =====================
    subgraph Metrics["Metrics & Observability"]
        E1["Runtime Metrics<br/>(duration, peers)"]
        E2["Story gRPC Metrics<br/>(health, sync, height)"]
    end

    %% =====================
    %% Reporting
    %% =====================
    subgraph Output["Reporting & Artifacts"]
        F1["Metrics Aggregation"]
        F2["Chaos Report<br/>(chaos_report.md)"]
    end

    %% =====================
    %% Data Flow
    %% =====================
    A1 --> A2
    A2 --> B1

    B1 --> B2 --> B3

    B3 --> C1
    B3 --> C2
    B3 --> C3

    C1 --> D2
    C2 --> D1
    C3 --> D2

    D1 --> E1
    D1 --> E2
    D2 --> E1

    E1 --> F1
    E2 --> F1

    F1 --> F2
