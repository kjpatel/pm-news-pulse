# How I fight token fraud as a solo founder

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-i-fight-token-fraud-as-a-solo)
**Author**: Lenny Rachitsky (featuring Claire Vo) | **Date**: Nov 16, 2026

---

## Summary

Claire Vo, solo founder of ChatPRD, explains how fraudsters exploited her AI product's free trials, promo codes, relays, and a 24/7 compute-consuming MCP, costing tens of thousands of dollars. She argues that anyone selling AI is really selling compute, and shares the controls and real-time fraud classification she built to fight back.

## Key Takeaways

- **Treat AI usage as compute, not software seats.** Model your pricing, limits, and abuse monitoring around the fact that every request costs you real money, since selling AI means selling compute.
- **Eliminate or tightly gate free trials.** Vo turned off free trials entirely after fraudsters farmed them and resold promo codes, so require payment verification before granting meaningful usage.
- **Add business controls that raise the cost of abuse.** Use payment-side fraud tools like Stripe Radar, limit usage per account, and make reselling and relay schemes harder before investing in complex technical defenses.
- **Watch for abuse through your support channels.** Vo found that an AI support desk could itself become an attack vector, so review what your AI agents can be prompted to do.
- **Use a classifier loop to detect fraud in real time.** Vo uses Jev to classify suspicious usage patterns as they happen, and bot-detection and firewall tools like Vercel Bot ID and Vercel Firewall can filter automated abuse.

## Related

- [[2026-09-15 The AI cost crisis is entirely self-inflicted (and Fable 5 just made it worse)]]
- [[2026-06-24 Defending Against AI-Powered Attackers]]
- [[2026-08-02 How to Cut Your AI Bill From $200 to $20 a Month]]
