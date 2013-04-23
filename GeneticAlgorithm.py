#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

from random import randint

class GeneticAlgorithm( object ):
	'''
	Classe de implementação do algoritmos genéticos
	'''

	# Attributes
	populationAmount = 0
	genesAmount = 0
	generations = 0
	crossingRate = 0
	mutationRate = 0
<<<<<<< HEAD

	colors = {}
	population = []

=======
	adjacency = []
	colors = {}

	population = []


>>>>>>> [Updated] Graph & GeneticAlgorithm
	'''
	Construtor da classe
	'''
	def __init__( self, populationAmount, genesAmount, generations, crossingRate, mutationRate, adjacency ):
		self.populationAmount = populationAmount
		self.genesAmount = genesAmount
		self.generations = generations
		self.crossingRate = crossingRate
		self.mutationRate = mutationsRate
		self.adjacency = adjacency

		self.colors = { 0 : 'Vermelho', 1 : 'Verde', 2 : 'Azul', 3 : 'Amarelo' }

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

	# Methods
	'''
	Inicializa a população com valores aleatórios para seus genes
	'''
	def initPopulation( self ):
		for i in range( self.populationAmount ):
			chromosome = ""

			for j in range( self.genesAmount ):
				chromosome += str( randint( 0, self.colors.__len__() - 1 ) )

			self.population.append( chromosome )

	'''
	Calcula a aptidão de todos os individuos da população
	'''
	def fitness( self, population ):
		# Iterating through population
		for chromosome in population:
			chromosomeFit = 0

			# Iterating through genes in chromosome
			for gene in chromosome:
				
				

	'''
	Realiza a seleção dos filhos que farão parte da população
	'''
	def selection( self ):
		pass

	def crossing( self ):
		pass

	def mutation( self ):
		pass