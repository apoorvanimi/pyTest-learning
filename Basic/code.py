# Sample 1: basics
name = "SDET Candidate"
scores = [88, 92, 79, 95]
avg = sum(scores) / len(scores)
print(f"Hi {name}, your average score is {avg:.2f}")
for i, s in enumerate(scores, start=1):
    print(i, s)
    print(f"Attempt {i}: {'PASS' if s >= 80 else 'FAIL'}")

users = [{"id": 1, "name": "Amit"}, {"id": 2, "name": "Priya"}]
print (users[0].get("id"))
print (users[0].get("name"))
by_id = {u["id"]: u["name"] for u in users}
print(by_id)