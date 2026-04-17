def suggest_gate(crowd_data):
    if crowd_data["Gate A"] > crowd_data["Gate B"]:
        return "Use Gate B (less crowded)"
    else:
        return "Use Gate A"

def estimate_wait_time(queue_length):
    if queue_length > 100:
        return "High waiting time"
    elif queue_length > 50:
        return "Moderate waiting time"
    else:
        return "Low waiting time"

# Example usage
crowd = {"Gate A": 120, "Gate B": 60}
print(suggest_gate(crowd))
print(estimate_wait_time(120))
