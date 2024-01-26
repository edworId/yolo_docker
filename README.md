<h1 align="center"> YOLO em Docker com Python </h1>

O YOLO (You Only Look Once) é um inovador algoritmo de detecção de objetos em imagens e vídeos. Ao contrário de abordagens tradicionais, o YOLO realiza a detecção em uma única passagem pela imagem, dividindo-a em uma grade e predizendo as caixas delimitadoras e as probabilidades de classes simultaneamente. Essa eficiência permite que o YOLO alcance velocidades em tempo real, sendo amplamente utilizado em aplicações que requerem detecção rápida e precisa, como veículos autônomos, vigilância por vídeo e análise de imagens médicas.

Já o Docker é uma plataforma de código aberto que simplifica a implantação e gerenciamento de aplicativos em contêineres. Contêineres são unidades leves e portáteis que encapsulam o código, suas dependências e configurações, garantindo consistência em diferentes ambientes. Uma das principais funcionalidades do Docker é a capacidade de isolar aplicativos em contêineres, eliminando inconsistências entre ambientes de desenvolvimento, teste e produção. Além disso, o Docker permite a rápida escalabilidade e distribuição de aplicativos, facilitando a integração contínua e a entrega contínua.

<h2>VANTAGENS: </h2>
	
	- O Docker é rápido: Ao contrário de uma máquina virtual, seu aplicativo inicializa em alguns segundos e para com a mesma rapidez.
	- O Docker é multiplataforma: Você pode iniciar seu contêiner em qualquer sistema.
	- Os contêineres podem ser construídos e excluídos mais rápido do que em uma máquina virtual.
	- Não há mais dificuldades em configurar seu ambiente de trabalho: Depois que seu Docker estiver configurado, você nunca mais terá que reinstalar suas dependências manualmente mesmo se mudar seu computador.
	- Você mantém seu espaço de trabalho limpo, pois cada um de seus ambientes será isolado e você pode excluí-los a qualquer momento, sem impactar o resto.
	- É mais fácil implantar seu projeto no servidor para colocá-lo online.

<h2>DESVANTAGENS: </h2>
	
	- Há uma tonelada de solicitações de recursos para upgrade que ainda estão em andamento (como capacidade de autorregistro e autoinspeção de contêineres, cópia de arquivos do host para o contêiner e muito mais).
	- Há momentos em que um container fica inativo, então depois disso, ele precisa de uma estratégia de backup e recuperação, embora existam várias soluções, mas que não são automatizadas ou nem muito escaláveis ainda.
	- Em comparação com as máquinas virtuais, os contêineres Docker oferecem menos sobrecarga, mas não sobrecarga zero.
	- O principal problema é que se um aplicativo projetado para ser executado em um contêiner do Docker no Windows, ele não pode ser executado no Linux ou vice-versa. No entanto, as máquinas virtuais não estão sujeitas a essa limitação.
	- Podemos dizer que, para aplicativos que requerem interfaces ricas, o Docker não é uma boa solução.

<h1 align="center">  </h1>
<p align="center">
<img width="900", img src="https://github.com/edworId/facial_emotion_detection/blob/main/menu.png"/>
</p>

<h6 align="center"> Estrutura Docker </h6>

Este projeto fornece uma implementação fácil e rápida para executar o YOLO (You Only Look Once) em um ambiente Docker usando Python. O YOLO é um algoritmo de detecção de objetos em imagens e vídeos em tempo real.

## Pré-requisitos

Certifique-se de ter o Docker instalado em sua máquina antes de prosseguir. Você pode encontrar instruções de instalação [aqui](https://docs.docker.com/get-docker/).

```
sudo apt update && sudo apt upgrade
```
```
curl -fsSL https://get.docker.com | bash
```

## DOCKER IMAGE: 
Nesta etapa, você escreve um Dockerfile que cria uma imagem do Docker. A imagem contém todas as dependências que o aplicativo Python precisa, incluindo o próprio Python.

### Exemplo de Imagem:

```
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

Agora você deve rodar o código abaixo para poder construir a sua imagem

```
docker build -t nome_da_imagem .
```

## Instruções de Uso da Docker

```
$ docker ps (LISTAR CONTAINERS)
$ docker ps -a (LISTAR CONTAINERS ATIVOS E INATIVOS)
$ docker start container_id  (Starta o container que está parado) 
$ docker exec - it container_id bash  (Entramos dentro da docker em root)
$ docker inspect container_id  (Inspeção)
$ docker run -p 2300:5000 -d docker_image  (conectar entre ips)
$ docker rm 'container' (Remove containers indesejados)
$ docker rmi 'imagem' (Remove imagens indesejados)
```

    
<h1 align="center">  </h1>

CLONE: git clone 

<h1 align="center"> Autores </h1>

| [<img src="https://avatars.githubusercontent.com/u/110691832?s=400&u=e671447386d38975c165bff78b715ea80549c069&v=4" width=115><br><sub>Edmundo Lopes Silva</sub>](https://github.com/edworId) |  
| :---: |

<p align="center">
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>
</p>
