import sys
input = sys.stdin.readline

n = int(input().strip())
coords = list(map(int, input().split()))

sorted_coords = sorted(set(coords))

coord_dict = {value: index for index, value in enumerate(sorted_coords)}

compressed_coords = [coord_dict[x] for x in coords]

print(' '.join(map(str, compressed_coords)))