# Instalar o requirements.txt

```bash
pip install -r requirements.txt
```

# Iniciar Alembic
```bash
python -m alembic init migrations
```

# Gerar a migrations
```bash
python -m alembic revision --autogenerate -m "Criar tabela usuarios"
```

# Aplicar a migration
```bash
python -m alembic upgrade head
```

# Rodar o código
```bash
python -m uvicorn app.main:app --reload
```