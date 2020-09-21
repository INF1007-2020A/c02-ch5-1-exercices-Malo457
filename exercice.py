#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	sousTotal = 0
	for elem in data:
		sousTotal += elem[INDEX_QUANTITY]*elem[INDEX_PRICE]
	taxes = sousTotal * 0.15
	total = sousTotal + taxes
	reponse = name
	#{ce qu'on veut afficher : combien de caractère.quelle précision
	reponse += '\n' + f'SOUS TOTAL {sousTotal : >10.2f} $'
	reponse += '\n' + f'TAXES      {taxes : >10.2f} $'
	reponse += '\n' + f'TOTAL      {total : >10.2f} $'

	return reponse


def format_number(number, num_decimal_digits):
	entier = abs(int(number))
	decimal = abs(number) % 1.0
	ch_decimal = '.' + str(int(round(decimal * 10**num_decimal_digits)))
	chaineFinale = ch_decimal

	while entier >= 1000:
		digits = entier % 1000
		chaine = f" {digits:0>3}"
		chaineFinale = chaine + chaineFinale
		entier = entier // 1000

	chaineFinale = str(entier) + chaineFinale
	return ('-' if number < 0 else '') + chaineFinale

def get_triangle(num_rows):
	carBordure = '+'
	carTriangle = 'A'
	largeurTri = (num_rows - 1) * 2 + 1
	ligneBordure = carBordure * (largeurTri + 2)
	resultat = ligneBordure
	i = 0
	while i < num_rows:
		nombreCarac = 1 + i * 2
		caracTri = nombreCarac * carTriangle
		ligneTriangle = f'{caracTri: ^{largeurTri}}'
		resultat += '\n' + carBordure + ligneTriangle + carBordure
		i += 1
	resultat += '\n' + ligneBordure
	return resultat


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
