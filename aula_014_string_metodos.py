curso = 'curso python'
print(curso.upper())
print(curso.lower())
print(curso.capitalize())
print(curso.title())

curso = '  python  '
print(curso.strip()) # 'python'
print(curso.lstrip()) # 'python  '
print(curso.rstrip()) # '  python'

curso = 'Python'
print(curso.center(20, '#'))
print('.'.join(curso))

nome_completo = ['Carlos', 'Alberto', 'Magno', 'Ferreira']
for nome in nome_completo:
    print(nome.center(20, '#'))
    