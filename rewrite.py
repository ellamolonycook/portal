import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Navigation
nav_start = content.find('<nav class="space-y-1">')
if nav_start == -1:
    print("Could not find nav")
    sys.exit(1)
    
nav_end = content.find('</nav>', nav_start) + len('</nav>')

new_nav = '''<nav class="space-y-1">
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-brand-deep bg-brand-sagelt transition-all duration-300 hover:translate-x-1">
          <svg class="w-4 h-4 text-brand-olive" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
          Home
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
          Curriculum
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
          Live Sessions
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-brand-mid hover:text-brand-deep hover:bg-brand-sagelt/50 transition-all duration-300 hover:translate-x-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          Resources
        </a>
      </nav>'''

content = content[:nav_start] + new_nav + content[nav_end:]

# 2. Replace Main Area
main_start = content.find('<!-- CENTER SCROLLABLE CONTENT -->')
main_end = content.find('<script>', main_start)

if main_start == -1 or main_end == -1:
    print("Could not find main area")
    sys.exit(1)

new_main = '''<!-- CENTER SCROLLABLE CONTENT -->
    <main class="flex-1 overflow-y-auto custom-scroll relative bg-brand-cream">
      <div class="absolute inset-0 grid-bg opacity-100 z-0"></div>
      
      <div class="relative z-10 p-8 lg:p-12 xl:px-16 max-w-[1200px] mx-auto min-h-full flex flex-col">
        
        <header class="mb-12">
          <h1 class="text-4xl lg:text-[42px] font-display font-bold tracking-tight text-brand-deep">
            Welcome back, Ella.
          </h1>
          <p class="mt-3 text-brand-mid max-w-2xl text-sm leading-relaxed">
            Here's what's happening this week, your next upcoming session, and your current learning phase.
          </p>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          <!-- What's Next This Week -->
          <div class="lg:col-span-2 space-y-4">
            <h2 class="text-[11px] font-mono tracking-[0.2em] uppercase text-brand-olive font-bold">What's next this week</h2>
            <div class="bg-brand-offwhite border border-brand-green/10 rounded-[1.5rem] p-8 shadow-sm h-[320px] flex flex-col justify-center items-center text-center card-lift">
              <div class="w-12 h-12 rounded-xl bg-brand-sagelt text-brand-olive flex items-center justify-center mb-4">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h3 class="text-xl font-bold text-brand-deep mb-2">Complete Phase 1 Exercises</h3>
              <p class="text-sm text-brand-mid max-w-sm mb-6">Finish drafting your AI agent personas and prompt structures for the upcoming review.</p>
              <button class="px-6 py-2.5 bg-brand-deep text-brand-offwhite text-xs font-semibold rounded-lg hover:bg-brand-green transition-colors">
                Resume Curriculum
              </button>
            </div>
          </div>

          <div class="space-y-8">
            <!-- Next Session -->
            <div class="space-y-4">
              <h2 class="text-[11px] font-mono tracking-[0.2em] uppercase text-brand-olive font-bold">Next Session</h2>
              <div class="bg-brand-offwhite border border-brand-green/10 rounded-2xl p-6 shadow-sm card-lift cursor-pointer hover:border-brand-green/30 transition-all">
                <div class="flex items-center gap-3 mb-4">
                  <div class="bg-red-50 text-red-600 text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">Live Call</div>
                  <div class="text-xs text-brand-mid font-medium">Thursday, 2:00 PM (Local)</div>
                </div>
                <h3 class="text-base font-bold text-brand-deep mb-2">Weekly Group Q&A</h3>
                <p class="text-xs text-brand-mid mb-4">Bring your questions on Phase 1 implementation.</p>
                <a href="#" class="text-xs font-semibold text-brand-olive hover:text-brand-deep flex items-center gap-1 transition-colors">
                  Join via Zoom <span class="font-mono ml-1">&rarr;</span>
                </a>
              </div>
            </div>

            <!-- The Phase You're On -->
            <div class="space-y-4">
              <h2 class="text-[11px] font-mono tracking-[0.2em] uppercase text-brand-olive font-bold">Current Phase</h2>
              <div class="bg-brand-offwhite border border-brand-green/10 rounded-2xl p-6 shadow-sm card-lift cursor-pointer hover:border-brand-green/30 transition-all">
                <div class="text-xs text-brand-mid font-medium mb-1">Phase 1</div>
                <h3 class="text-base font-bold text-brand-deep mb-3">Foundations & Strategy</h3>
                
                <div class="w-full bg-brand-sagelt rounded-full h-1.5 mb-3">
                  <div class="bg-brand-olive h-1.5 rounded-full" style="width: 60%"></div>
                </div>
                <div class="flex justify-between text-[10px] text-brand-mid font-medium">
                  <span>60% Complete</span>
                  <span>3/5 Modules</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </main>
  </div>

  '''

content = content[:main_start] + new_main + content[main_end:]

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
