# ws\_mch\_iot — Industrial Telemetry 

*Real‑time monitoring meets historic analytics on Microsoft Fabric.*

## Overview

`ws\\\\\\\_mch\\\\\\\_iot` transforms live machinery sensor data into operational intelligence and long‑term business insights. The platform ingests high‑velocity telemetry, classifies anomalies instantly, drives a live KQL dashboard, and builds a star‑schema history for Power BI trend analysis.

## Architecture Pillars

**Hot Path (Eventhouse)**
Live ingestion flows via Eventstream directly into a KQL database. An update policy cleans and classifies raw telemetry (`NORMAL`/`ALERT`/`ANOMALY`/`BAD`/`NULL`). Materialized views refresh a 10‑tile operational dashboard, while alert functions trigger Activator email notifications on critical failures. All rejected records remain queryable for root‑cause debugging.

**Cold Path (Lakehouse)**
A scheduled incremental pipeline (daily 00:00 UTC) pulls cleaned data into a medallion lakehouse. The Bronze layer stores raw exports; Silver applies an idempotent `MERGE` on `event\\\\\\\_id` (with a dead‑letter queue for stale or malformed data); and Gold joins to current master dimensions to produce `ft\\\\\\\_telemetry` and `agg\\\\\\\_machine\\\\\\\_daily` fact tables. These Gold tables feed a Direct Lake semantic model, which serves a comprehensive Power BI report for historic and predictive analytics.

**Control Path (Warehouse)**
Master reference data is maintained as SCD Type‑2 dimensions for 10 plants, 18 lines, and 31 machines. A current‑state view (`vw\\\\\\\_mch\\\\\\\_machine\\\\\\\_current`) abstracts SCD complexity for seamless joins. Security is demo‑ready: Row‑Level Security restricts operational users to APAC plants, and Column‑Level Security hides commercial fields (`maintenance\\\\\\\_cost`, `vendor\\\\\\\_contact`).

## Orchestration \& Execution

Three data pipelines orchestrate the batch workflows. All notebooks execute on the Python kernel (`deltalake`, `azure-kusto-data`, `pyodbc`) to handle trial capacity constraints, with production‑grade Spark variants (V‑Order, broadcast joins) provided as reference.

## End‑to‑End Lineage

Every telemetry record resolves through `tbl\\\\\\\_mch\\\\\\\_clean.machine\\\\\\\_id` → `DIM\\\\\\\_MACHINE` → `DIM\\\\\\\_LINE` → `DIM\\\\\\\_PLANT`, ensuring full referential integrity across the entire platform.

