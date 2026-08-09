import re

index_path = r'c:\Users\makok\Desktop\Trip to Hiroshima\index.html'
map_path = r'c:\Users\makok\Desktop\Trip to Hiroshima\map.html'

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Remove card-header-media div entirely
index_html = re.sub(r'<div class="card-header-media">.*?</div>', '', index_html, flags=re.DOTALL)
# Remove card-photo img tags
index_html = re.sub(r'<img[^>]*class="card-photo"[^>]*>\s*', '', index_html)
# Update tap hint
index_html = re.sub(r'<div class="card-tap-hint">[^<]+</div>', '<div class="card-tap-hint">タップで詳細・公式HP表示 ▼</div>', index_html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

with open(map_path, 'r', encoding='utf-8') as f:
    map_html = f.read()

# Remove img tag generation block in popup
map_html = re.sub(
    r'if\s*\(\s*spot\.img\s*\)\s*\{\s*popupContent\s*\+=\s*`<img[^>]+>`;\s*\}',
    '// Image removed per instructions',
    map_html
)

with open(map_path, 'w', encoding='utf-8') as f:
    f.write(map_html)

print("Done")
