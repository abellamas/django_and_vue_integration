from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Alumnos
from .serializers import AlumnosSerializer



class AlumnosView(APIView):
 
  def get(self,request,dni=None):
    if dni is None:
      alumnos_db = Alumnos.objects.all()
      alumnos_serializer = AlumnosSerializer(alumnos_db,many=True)
      return Response(alumnos_serializer.data, status=status.HTTP_200_OK)
    elif type(dni) is int:
      try:
        alumno_db = Alumnos.objects.get(dni=dni)
        alumno_db = AlumnosSerializer(alumno_db)
        return Response(alumno_db.data, status=status.HTTP_200_OK)
      except:
        return Response({'status': 'denied','errors':'El alumno no existe'},status=status.HTTP_404_NOT_FOUND)
        
  
  
  def post(self,request):
    alumnos = AlumnosSerializer(data=request.data)
    if alumnos.is_valid():
      alumnos.save()
      return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    else:
      return Response({'status': 'denied','errors':alumnos.errors},status=status.HTTP_400_BAD_REQUEST)
    
    
    
  def put(self,request,dni=None):
    try:
      if dni is not None:
        alumno_db = Alumnos.objects.get(dni=dni)
        alumno_serializer = AlumnosSerializer(alumno_db,data=request.data)
        if alumno_serializer.is_valid():
          alumno_serializer.save()
          return Response(alumno_serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'status': 'denied','errors':'No se pudieron guardar los cambios o el alumno no existe'},status=status.HTTP_404_NOT_FOUND)
    
      
  def delete(self,request,dni=None):
    try:  
      if dni is not None:
        alumno_db = Alumnos.objects.get(dni=dni)
        alumno_db.delete()
        return Response({'status': 'El alumno ha sido eliminado'}, status=status.HTTP_200_OK)
    except:
      return Response({'status': 'denied','errors':'No se pudo eliminar el alumno'},status=status.HTTP_404_NOT_FOUND)