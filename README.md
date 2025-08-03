# 🦠 Simulação Epidêmica com Autômatos Celulares (Modelo SEIR)

Este projeto implementa uma simulação visual da propagação de uma epidemia em uma população modelada como uma grade de autômatos celulares. Utiliza o modelo **SEIR** (Suscetível, Exposto, Infectado, Recuperado) com interações locais entre indivíduos.

Cada célula da grade representa um indivíduo, e a doença se propaga com base em regras probabilísticas, levando em conta a vizinhança imediata.

## 📄 Documento Explicativo

> Para uma explicação teórica e detalhada do modelo, consulte o arquivo [Modelo_SEIR_Autômatos_Celulares_Pablo.docx](), incluído neste repositório.

---

## ✅ Requisitos

Para rodar esta simulação, você precisa do Python 3 e dos seguintes pacotes:

- `pygame`
- `numpy`

Você pode instalá-los com:

```bash
pip install pygame numpy
````

---

## ▶️ Como Executar

Clone o repositório e execute o arquivo principal com Python:

```bash
python simulador_epidemia.py
```

Durante a simulação:

* Pressione **`R`** para reiniciar a simulação a qualquer momento.
* A janela exibirá a evolução da epidemia ao longo do tempo.

---

## 🎨 Representação de Cores

| Estado     | Cor          |
| ---------- | ------------ |
| Suscetível | Azul         |
| Exposto    | Laranja      |
| Infectado  | Vermelho     |
| Recuperado | Verde        |

---

## 🧪 Parâmetros do Modelo

Você pode ajustar os parâmetros diretamente no código-fonte:

* `BETA`: probabilidade de contágio (default: `0.15`)
* `SIGMA`: taxa de incubação (default: `0.05`)
* `GAMMA`: taxa de recuperação (default: `0.02`)
* `GRID_SIZE`: tamanho da grade (default: `100x100`)
* `INITIAL_INFECTED_COUNT`: número inicial de infectados (default: `1`)

---

## 📘 Referências

* Keeling, M. J., & Rohani, P. (2008). *Modeling Infectious Diseases in Humans and Animals*. Princeton University Press.
* Schiff, J. L. (2008). *Cellular Automata: A Discrete View of the World*. Wiley-Interscience.

