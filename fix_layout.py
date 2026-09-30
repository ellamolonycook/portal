import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove profile block from header
profile_start = content.find('<!-- Right Profile -->')
header_end = content.find('</header>')
if profile_start != -1 and header_end != -1:
    # We want to keep the closing </header> but remove the profile block
    # Actually, we can just replace the whole header inner content or slice out the profile block
    content = content[:profile_start] + '\n  ' + content[header_end:]

# 2. Change bg-brand-cream to bg-white on the main area
content = content.replace('<main class="flex-1 overflow-y-auto custom-scroll relative bg-brand-cream">', '<main class="flex-1 overflow-y-auto custom-scroll relative bg-white">')

# 3. Fix grid layout to let the video box push to the right
content = content.replace('<div class="relative z-10 p-8 lg:p-12 xl:px-16 grid grid-cols-1 xl:grid-cols-12 gap-12 max-w-[1600px] mx-auto">', '<div class="relative z-10 p-8 lg:p-12 xl:px-16 max-w-[1400px] mx-auto">')
content = content.replace('<!-- LEFT COLUMN (Spans 8) -->\n        <div class="xl:col-span-8 space-y-16">', '<!-- FULL WIDTH COLUMN -->\n        <div class="w-full space-y-16">')

# 4. Remove Phase Label
content = content.replace('<div class="text-xs text-brand-mid font-mono tracking-widest uppercase mb-2">Phase 1</div>', '')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
