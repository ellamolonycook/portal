import os

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove header text
text_to_remove = '''<!-- Middle Nav -->
      <div class="hidden md:flex items-center gap-4 text-[10px] font-mono tracking-widest uppercase text-brand-mid">
        <span class="flex items-center gap-2 text-brand-deep font-medium">
          <span class="w-1.5 h-1.5 rounded-full bg-brand-deep"></span>
          AI EDUCATION
        </span>
        <span class="text-brand-green/30">|</span>
        <span>BUILD &bull; LEARN &bull; GROW</span>
      </div>'''
content = content.replace(text_to_remove, '')

# 2. Change video to minimal abstract
content = content.replace(
    'src="https://www.w3schools.com/html/mov_bbb.mp4"',
    'src="https://assets.mixkit.co/videos/preview/mixkit-white-abstract-waves-moving-slowly-seamless-loop-32943-large.mp4"'
)

# 3. Update sidebar links
content = content.replace('>Home</a>', ' href="dashboard.html">Home</a>')
content = content.replace('href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-brand-deep bg-brand-sagelt', 'href="dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-brand-deep bg-brand-sagelt')

# The others are currently: href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid ...
content = content.replace('href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">\n          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>\n          Curriculum', 'href="curriculum.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">\n          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>\n          Curriculum')

content = content.replace('href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">\n          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>\n          Live Sessions', 'href="sessions.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">\n          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>\n          Live Sessions')

content = content.replace('href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">\n          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>\n          Resources', 'href="resources.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">\n          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>\n          Resources')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Define helper to scaffold pages
def create_page(filename, title, active_url):
    # read base
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        page = f.read()
    
    # 1. Strip the active class from dashboard.html
    page = page.replace('href="dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-brand-deep bg-brand-sagelt transition-all duration-300 hover:translate-x-1"', 'href="dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1"')
    
    # 2. Add the active class to the current page
    target_link = f'href="{active_url}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1"'
    active_link = f'href="{active_url}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-brand-deep bg-brand-sagelt transition-all duration-300 hover:translate-x-1"'
    page = page.replace(target_link, active_link)
    
    # 3. Replace main content with placeholder
    main_start = page.find('<!-- FULL WIDTH COLUMN -->')
    main_end = page.find('</main>')
    
    new_content = f'''<!-- CONTENT -->
        <div class="w-full space-y-12">
          <div class="space-y-4">
            <h1 class="text-3xl font-display font-bold text-brand-deep">{title}</h1>
            <p class="text-brand-mid text-sm">Content for {title} will populate here.</p>
          </div>
        </div>
      </div>
    '''
    page = page[:main_start] + new_content + page[main_end:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page)

create_page('curriculum.html', 'Curriculum', 'curriculum.html')
create_page('sessions.html', 'Live Sessions', 'sessions.html')
create_page('resources.html', 'Resources', 'resources.html')

