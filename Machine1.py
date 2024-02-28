from BaseSimulation import SlotMachine
import itertools

points_400= {"AAA":400}
combo_200 = [''.join(candidate) for candidate in itertools.product('AB', 'AB', 'AB')]
points_200 = {combo: 200 for combo in combo_200}
combo_50 = [''.join(candidate) for candidate in itertools.product('ACDEF', 'ACDE', 'ACDE')]
points_50 = {combo: 50 for combo in combo_50}
combo_10 = [''.join(candidate) for candidate in itertools.product('AGHIJK', 'AFGHIJK', 'AFGHIJK')]
points_10 = {combo: 10 for combo in combo_10}
combo_5a = [''.join(candidate) for candidate in itertools.product('ABCDEFGHIJK', 'ABCDEFGHIJK', 'ABCDEFGHIJK')]
points_5a = {combo: 5 for combo in combo_5a}
combo_5b = ['AA' + letter for letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_5b = {combo: 5 for combo in combo_5b}
combo_5c = ['A' + letter + 'A' for letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_5c = {combo: 5 for combo in combo_5c}
combo_5d = [letter + 'AA'  for letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_5d = {combo: 5 for combo in combo_5d}

combo_2a = ['A{}{}'.format(second_letter, third_letter) for second_letter in 'ABCDEFGHIJKLMNOPQRSTUV' for third_letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_2a = {combo: 2 for combo in combo_2a}
combo_2b = ['{}A{}'.format(first_letter, third_letter) for first_letter in 'ABCDEFGHIJKLMNOPQRSTUV' for third_letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_2b = {combo: 2 for combo in combo_2b}
combo_2c = ['{}{}A'.format(first_letter, second_letter) for first_letter in 'ABCDEFGHIJKLMNOPQRSTUV' for second_letter in 'ABCDEFGHIJKLMNOPQRSTUV']
points_2c = {combo: 2 for combo in combo_2c}

pointsdict = {}
dictionaries_to_update = [points_2a, points_2b, points_2c, points_5a, points_5b, points_5c, points_5d, points_10, points_50, points_200, points_400]

for dictionary in dictionaries_to_update:
    pointsdict.update(dictionary)


slot1 = SlotMachine(3, pointsdict)

print(slot1.simulation(1000,200000,1))


