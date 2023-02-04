# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

english = [{'1':'aeioulnstr'},{'2':'dg'},{'3':'bcmp'},{'4':'fhvwy'},{'5':'k'},{'8':'jx'},{'10':'qz'}]
russian = [{'1':'авеинорст'},{'2':'дклмпу'},{'3':'бгёья'},{'4':'йы'},{'5':'жзхцч'},{'8':'шэю'},{'10':'фщъ'}]
wordEnglish = input('введите слово на английском языке: ').lower()
wordRussian = input('Ведите слово на русском языке: ').lower()
countEngl =0
countRus= 0
for letter in wordEnglish:
    for element in english:
        for value in element.values():
            if letter in value:
                for key in element.keys():
                    countEngl+=int(key)
print('Стоимость введённого Вами англиского слова ', wordEnglish , ' равна: ', countEngl, ' очков')
print()
for letter in wordRussian:
    for element in russian:
        for value in element.values():
            if letter in value:
                for key in element.keys():
                    countRus+=int(key)
print('Стоимость введённого Вами русского слова ', wordRussian, ' равна: ', countRus, ' очков')
