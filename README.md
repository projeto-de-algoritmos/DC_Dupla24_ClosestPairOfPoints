# DC_Dupla24_ClosestPairOfPoints

**Número da Lista**: 24<br>
**Conteúdo da Disciplina**: Dividir e Conquistar<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0117548  |  [Bruno Carmo Nunes](https://github.com/brunocmo) |
| 17/0150747  |  [Marcos Vinícius Rodrigues da Conceição](https://github.com/marcos-mv) |
## Video



## Sobre
A ideia do projeto é mini-game onde dado uma lista de pontos é aplicado o algoritmo para encontrar a menor distância entre dois pontos.

![portoRicoDelinear](docs/portoRicoDelinear.jpg)

Onde pode se observar abaixo a implementação dos postes em cada esquina de ruas, fazendo então uma conexão econômica e de acesso a todos da região.
Mostrando no final o mapa e o total de metros de cabo.

![portoRicoDF](docs/portoRicoDF.png)

## Screenshots

![mapaConsole](docs/mapaConsole.png)

![mapaConsolePrint](docs/mapaConsolePrint.png)

## Instalação
**Linguagem**: C++<br>

Feito e usado no kernel: **Linux 6.0.10-arch2-1 x86_64**

Tenha o *git*, *make* e o compilador *c++* versão C++11 instalado na sua maquina.
De preferência, para não ocorrer problemas, use o Ubuntu.

Para clonar:

`git clone https://github.com/projeto-de-algoritmos/Grafos2_OpticalFiberDistribution.git`

Para compilar o programa:

`make`

Para executar o programa:

`make run`

Para limpar os arquivos .o e bin do programa:

`make clean`

## Uso
Primeiro compile o programa com o `make` e depois execute o programa com `make run` , vai apresentar-se na tela inicial um menu, onde o usuário pode escolher imprimir o mapa, gerar o mapa com um nó inicial, fazer a mudança de distância entre os nós e limpar o mapa.

Para gerar o mapa basta pressionar a opção 2 e escolher um nó do mapa. Como resultado irá a aparecer as conexõe em azul e no final o tamanho de metros da fibra óptica.

Na opção 3, você pode fazer a mudança de distâncias entre os nós, onde cada mudança pode gerar um mapa diferente do que visto. Especificamente para gerar mudanças, tente reduzir as distâncias já mencionadas na imagem. Como por exemplo o nó 10 e o nó 24 pode ser reduzido para um valor de 100 metros. Com essa mudança outro mapa será gerado, com a distância no final.

Por fim a opção 0 para sair do programa.

## Outros
Quando executar o programa no CLI, use-o em tela cheia para melhor aproveitamento do mesmo.