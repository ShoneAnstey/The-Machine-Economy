import sys
import os

filename = sys.argv[1]
with open(filename, 'r') as f:
    content = f.read()

# Debug: verify what we are reading
# with open('debug_log.txt', 'a') as f:
#     f.write(f"Editing {filename}\nContent start: {content[:100]}\n")

# If it's the sequence list (contains 'pick <hash>')
# We identify this by checking for lines starting with pick and containing our target hashes
if 'pick ' in content and 'commit' not in content:
    # We need to replace pick with reword for the specific commits
    # 9bc08e7 Remove accidentally tracked...
    # cab864b Polish PDF layout...
    # 5e8bf83 Add PDF download link...
    
    # We use simpler logic: replace the command for the lines containing the hash
    new_lines = []
    for line in content.splitlines():
        if line.startswith('pick 9bc08e7') or line.startswith('pick 9bc08e7'):
            line = line.replace('pick ', 'reword ')
        elif line.startswith('pick cab864b') or line.startswith('pick cab864b'):
            line = line.replace('pick ', 'reword ')
        elif line.startswith('pick 5e8bf83') or line.startswith('pick 5e8bf83'):
            line = line.replace('pick ', 'reword ')
        new_lines.append(line)
    
    with open(filename, 'w') as f:
        f.write('\n'.join(new_lines))
    sys.exit(0)

# If we are editing a commit message (the filename is usually COMMIT_EDITMSG)
if "COMMIT_EDITMSG" in filename or True: # Fallback to checking content
    # Use 'in' check for robustness matching the old message
    if "Remove accidentally tracked HTML file from assets" in content:
        with open(filename, 'w') as f:
            f.write("chore: cleanup assets directory")
    elif "Polish PDF layout" in content:
        with open(filename, 'w') as f:
            f.write("style: professional PDF layout and formatting")
    elif "Add PDF download link to README" in content:
        with open(filename, 'w') as f:
            f.write("docs: update README with document links")
