import glob

files = glob.glob('*.html')

video_old = 'https://assets.mixkit.co/videos/preview/mixkit-white-abstract-waves-moving-slowly-seamless-loop-32943-large.mp4'
video_new = 'https://assets.mixkit.co/videos/preview/mixkit-abstract-technology-lines-background-loop-32742-large.mp4'

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Move container left by increasing max-w and forcing a smaller left margin if needed, 
    # but increasing max-w is usually enough. Let's try changing mx-auto to mr-auto ml-8 lg:ml-16
    content = content.replace('max-w-[1100px] mx-auto', 'max-w-[1200px] mr-auto ml-4 lg:ml-12')
    
    # Change background position of grid so it stays anchored left
    content = content.replace('background-position: center top;', 'background-position: left top;')
    
    # Swap video
    content = content.replace(video_old, video_new)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
