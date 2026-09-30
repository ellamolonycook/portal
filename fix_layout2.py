import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix container width (bring video box closer)
content = content.replace('max-w-[1600px]', 'max-w-[1100px]')
content = content.replace('-right-8', 'right-0')

# 2. Drop the olive accent overall -> change to deep/mid (monochrome)
content = content.replace('text-brand-olive', 'text-brand-deep')
content = content.replace('bg-brand-olive', 'bg-brand-deep')
content = content.replace('group-hover:text-brand-olive', 'group-hover:text-brand-mid')
content = content.replace('shadow-brand-olive/20', 'shadow-brand-deep/10')
content = content.replace('shadow-brand-olive/10', 'shadow-brand-deep/5')

# Make the glowing orb neutral instead of green
content = content.replace('rgba(204,238,160,0.6)', 'rgba(230,230,230,0.6)')
content = content.replace('rgba(204,238,160,0)', 'rgba(230,230,230,0)')

# 3. Fix the lower section: remove the external headings and integrate them cleanly.
lower_section_start = content.find('<!-- NEXT SESSION & CURRENT PHASE -->')
lower_section_end = content.find('</main>')

if lower_section_start != -1 and lower_section_end != -1:
    new_lower = '''<!-- NEXT SESSION & CURRENT PHASE -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-10 border-t border-brand-green/10 mt-16">
            
            <!-- Next Session -->
            <div class="p-8 rounded-[1.5rem] bg-brand-offwhite border border-brand-green/10 shadow-sm flex flex-col card-lift cursor-pointer group h-full relative overflow-hidden">
              <div class="text-[10px] font-mono tracking-[0.2em] uppercase text-brand-deep/60 font-bold mb-6">Next Session</div>
              <div class="flex items-center gap-3 mb-4">
                <div class="bg-brand-deep/5 text-brand-deep text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-brand-deep animate-pulse"></span>Live Call</div>
                <div class="text-sm text-brand-mid font-medium">Thursday, 2:00 PM (Local)</div>
              </div>
              <h3 class="text-2xl font-bold text-brand-deep mb-3 group-hover:text-brand-mid transition-colors">Weekly Group Q&A</h3>
              <p class="text-sm text-brand-mid leading-relaxed mb-8 flex-1">Bring your questions on Phase 1 implementation. We'll be reviewing agent personas live.</p>
              <div class="flex items-center gap-3 mt-auto">
                <button class="px-5 py-2.5 bg-brand-deep text-brand-offwhite text-xs font-semibold rounded-xl hover:bg-brand-green transition-colors shadow-sm">
                  Join via Zoom
                </button>
                <button class="px-5 py-2.5 text-brand-deep text-xs font-semibold rounded-xl border border-brand-green/15 hover:bg-brand-sagelt transition-colors">
                  Add to Calendar
                </button>
              </div>
            </div>

            <!-- Current Phase -->
            <div class="p-8 rounded-[1.5rem] bg-brand-offwhite border border-brand-green/10 shadow-sm flex flex-col card-lift cursor-pointer group h-full relative overflow-hidden">
              <div class="text-[10px] font-mono tracking-[0.2em] uppercase text-brand-deep/60 font-bold mb-6">Current Phase</div>
              <h3 class="text-2xl font-bold text-brand-deep mb-3 group-hover:text-brand-mid transition-colors mt-2">Foundations & Strategy</h3>
              <p class="text-sm text-brand-mid leading-relaxed mb-8 flex-1">You are currently learning how to build the foundational strategy for your custom AI agents.</p>
              
              <div class="mt-auto">
                <div class="w-full bg-brand-green/10 rounded-full h-2 mb-4 overflow-hidden">
                  <div class="bg-brand-deep h-full rounded-full transition-all duration-1000 ease-out" style="width: 60%"></div>
                </div>
                <div class="flex justify-between text-xs text-brand-deep font-medium">
                  <span>60% Complete</span>
                  <span class="text-brand-mid">3/5 Modules</span>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    '''
    content = content[:lower_section_start] + new_lower + content[lower_section_end:]

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
