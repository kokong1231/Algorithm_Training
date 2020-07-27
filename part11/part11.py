cacheSize = int(input())
reference = input().split(', ')
cache = []
count_value = 0

for ref in reference:
  if not ref in cache:
    if len(cache) < cacheSize:
        cache.append(ref)
        count_value += 5

    elif cacheSize == 0:
        cache.append(ref)
        count_value += 5

    else:
        cache.pop(0)
        cache.append(ref)
        count_value += 5

  else:
    cache.pop(cache.index(ref))
    cache.append(ref)
    count_value += 1

print(count_value)

