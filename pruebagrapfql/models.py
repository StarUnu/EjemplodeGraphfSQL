from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


'''
para poner datos :)
mutation {
  createUser(firstName: "Jhon", lastName: "Smith") {
    id
    firstName
    lastName
  }
}
'''
'''
Consultar que ya se creo

query{
  users{
    id
    firstName
    lastName
  }
}
'''
'''
Instalación de react
create-react-app my-app
cd my-app
npm install react-scripts@2.1.8
npm start'''