#Faça uma função que, dado uma string sep e uma lista l de
#strings, concatena as strings de l usando sep como separador:

def concatena_strings(l,sep):
	"""Retorna uma string formada pela concatenação das strings de l usando sep como separador

	Parâmetros:
	l -- A lista que contém as strings a serem concatenadas
	sep -- A string se separação das strings a serem concatenadas
	"""
	string = ""
	n = len(l)
	for i in range(n):
		if i == n - 1:
			string = string + l[i]
		else:
			string = string + l[i] + sep
	return string

