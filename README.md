import math
import sys

def calculate_similarity(vec_x, vec_y):
    dot_product = vec_x[0] * vec_y[0] + vec_x[1] * vec_y[1] + vec_x[2] * vec_y[2]
    norm_sq_x = vec_x[0]**2 + vec_x[1]**2 + vec_x[2]**2
    norm_sq_y = vec_y[0]**2 + vec_y[1]**2 + vec_y[2]**2
    
    norm_x = math.sqrt(norm_sq_x)
    norm_y = math.sqrt(norm_sq_y)
    
    if norm_x == 0 or norm_y == 0:
        return -2.0
        
    return dot_product / (norm_x * norm_y)

def solve():
    try:
        N = int(sys.stdin.readline().strip())
    except:
        return
    
    words = []
    vectors = []

    for _ in range(N):
        try:
            line = sys.stdin.readline().strip()
            if not line:
                break
                
            parts = line.split()
            word = parts[0]
            vector = [int(p) for p in parts[1:4]]
            
            words.append(word)
            vectors.append(vector)
        except:
            continue

    num_words = len(words)
    
    if num_words < 2:
        return

    max_similarity = -2.0
    result_pair = ("", "")

    for i in range(num_words):
        for j in range(i + 1, num_words):
            
            vec_i = vectors[i]
            vec_j = vectors[j]
            
            current_similarity = calculate_similarity(vec_i, vec_j)
            
            if current_similarity > max_similarity:
                max_similarity = current_similarity
                result_pair = (words[i], words[j])
            
    if result_pair[0] and result_pair[1]:
        sys.stdout.write(f"{result_pair[0]} {result_pair[1]}\n")

solve()
