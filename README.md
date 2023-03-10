# Flask API
Um exemplo simples de como utilizar uma api. Ideal para estudos e ensinar a sua utilização com os demais.

# Utilizando o curl para gerenciar a API

## Listar produtos

```bash
curl -X GET http://localhost:5000/produtos
```

## Buscar produtos

```bash
curl -X GET http://localhost:5000/produtos/1
```

## Adicionar um novo produto

```bash
curl -X POST -H "Content-Type: application/json" -d '{"nome":"cafeteira", "preco":100.0, "quantidade":5}' http://localhost:5000/produtos
```

## Atualizando as informações e um produto

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"nome":"cafeteira", "preco":110.0, "quantidade":10}' http://localhost:5000/produtos/1
```

## Deletar um produto pelo seu ID


```bash
curl -X DELETE http://localhost:5000/produtos/1

