from flask import Flask, render_template_string, request

app = Flask(__name__)

# Aqui fica toda a parte visual do site (desenhos, cores e textos)
HTML_CODE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Minha Amiga Fofa 🐻</title>
    <style>
        body {
            background-color: #ffeef2;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 50px 20px;
            color: #d14969;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 10px 20px rgba(209, 73, 105, 0.1);
            max-width: 400px;
            margin: 0 auto;
        }
        h1 { font-size: 24px; }
        .ursinho { font-size: 60px; margin: 20px 0; }
        .botao {
            background-color: #ff6b8b;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 25px;
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
            display: inline-block;
            margin-top: 15px;
        }
        .botao:hover { background-color: #ff476f; transform: scale(1.05); }
        .mensagem { font-size: 18px; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <h1>Um recadinho especial... 🧸</h1>
    <div class="ursinho">🐻 💫 🐻</div>
    <p>Você é uma amiga incrível!</p>
    
    {% if etapa == 0 %}
        <!-- Estado inicial: Primeiro Botão -->
        <a href="/?passo=1" class="botao">Clique para mais! ✨</a>
    {% elif etapa == 1 %}
        <!-- Primeiro clique: Aparece o coração e novas palavras -->
        <div class="mensagem">❤️ Você enche o mundo de alegria! ❤️</div>
        <a href="/?passo=2" class="botao">Clique mais uma vez! 🥰</a>
    {% elif etapa == 2 %}
        <!-- Segundo clique: Mensagem Final super fofa -->
        <div class="mensagem">❤️ Você enche o mundo de alegria! ❤️</div>
        <div class="mensagem" style="color: #ff476f; margin-top: 15px;">
            🧸 Obrigado por ser essa amiga tão perfeita e insubstituível! ✨💖
        </div>
        <a href="/" class="botao" style="background-color: #bbb;">Ver de novo 🔄</a>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/')
def home():
    # Esse comando descobre em qual botão a sua amiga clicou
    passo = request.args.get('passo', 0, type=int)
    return render_template_string(HTML_CODE, etapa=passo)

if __name__ == '__main__':
    # Configuração obrigatória para que o site funcione na internet depois
    app.run(host='0.0.0.0', port=5000)
