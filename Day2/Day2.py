def repeating(data: str) -> int:
    ranges = data.strip().split(",")
    total = total2 = 0

    for r in ranges:
        low, high = map(int, r.split("-"))
        # Part 1 half repeating sequence
        for i in range(low, high + 1):
            text = str(i)
            mid = len(text) // 2
            if text[:mid] == text[mid:]:
                total += i
            # Part 2 any repeating sequence    
            for seq_len in range(1, len(text) // 2 + 1):
                if len(text) % seq_len == 0:
                    seq = text[:seq_len]
                    if seq * (len(text) // seq_len) == text:
                        total2 += i
                        break
    return total,total2

with open("Day2.txt") as f:
    result = repeating(f.read())
    print(result) 
