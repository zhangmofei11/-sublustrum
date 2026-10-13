import os

ga4 = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LM3HC5J475"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-LM3HC5J475');
</script>'''

files = ['about.html', 'characters.html', 'lore.html', 'puzzles.html', 'privacy-policy.html', 'walkthrough.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping (not found): {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'G-LM3HC5J475' not in content:
        content = content.replace('    <style>', ga4 + '\n    <style>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated: {f}')
    else:
        print(f'Already has GA4: {f}')
