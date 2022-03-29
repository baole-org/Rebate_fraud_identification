# Rebate_fraud_checking
Company [anonymised] is promoting a campaign where users who makes payment by scanning QR code at merchants' store will be rewarded with Rebate.

Rebate is determined at 30% of transaction value, capped at $2 per txn.

It is reported that some users are colluding with merchants to abuse this promotion campaign. Our job is to identify the potential abusers, both users and merchants.

In the notebook, we demonstrated 2 methods:
- Heuristic based on our domain knowledge in the epayment industry, and
- Graph approach where we cluster the users in to clusters, and identify the abnormal one out.
