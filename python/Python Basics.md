##### Type conversions

- _int_
- _float_
- _string_
- _None_

```python
i = 42
type(1) #int
f = float(i)
printf(f) #42.0
type(f) #float
let = 'string'
```
 
 ## Strings

| P | Y | T | H | O | N
----| ----| ----| ----| ----| ----| 
0 | 1 | 2 | 3 | 4 | 5

_Example_

```python
let python = 'PYTHON'
print(python[0:5])
```

 | P | Y | T | H | O | N
----| ----| ----| ----| ----| ----| 
==0== | ==1== |==2== | ==3== | ==4== | 5


```python
print(python[6:7])
```
 | P | Y | T | H | O | N
----| ----| ----| ----| ----| ----| 
==0== |1 |2 | 3 | 4 | 5
	
#### In as a logical Operator
```python
fruit = 'banana'
(n in fruit) #true
```

#### String library
 - `_dir()_` <- mostra todas os métodos que podemos utilizar (built-in methods).

| . | . |
----|  ----|
| str.center(width) | str.lower()
| str.replace(old, new) | str.upper()
| str.strip() | str.find()

- `str.find()` retorna o primeiro index da string em questão.
- `len()` retorna o tamanho; pode ser usado também em listas.
- `split()` produz uma lista contendo strings.;

#### Listas
- `range(len(list)` 
```python
friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends))...
```

###### Concatenando listas
```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```
###### Slice
```python
>>> t = [9, 41, 12, 3, 74, 15]
>>> t[1:3]
[41, 12]
>>> t[:4]
[9, 41, 12, 3]
>>> t[3:]
[3, 74, 15]
>>> t[:]
[9, 41, 12, 3, 74, 15]
```
###### Methods
- `append()`  adicionar um valor no fim de uma lista.
- `list()` instancia para uma lista.
- `max()`, `min()`
- `sum()`

#### Dicionários

_São como objetos em javascript._
```python
>>> purse = dict()
>>> purse['money'] = 12
>>> purse['candy'] = 3
>>> purse['tissues'] = 75
>>> print(purse)
{'money':12, 'tissues': 75, 'candy': 3}
```

.`get()` verifica se uma key existe no dicionário.
```python
counts = dict()
for name is names:
	counts[name] = counts.get(name, 0) #0 valor default
```

### Retrieving dictonaries/lists
- `list()` instancia uma lista.
- `dictonarie.keys()` retorna chaves de valores.
- `dictonarie.values()` retorna valores.
- `dictonarie.items()` retorna tupla (key, value); (objeto -> javascript).

##### Método parecido com javascript

```python
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100 }
for aaa, bbb in jjj.items():
	print(aaa, bbb)
```


### Tuplas

_Parecidas com listas, porém, são imutaveis._

- Prefere-se tuplas ao invés de listas para criar variaveis temporarias.

#### formas de instancia
```python
>>> (x, y) = (4, 'fred')
>>> print(y)
fred
```
 
 ### Sorting lists of tuples
 
 - `sorted()` retorna lista de tuplas.
 
 ```python
 >>> d = {'a':10, 'b':1, 'c': 22}
 >>> sorted(d.items())
 [('a', 10), ('b', 1), ('c', 22)]
 ```
 
 ### Rede
 
  - TCP: Peer-to-Peer Conection
  - Port: application-specific or process-specific software communications endpoints.; Permite que varias aplicações coexistem na mesma rede.
  - Socket: endpoint of a bidirecional inter-process communication flow accross an internet Protocol-based computer network.

##### Comoon tcp ports
- Telnet (23) - Login 
- SSH (22) - Secure Login
- HTTP (80)
- HTTPS (443)
- SMTP (Mail)
- IMAP (143/220/993) - Mail
- POP (109/110) Mail retrieval
- DNS (53) - Domain Name
- FTP (21) - File Transfer

##### Htpp
- Inventado para a web com o intuito de buscar por imagens documentos etc.
- Contem regras para que os navegadores deem acesso aos documentos no servidor.

