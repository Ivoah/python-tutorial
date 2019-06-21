import re

chapter_re = re.compile(r'\[(.*)\]\((.*)\)')

with open('all.md', 'w') as all:
    with open('toc.md') as toc:
        files = chapter_re.findall(toc.read())
    
    all.writelines(
        ['# Table of Contents\n', '\n']
        + [f'* [{t}](#{"-".join(t.lower().split())})\n' for t, f in files]
        + ['\n']
    )

    all.write('\n'.join(open(f).read() for _, f in files))
