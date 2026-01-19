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

flowchart TD
    A[User / Operator] --> B[Scenario YAML]

    B --> C[CLI: chaosctl.py]
    C --> D[Safety Guardrails]

    D --> E[Chaos Engine]

    E --> F1[Network Faults]
    E --> F2[Node Faults]
    E --> F3[Resource Stress]

    F1 --> G1[tc / netem<br/>latency, packet loss]
    F2 --> G2[systemd<br/>service restart]
    F3 --> G3[stress-ng<br/>CPU / IO pressure]

    G1 --> H[Metrics Collection]
    G2 --> H
    G3 --> H

    H --> I1[Runtime Metrics<br/>peers, duration]
    H --> I2[gRPC Metrics<br/>health, sync, height]

    I1 --> J[Report Generator]
    I2 --> J

    J --> K[chaos_report.md]

    subgraph Safety
        D
    end

    subgraph Observability
        H
        I1
        I2
    end

 ---
