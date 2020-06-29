## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone 
python -m venv .venv
.venv/Script/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```