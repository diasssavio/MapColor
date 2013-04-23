#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

from random import randint

class GeneticAlgorithm( object ):
	'''
	Classe de implementação do algoritmo genético
	'''

	# Attributes
	populationAmount = 0
	genesAmount = 0
	generations = 0
	crossingRate = 0
	mutationRate = 0

	adjacencyMatrix = None
	colors = []

	population = []
	populationFitness = []
	
	'''
	Construtor da classe
	'''
	def __init__( self, populationAmount, genesAmount, generations, crossingRate, mutationRate, adjacencyMatrix ):
		self.populationAmount = populationAmount
		self.genesAmount = genesAmount
		self.generations = generations
		self.crossingRate = crossingRate
		self.mutationRate = mutationsRate
		self.adjacencyMatrix = adjacencyMatrix

		self.colors = [ 'Vermelho', 'Verde', 'Azul', 'Amarelo' ]

		self._run()

	'''
	Função que retorna representação da instancia
	'''
	def __repr__( self ):
		pass

	# Main method from genetic algorithm
	'''
	Função que executa o loop do AG
	'''
	def _run( self ):
		self.initPopulation()

		for i in range( self.generations ):
			self.fitness( self.population )

			selection()

	'''
	Faz a distribuição da porcentagem relativa de seleção para cada cromossomo
	baseado em seu fitness
	'''
	def _roulette( self ):
		pass

	def _adjacent( self, vertex ):
		adjacent = []

		for i in range( self.adjacencyMatrix.__len__() ):
			if self.adjacencyMatrix[ vertex ][i]:
				adjacent.append( i )

		return adjacent

	# Methods
	'''
	Inicializa a população com valores aleatórios para seus genes
	'''
	def initPopulation( self ):
		for i in range( self.populationAmount ):
			chromosome = ""

			# Sorting genes
			for j in range( self.genesAmount ):
				chromosome += str( randint( 0, self.colors.__len__() - 1 ) )

			self.population.append( chromosome )

	'''
	Calcula a aptidão de todos os individuos da população
	'''
	def fitness( self, population ):
		fit = []

		# Iterating through population
		for chromosome in population:
			chromosomeFit = 0

			# Iterating through genes in chromosome
			for gene in chromosome:
				neighbors = self._adjacent( int( gene ) )

				for neighbor in neighbors:
					if chromosome[neighbor] != gene:
						chromosomeFit += 1

			fit.append( chromosomeFit )

		return fit

	'''
	Realiza a seleção dos filhos que farão parte da população
	'''
	def selection( self ):
		pass

	def crossing( self ):
		pass

	def mutation( self ):
		pass