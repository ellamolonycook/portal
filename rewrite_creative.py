import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Sidebar Rewrite
nav_start = content.find('<nav class="space-y-1">')
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

# 2. Update Hero content
content = content.replace("Time Rich AI Learning Hub", "WHAT'S NEXT THIS WEEK")
content = content.replace("Build the skills, systems, and AI agents that give you your time back.", "Draft your first AI agent personas.")
content = content.replace("Learn to build, deploy, and manage AI systems that work alongside your business. Practical courses, hands-on training, and expert guidance — all in one place.", "Finish drafting your agent personas and prompt structures so they're ready for the upcoming live review session on Thursday.")
content = content.replace("Explore Courses", "Resume Curriculum")
content = content.replace("Watch Intro", "View Workbook")

# Sticky note replacements
content = content.replace("+</span> Learn</div>", "+</span> Goal</div>")
content = content.replace(">Build</div>", ">Actions</div>")
content = content.replace(">Automate</div>", ">Content</div>")
content = content.replace("+</span> Grow</div>", "+</span> Next</div>")

# 3. Replace "Featured Courses" and "Learning Paths" with "Next Session" & "Current Phase"
# We need to wipe out the big sections and replace them.
feature_start = content.find('<!-- FEATURED COURSES -->')
main_end = content.find('<!-- FOOTER -->') if '<!-- FOOTER -->' in content else content.find('</main>')

if feature_start != -1 and main_end != -1:
    new_sections = '''<!-- NEXT SESSION & CURRENT PHASE -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 pt-8 border-t border-brand-green/10 mt-12">
            
            <!-- Next Session -->
            <section class="space-y-6">
              <div class="flex items-baseline justify-between pb-2">
                <h2 class="text-lg font-bold text-brand-deep">Next Session</h2>
              </div>
              <div class="p-8 rounded-[1.5rem] bg-brand-offwhite border border-brand-green/10 shadow-sm flex flex-col card-lift cursor-pointer group h-full">
                <div class="flex items-center gap-3 mb-6">
                  <div class="bg-red-50 text-red-600 text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-red-600 animate-pulse"></span>Live Call</div>
                  <div class="text-sm text-brand-mid font-medium">Thursday, 2:00 PM (Local)</div>
                </div>
                <h3 class="text-2xl font-bold text-brand-deep mb-3 group-hover:text-brand-olive transition-colors">Weekly Group Q&A</h3>
                <p class="text-sm text-brand-mid leading-relaxed mb-8 flex-1">Bring your questions on Phase 1 implementation. We'll be reviewing agent personas live.</p>
                <div class="flex items-center gap-3">
                  <button class="px-5 py-2.5 bg-brand-deep text-brand-offwhite text-xs font-semibold rounded-xl hover:bg-brand-green transition-colors shadow-lg shadow-brand-deep/10">
                    Join via Zoom
                  </button>
                  <button class="px-5 py-2.5 text-brand-deep text-xs font-semibold rounded-xl border border-brand-green/15 hover:bg-brand-sagelt transition-colors">
                    Add to Calendar
                  </button>
                </div>
              </div>
            </section>

            <!-- Current Phase -->
            <section class="space-y-6">
              <div class="flex items-baseline justify-between pb-2">
                <h2 class="text-lg font-bold text-brand-deep">Current Phase</h2>
              </div>
              <div class="p-8 rounded-[1.5rem] bg-brand-offwhite border border-brand-green/10 shadow-sm flex flex-col card-lift cursor-pointer group h-full">
                <div class="text-xs text-brand-mid font-mono tracking-widest uppercase mb-2">Phase 1</div>
                <h3 class="text-2xl font-bold text-brand-deep mb-3 group-hover:text-brand-olive transition-colors">Foundations & Strategy</h3>
                <p class="text-sm text-brand-mid leading-relaxed mb-8 flex-1">You are currently learning how to build the foundational strategy for your custom AI agents.</p>
                
                <div class="w-full bg-brand-sagelt rounded-full h-2.5 mb-4 overflow-hidden border border-brand-sage">
                  <div class="bg-brand-olive h-full rounded-full transition-all duration-1000 ease-out" style="width: 60%"></div>
                </div>
                <div class="flex justify-between text-xs text-brand-deep font-medium">
                  <span>60% Complete</span>
                  <span class="text-brand-mid">3/5 Modules</span>
                </div>
              </div>
            </section>

          </div>
        </div>
      </div>
    '''
    content = content[:feature_start] + new_sections + content[main_end:]

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
