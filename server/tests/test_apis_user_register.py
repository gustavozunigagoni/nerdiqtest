import unittest
from quart import Quart, json
from asynctest import TestCase

from apis.user import user

class TestApp(TestCase):

    async def setUp(self) -> None:
        self.app = Quart(__name__)
        self.app.register_blueprint(user)
        self.client = self.app.test_client()

    async def test_port_register(self):
        data = {
            "email": "gustavozunigagoni@yahoo.com",
            "nombre": "ana lucrecia mendes murillo",
            "password": "contrasena_cifrada"
        }
        response = await self.client.post('/register', json=data)

        self.assertEqual(response.status_code, 200)
        result = await response.get_json()
        self.assertEqual(result['message'], 'Confirmation email sent')

if __name__ == '__main__':
    unittest.main()
