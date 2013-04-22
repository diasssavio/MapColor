#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

from random import randint

class GeneticAlgorithm( object ):
	'''
	Classe de implementação do algoritmos genéticos
	'''

	'''
	Construtor da classe
	'''
	def __init__( self, populationAmount, genesAmount, generations, crossingRate, mutationRate ):
		self.populationAmount = populationAmount
		self.genesAmount = genesAmount
		self.generations = generations
		self.crossingRate = crossingRate
		self.mutationRate = mutationsRate

		self.colors = { 0 : 'Vermelho', 1 : 'Verde', 2 : 'Azul', 3 : 'Amarelo' }

		self._run()

	'''
	Função que retorna representação da instancia
	'''
	def __repr__( self ):
		pass

	'''
	Função que executa o loop do AG
	'''
	def _run( self ):
		self.initPopulation()

		for i in range( self.generations ):
			self.fitness()

			selection()

	def _roulette( self ):
		pass

	'''
	Inicializa a população com valores aleatórios para seus genes
	'''
	def initPopulation( self ):
		self.population = []

		for i in range( self.populationAmount ):
			chromosome = ""

			for j in range( self.genesAmount ):
				chromosome += str( randint( 0, self.colors.__len__() - 1 ) )

			self.population.append( chromosome )

	'''
	Calcula a aptidão de todos os individuos da população
	'''
	def fitness( self ):
		pass

	'''

	'''
	def selection( self ):
		pass

	def crossing( self ):
		pass

	def mutation( self ):
		pass