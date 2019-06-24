import re

chapter_re = re.compile(r'\[(.*)\]\((.*)\)')

with open('README.md', 'w') as all:
    with open('toc.md') as toc:
        files = chapter_re.findall(toc.read())
    
    all.writelines(
        ['# Table of Contents\n', '\n']
        + [f'* [{t}](#{"-".join(t.lower().split())})\n' for t, f in files]
        + ['\n']
    )

    body = '\n'.join(open(f).read() for _, f in files)
    all.write(re.sub(r'\(.*\.md(#.*)\)', r'(\1)', body))
