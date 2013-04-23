#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import Graph
import GeneticAlgorithm

def main():
	vertexes = [ 'RR', 'AP', 'AM', 'PA', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'AC'\
				'RO', 'MT', 'TO', 'BA', 'MS', 'GO', 'DF', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS' ]
	
	edges = [ ( 'RR', 'PA' ), ( 'RR',  'AM' ) \
			( 'AP', 'AM' ) \
			( 'AM', 'PA'), ( 'AM', 'MT' ), ( 'AM', 'RO' ), ( 'AM', 'AC' ) ]

	graph = Graph( vertexes, edges )

	# geneticAlgorithm = GeneticAlgorithm(  )

if __name__ == '__main__':
	main()