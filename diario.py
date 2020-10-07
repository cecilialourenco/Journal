#!/usr/bin/env python

import datetime

def data_e_hora():
    return datetime.datetime.today().strftime('%d/%m/%Y %H:%M')

def registro():
    escreva = input('Escreva sobre o seu dia: \n{}: '.format(data_e_hora()))
    escreva = escreva.strip()
    return escreva

arquivo = open('./diario.txt', 'a')
arquivo.write(data_e_hora() + ': ')
arquivo.write(registro() + '\n\n')
