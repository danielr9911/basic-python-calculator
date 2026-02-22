"""
Pruebas unitarias para la aplicación Flask.
"""
import pytest
import json
from app import app


class TestApp:
    """Clase de pruebas para la aplicación Flask."""
    
    @pytest.fixture
    def client(self):
        """Fixture que provee un cliente de prueba de Flask."""
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    
    def test_index_route(self, client):
        """Prueba que la ruta principal carga correctamente."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Calculadora' in response.data
    
    # Pruebas para el endpoint /calcular con suma
    def test_calcular_suma(self, client):
        """Prueba el endpoint de suma."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 5,
                                  'numero2': 3,
                                  'operacion': 'suma'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == 8
        assert data['operacion'] == 'suma'
    
    # Pruebas para el endpoint /calcular con resta
    def test_calcular_resta(self, client):
        """Prueba el endpoint de resta."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 10,
                                  'numero2': 3,
                                  'operacion': 'resta'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == 7
        assert data['operacion'] == 'resta'
    
    # Pruebas para el endpoint /calcular con multiplicación
    def test_calcular_multiplicacion(self, client):
        """Prueba el endpoint de multiplicación."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 4,
                                  'numero2': 5,
                                  'operacion': 'multiplicacion'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == 20
        assert data['operacion'] == 'multiplicacion'
    
    # Pruebas para el endpoint /calcular con división
    def test_calcular_division(self, client):
        """Prueba el endpoint de división."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 20,
                                  'numero2': 4,
                                  'operacion': 'division'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == 5
        assert data['operacion'] == 'division'
    
    # Pruebas de errores
    def test_calcular_division_por_cero(self, client):
        """Prueba que la división por cero devuelve error."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 10,
                                  'numero2': 0,
                                  'operacion': 'division'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert 'cero' in data['error'].lower()
    
    def test_calcular_operacion_invalida(self, client):
        """Prueba que una operación inválida devuelve error."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 5,
                                  'numero2': 3,
                                  'operacion': 'potencia'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_calcular_con_decimales(self, client):
        """Prueba operaciones con números decimales."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 5.5,
                                  'numero2': 2.5,
                                  'operacion': 'suma'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == 8.0
    
    def test_calcular_con_negativos(self, client):
        """Prueba operaciones con números negativos."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': -5,
                                  'numero2': 3,
                                  'operacion': 'suma'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == -2
    
    def test_calcular_datos_invalidos(self, client):
        """Prueba que datos inválidos devuelven error."""
        response = client.post('/calcular',
                              data=json.dumps({
                                  'numero1': 'abc',
                                  'numero2': 3,
                                  'operacion': 'suma'
                              }),
                              content_type='application/json')
        
        assert response.status_code in [400, 500]
        data = json.loads(response.data)
        assert 'error' in data
