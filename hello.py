from dotenv import load_dotenv
import os

load_dotenv()

senha = os.getenv("SENHA")

print("A senha é:", senha)
print("nova funcionalidade")