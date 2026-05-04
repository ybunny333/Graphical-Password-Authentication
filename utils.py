import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def normalize_point(point, grid_size):
    return (
        point[0] // grid_size * grid_size,
        point[1] // grid_size * grid_size
    )

def combine_data(points, words, grid_size):
    combined = ""

    for i in range(len(points)):
        p = normalize_point(points[i], grid_size)
        combined += f"{p[0]},{p[1]}:{words[i]}|"

    return combined