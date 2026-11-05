from datasets import load_dataset
docs = load_dataset("thesafetystack/the-safety-stack", split="train")   # one row per document, every annotation

def used(row, slug):   # the document's own work uses the technique, at least a paragraph's worth
    st = row["annotations"]["safety_techniques"]
    return any(t["slug"] == slug and t["roles"]["used"] >= 2 for t in (st and st["payload"]["techniques"]) or [])

rlhf = docs.filter(lambda r: used(r, "rlhf"))
