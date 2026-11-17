# The Lakehouse for AI

**Source**: [Tomasz Tunguz](https://tomtunguz.com/the-lakehouse-for-ai/)
**Author**: Tomasz Tunguz | **Date**: Nov 17, 2026

---

## Summary

LanceDB's $57.5m Series B and the production deployments at Exa, Runway, Microsoft AI, Adobe, and NVIDIA argue that AI workloads are consolidating onto a single multimodal lakehouse format (Lance) that serves both training and inference, replacing fragmented blob, Parquet, and vector copies. The piece frames this architecture as the emerging standard for frontier-scale AI data.

## Key Takeaways

- **Consolidate fragmented AI data copies into one store.** Replace separate blob storage, Parquet files, and vector indexes with a single multimodal table format that serves both training and inference, which removes duplicate pipelines and sync failures.
- **Use column backfills to avoid rewriting large datasets.** Exa's approach of adding new columns in place and writing only new data shows how to enrich massive corpora without reprocessing everything.
- **Pick formats that handle unstructured data, appends, distributed reads, and SQL together.** Runway chose Lance in 2024 because it was the only option covering all of these needs at once, so evaluate candidate storage formats against that full requirement list.
- **Keep AI data under the same governance contract as other enterprise data.** Adobe's platform team places AI-native data in its existing lakehouse under the same contract, so security, access, and compliance policies apply uniformly.
- **Plan for data layers that scale to thousands of GPUs.** NVIDIA's training on tens of thousands of GPUs reading Lance tables directly, and Microsoft AI's distributed inference across thousands of nodes, suggest designing data infrastructure for parallel access from the start.

## Related

- [[2026-10-05 Inference Is the Most Important Market in Software]]
- [[2026-08-21 Mainframes became personal. So will your data center.]]
- [[2026-03-05 Data Center Intelligence at the Price of a Laptop]]
