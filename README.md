# Banco imobiliário

Um simples script para simular o desempenho de alguns "perfis" de jogador
em uma partida de banco imobiliário.

## Instalando dependências

As dependências devem ser instaladas preferencialmente em um ambiênte virtual.

```bash
virtualenv --system-site-packages -p python3 bancoimob-venv3
# or
python3 -m bancoimob-venv3

source bancoimob-venv3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

```bash
python3 run.py #Exibe no console as estatísticas
                # das 300 simulações realizadas
# or

python3 run.py 300 #Permite escolher a quantidade
                    # de simulações que será realizada.
```

## Comentários

Algumas classes não foram escritas da maneira mais otimizada possível
como a classe Player, por exemplo, a intenção primária foi atender todos
os requisitos do desafio técnico.

## License
[MIT](https://choosealicense.com/licenses/mit/)