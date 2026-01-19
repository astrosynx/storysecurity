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

