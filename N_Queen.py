import random

# توليد حالة عشوائية لسلسلة الأم المكونة من الملكات
def generate_random_board(n):
    board = list(range(n))
    random.shuffle(board)
    return board

# تقييم الحالة بعدد التصادمات بين الملكات
def evaluate(board):
    n = len(board)
    collisions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or board[i] - i == board[j] - j or board[i] + i == board[j] + j:
                collisions += 1
    return collisions

# عملية التطور والتلاعب بالسلسلة الأم
def evolve(board, population_size, mutation_rate):
    n = len(board)
    population = [board]

    # إنشاء عدد معين من السلسلات الأم المطابقة
    while len(population) < population_size:
        new_board = board.copy()

        # تطبيق عملية الانتقال على السلسلة الجديدة
        for i in range(n):
            if random.random() < mutation_rate:
                j = random.randint(0, n - 1)
                new_board[i], new_board[j] = new_board[j], new_board[i]

        population.append(new_board)

    # تقييم وفرز السلسلات الأم المطابقة
    population = sorted(population, key=lambda x: evaluate(x))
    return population[0]

# حل المشكلة باستخدام الخوارزمية الجينية
def solve_n_queen(n, population_size=100, mutation_rate=0.1, max_iterations=1000):
    # إنشاء سلسلة الأم الأولية
    board = generate_random_board(n)
    iterations = 0

    while evaluate(board) > 0 and iterations < max_iterations:
        board = evolve(board, population_size, mutation_rate)
        iterations += 1

    if evaluate(board) == 0:
        print("تم حل المشكلة. الحل النهائي:")
        print(board)
        print_board(board)
    else:
        print("لم يتم العثور على حل في الحد الأقصى لعدد الاجتيازات.")

# طباعة السلسلة الأم المكونة من الملكات كل ملكة في سطرها
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ["X"] * n
        row[board[i]] = "Q"
        print(" ".join(row))

# استدعاء الدالة لحل مشكلة N-Queen مع N = 8
solve_n_queen(8)