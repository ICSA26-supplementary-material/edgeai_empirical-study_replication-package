# ATLAS.ti Exports – Documentation

This folder contains all **ATLAS.ti exports** used in our EdgeAI architecture study.  
The goal of this README is to help readers understand **what each export file contains**,  
**how it was generated**, and **how it can be reused or replicated**.

> 🧭 **How to read this document**  
> For each exported file we provide a **short, focused description**:
> - **Purpose:** why this file exists in the pipeline.
> - **Contents:** what kind of data it includes (codes, quotations, networks, etc.).
> - **Usage:** how this export is used in our analyses or replication.

---

## 1. ATLAS.ti Project Context

- **Tool version:** ATLAS.ti (desktop) – *version to be added if needed*  
- **Project scope:** qualitative/thematic coding of EdgeAI-related architectural fragments,
  including codes, categories, memos, and relationships used for RQ1.x.  
- **Main tasks supported by these exports:**
  - Reconstructing the **coding scheme** (codes, categories, families).
  - Inspecting **quotations / fragments** and their assigned codes.
  - Generating tables and statistics for **guidelines, domains, and quality attributes**.
  - Validating and replicating the **thematic analysis process**.

---

## 2. File Overview

Below we will document **each export file** individually.

For every file, we will add a mini-section in the following format:

```text

### 2.X 20250914_theme_frequencies.csv

- **Purpose:**  
  This export summarizes the **frequency of all themes** identified during the ATLAS.ti coding process. It provides a quantitative view of how often each high-level theme appeared across the coded fragments.

- **Contents:**  
  A CSV table containing at least two columns:  
  - **theme** – the thematic label or category assigned during axial/thematic coding.  
  - **frequency** – the number of times that theme appeared in the dataset (i.e., total quotations coded with that theme or aggregated subcodes).  

  This export represents the **final consolidated theme frequency table** used for descriptive statistics in the study.

- **Usage:**  
  Ideal for:  
  - generating plots (bar charts, Pareto charts, heatmaps);  
  - inspecting theme distribution for RQ1.x;  
  - validating the representativeness of guideline families;  
  - triangulating with the GitHub mining dataset and ISO/IEC mappings.  

  Researchers replicating this study can recompute this table by regrouping codes → categories → themes following the same hierarchical structure documented in the coding scheme.

```

### 2.X 20250914_code_frequencies.csv

- **Purpose:**  
  This file provides the **frequency of each individual code** used during the ATLAS.ti open coding phase.  
  While the theme frequency export aggregates information at a higher level, this file captures the **granular coding activity**, enabling deeper quantitative inspection of the coding scheme.

- **Contents:**  
  A CSV table typically containing:  
  - **code** – the exact code label assigned to quotations during open coding.  
  - **frequency** – the number of quotations associated with each code.  

  The table includes both low-level codes and more abstract codes, depending on how the coding hierarchy was structured.

- **Usage:**  
  Useful for:  
  - analyzing which concepts were most prominent in the qualitative dataset;  
  - generating visualizations (e.g., bar charts, Zipf-like distributions, code clouds);  
  - validating the consistency of the coding process;  
  - supporting RQ1.x by quantifying architectural concerns, patterns, and EdgeAI practices extracted from repositories;  
  - triangulating with ISO/IEC 25010 quality attribute mappings and guideline families.

  This export is essential for replicating the **open coding stage** and for reconstructing the prevalence of each architectural construct identified in the study.


[//]: # ()
[//]: # (### 2.X <FILENAME>)

[//]: # ()
[//]: # (- **Purpose:** ...)

[//]: # (- **Contents:** ...)

[//]: # (- **Usage:** ...)
