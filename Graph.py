#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

class Graph:
	'''
	Classe de representação de um grafo
	'''

	vertexes = []
	edges = []

	def __init__( self, vertexes, edges ):
		self.vertexes = vertexes
		self.edges = edges

	def __repr__( self ):
		pass

	def adjacencyMatrix( self ):
		adjacencyMatrix = []
		for vertex in vertexes:
			line = []
			adjacent = getAdjacent( vertex )
			for adj in adjacent:
				line.append(  )

			adjacentMatrix.append( line )

	'''

	'''
	def getAdjacent( self, vertex ):
		adjacent = []

		for edge in self.edges:
			if edge[0] == vertex:
				adjacent.append( edge[0] )
			elif edge[1] == vertex:
				adjacent.append( edge[1] )

		return adjacent
