#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

class Graph:
	'''
	Classe de representação de um grafo
	'''

	vertexes = []
	edges = []

	def __init__( self ):
		self.vertexes = []
		self.edges = []

	def __init__( self, vertexes, edges ):
		self.vertexes = vertexes
		self.edges = edges

	def __repr__( self ):
		pass

	def adjacencyMatrix( self ):
		adjacencyMatrix = []