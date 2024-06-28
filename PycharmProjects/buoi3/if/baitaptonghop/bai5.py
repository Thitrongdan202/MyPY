import random as r

# Chọn số lượng người chơi ngẫu nhiên từ 8 đến 20
num_players = r.randint(8, 20)
print(f"Số lượng người chơi: {num_players}")

# Tạo danh sách các lựa chọn của từng người chơi
choices = [r.choice(['Kéo', 'Búa', 'Bao']) for _ in range(num_players)]
scores = [0] * num_players  # Khởi tạo điểm số cho mỗi người chơi

# Hiển thị lựa chọn của từng người chơi
for i, choice in enumerate(choices):
    print(f"Người chơi {i + 1} chọn: {choice}")

# So sánh lựa chọn của từng người với nhau và xác định kết quả
print("\nKết quả các trận đấu:")

for i in range(num_players):
    for j in range(i + 1, num_players):
        nguoi_1 = choices[i]
        nguoi_2 = choices[j]
        result = ""

        if nguoi_1 == nguoi_2:
            result = f"Người chơi {i + 1} và Người chơi {j + 1}: Hòa"
        elif nguoi_1 == "Kéo":
            if nguoi_2 == "Bao":
                result = f"Người chơi {i + 1} thắng Người chơi {j + 1}"
                scores[i] += 1
            elif nguoi_2 == "Búa":
                result = f"Người chơi {i + 1} thua Người chơi {j + 1}"
                scores[j] += 1
        elif nguoi_1 == "Búa":
            if nguoi_2 == "Kéo":
                result = f"Người chơi {i + 1} thắng Người chơi {j + 1}"
                scores[i] += 1
            elif nguoi_2 == "Bao":
                result = f"Người chơi {i + 1} thua Người chơi {j + 1}"
                scores[j] += 1
        elif nguoi_1 == "Bao":
            if nguoi_2 == "Búa":
                result = f"Người chơi {i + 1} thua Người chơi {j + 1}"
                scores[j] += 1
            elif nguoi_2 == "Kéo":
                result = f"Người chơi {i + 1} thắng Người chơi {j + 1}"
                scores[i] += 1

        print(result)

# Tìm người chơi có điểm cao nhất
max_score = max(scores)
winners = [i + 1 for i, score in enumerate(scores) if score == max_score]

# In điểm của từng người chơi và người chiến thắng cuối cùng
print("\nĐiểm của từng người chơi:")
for i, score in enumerate(scores):
    print(f"Người chơi {i + 1}: {score} điểm")

if len(winners) > 1:
    print(f"\nCó {len(winners)} người chiến thắng với {max_score} điểm: Người chơi {', '.join(map(str, winners))}")
else:
    print(f"\nNgười chơi chiến thắng cuối cùng là Người chơi {winners[0]} với {max_score} điểm")
