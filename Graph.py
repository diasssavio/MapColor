#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

class Graph:
	'''
	Classe de representação de um grafo
	'''

	# Attributes
	vertexes = []
	edges = []

	# Methods
	def __init__( self, vertexes, edges ):
		self.vertexes = vertexes
		self.edges = edges

	def __repr__( self ):
		pass

	'''
	Matriz de adjacencias que representa o grafo
	'''
	def adjacencyMatrix( self ):
		matrix = []

		for vertex in self.vertexes:
			matrix.append( getAdjacent( vertex ) )

		return matrix

	'''
	Obtem um vetor com as adjacencias ao vertice passado
	'''
	def getAdjacent( self, vertex ):
		adjacent = []

		for aux in self.vertexes:
			if aux[0] == vertex or aux[1] == vertex:
				adjacent.append( 1 )
			else:
				adjacent.append( 0 )

		return adjacent
