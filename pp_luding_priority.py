rake_club = float(input('Какой общий рейк за неделю?'))
rakeback = float(input('Сколько рб у игроков?'))
rake_me = float(input('Сколько я накрутил?'))
rake_vitalik = float(input('Сколько накрутил Виталик?'))
winrate_me = float(input('Как я выступил?'))
winrate_vitalik = float(input('Как выступил Виталик?'))
rebate_club = float(input('Какой общий ребейт?'))
overlay = float(input('Какой оверлей?'))

rebate_my = abs(winrate_me + rake_me)*0.1
rebate_vitalik = abs(winrate_vitalik + rake_vitalik)*0.1

if (winrate_me + rake_me) >=0:
    my = (rake_me * 0.83) + winrate_me - rebate_my
else:
    my = (rake_me * 0.83) + winrate_me + rebate_my

if (winrate_vitalik + rake_vitalik) >=0:
    vitalik = (rake_vitalik * 0.83) + winrate_vitalik - rebate_vitalik
else:
    vitalik = (rake_vitalik * 0.83) + winrate_vitalik + rebate_vitalik


ostatok = (rake_club - rake_vitalik - rake_me - rakeback) * 0.83 + (rebate_club - rebate_vitalik - rebate_my)

my_funds = my + ostatok/2 - overlay/2

print(my_funds)















