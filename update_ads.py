import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/f664714ea35d28114691035ba6d27d45"></script>
<script data-cfasync="false" src="https://bauval.org/14/4b8b80784e41f776166db9b1753546da"></script>
<script>
  atOptions = {
    'key' : '48be807c658300c67ff992da310bb8eb',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/48be807c658300c67ff992da310bb8eb"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-f664714ea35d28114691035ba6d27d45"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'puzzles.html', 'characters.html', 'lore.html', 'about.html', 'privacy-policy.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '48be807c658300c67ff992da310bb8eb' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-f664714ea35d28114691035ba6d27d45' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
