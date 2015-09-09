# -*- coding: utf-8 -*-
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Permiso custom para solo permitir que los dueños de un Snippet
	puedan editarlo
	"""
	def has_object_permission(self, request, view, obj):
		# Permisos de lectura son permitidos para cualquier peticion,
		# asi que siempre vamos a permitir peticiones GET, HEAD o OPTIONS
		if request.method in permissions.SAFE_METHODS:
			return True

		# Permisos de escritura solo son permitidos al dueño del Snippet
		return obj.owner == request.user