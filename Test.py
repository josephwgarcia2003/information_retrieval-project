import json
from collections import Counter


with open("ksu1000.json", "r", encoding="utf-8") as f:
    data = json.load(f)

total_pages = len(data)
PagesWE = sum(1 for page in data if page["emails"])
PercentageWE = PagesWE / total_pages

email_count = Counter()
for page in data:
    email_count.update(page["emails"])

top_10_emails = email_count.most_common(10)

total_tokens = sum(len(page["body"].strip().split()) for page in data)
avg_tokens_per_page = total_tokens / total_pages

print("Total Pages:", total_pages)
print()
print("doc_len:", avg_tokens_per_page)
print()
print("emails:", top_10_emails)
print()
print("Perc:", PercentageWE )
