import os

# Folder containing the files
folder_path = 'Files'

# Inline body start and end HTML
bodyStart = '<body class="w3-light-grey">\n'
bodyEnd = '</body>\n</html>\n'

leftStart = '''
<!-- Left Column -->
<div class="w3-third">
  <div class="w3-white w3-text-grey w3-card-4">
'''

leftEnd = '''
  </div><br>
</div>
<!-- End Left Column -->
'''

pageContainerStart = '''
<!-- Page Container -->
<div class="w3-content w3-margin-top" style="max-width:1400px;">
'''

gridStart = '''
  <!-- The Grid -->
  <div class="w3-row-padding">
'''

rightColStart = '''
    <!-- Right Column -->
    <div class="w3-twothird">
'''

rightColEnd = '''
    </div>
'''

gridEnd = '''
  </div>
'''

pageContainerEnd = '''
</div>
'''

# File order with inline strings
file_order = [
    'header.txt',
    bodyStart,  # Insert body start
    'navbar.txt',
    pageContainerStart,
    gridStart,
    leftStart,
    'profile.txt',  # Profile content
    'aboutMe.txt',
    'skills.txt',  # Skills content
    'language.txt',  # Language content
    leftEnd,
    rightColStart,
    'techSkills.txt',
    'workEx.txt',  # Work experience content
    'education.txt',  # Education content
    'community.txt',
    'membership.txt',
    'training.txt',
    'publications.txt',  # Publications content
    rightColEnd,
    gridEnd,
    pageContainerEnd,
    'footer.txt',
    bodyEnd  # Insert body end
]

# Output file
output_file = 'index.html'

# Combine the files in the specified order
with open(output_file, 'w', encoding='utf-8') as outfile:
    for file_name in file_order:
        if isinstance(file_name, str) and (file_name.startswith('<') or file_name.startswith('\n')):  # Inline string (HTML tags)
            outfile.write(file_name)
            outfile.write('\n')
        elif isinstance(file_name, str):  # File from folder
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')  # Ensure proper line separation
            else:
                print(f"File not found: {file_name}")
