from BaseSimulation import SlotMachine2
import itertools

points_200= {"AAA":200}
combo_50 = [''.join(candidate) for candidate in itertools.product('AB', 'AB', 'AB')]
points_50 = {combo: 50 for combo in combo_50}
combo_20 = [''.join(candidate) for candidate in itertools.product('ACDEF', 'ACDE', 'ACDE')]
points_20 = {combo: 20 for combo in combo_20}
combo_8 = [''.join(candidate) for candidate in itertools.product('AGHIJK', 'AFGHIJK', 'AFGHIJK')]
points_8 = {combo: 8 for combo in combo_8}
combo_3a = [''.join(candidate) for candidate in itertools.product('ABCDEFGHIJK', 'ABCDEFGHIJK', 'ABCDEFGHIJK')]
points_3a = {combo: 3 for combo in combo_3a}
combo_3b = ['AA' + letter for letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_3b = {combo: 3 for combo in combo_3b}
combo_3c = ['A' + letter + 'A' for letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_3c = {combo: 3 for combo in combo_3c}
combo_3d = [letter + 'AA'  for letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_3d = {combo: 3 for combo in combo_3d}

combo_2a = ['A{}{}'.format(second_letter, third_letter) for second_letter in 'ABCDEFGHIJKLMNOPQRSTUV' for third_letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_2a = {combo: 2 for combo in combo_2a}
combo_2b = ['{}A{}'.format(first_letter, third_letter) for first_letter in 'ABCDEFGHIJKLMNOPQRSTUV' for third_letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_2b = {combo: 2 for combo in combo_2b}
combo_2c = ['{}{}A'.format(first_letter, second_letter) for first_letter in 'ABCDEFGHIJKLMNOPQRSTUV' for second_letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_2c = {combo: 2 for combo in combo_2c}

pointsdict4 = {}
dictionaries_to_update4 = [points_2a, points_2b, points_2c, points_3a, points_3b, points_3c, points_3d, points_8, points_20, points_50, points_200]

for dictionary in dictionaries_to_update4:
    pointsdict4.update(dictionary)


slot4 = SlotMachine2(3, pointsdict4)

print(slot4.simulation(10000,100000,1))


