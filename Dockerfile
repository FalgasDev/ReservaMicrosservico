# Imagem base
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta usada pelo Flask
EXPOSE 5001

# Comando para iniciar a aplicação
CMD ["python", "app.py"]