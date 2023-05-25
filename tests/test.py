import unittest
from src.models import db, EmployeeModel
from src.app import app


class MyTest(unittest.TestCase):
    def setUp(self):
        # Criar uma instância de aplicação Flask para os testes
        self.app = app
        self.app.config['TESTING'] = True

        # Configurar a conexão com o banco de dados em memória
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Inicializar o banco de dados
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_employee(self):
        with self.app.test_client() as client:
            # Simular uma solicitação POST para a rota de criação
            response = client.post('/data/create', data={
                'cpf': 12345678901,
                'name': 'John Doe',
                'age': 30,
                'position': 'Manager',
                'address': '123 Main St'
            })

            # Verificar se a resposta é um redirecionamento
            self.assertEqual(response.status_code, 302)

            # Verificar se o funcionário foi criado no banco de dados
            with self.app.app_context():
                employee = EmployeeModel.query.filter_by(cpf='12345678901').first()
                self.assertIsNotNone(employee)
                self.assertEqual(employee.name, 'John Doe')

    # Adicione mais testes para outras rotas e funcionalidades


if __name__ == '__main__':
    unittest.main()
